#!/usr/bin/env python3
"""Run fresh Codex sessions sequentially; no reference answers in case directory."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROMPT='''Fă un review independent al dosarului de documente din directorul curent. Verifică afirmațiile și deciziile propuse folosind numai faptele și regulile din dosar. Nu ai acces la un raport de referință.
Întrebarea beneficiarului: {task}
Citește toate fișierele .md din directorul curent. Lucrează numai pe acest dosar, fără alte directoare sau internet.
Identifică toate problemele materiale, contradicțiile, erorile și sursele de confuzie; nu presupune un număr fix de findinguri. Findingurile suplimentare sunt binevenite dacă pot fi demonstrate din documente. Pentru fiecare concluzie oferă probe cu numele fișierului și eticheta pasajului și o scurtă deducție. Distinge faptele certe de necunoscute. Include și aspecte corecte și un rezumat final coerent cu analiza. Răspunde în română, în Markdown, fără să modifici fișierele.
'''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--model',default='gpt-6.1-terra')
    ap.add_argument('--isolation',choices=['strict','context'],default='strict')
    ap.add_argument('--effort',choices=['low','medium','high','xhigh'],default='medium')
    ap.add_argument('--case',action='append',dest='cases')
    ap.add_argument('--run-id',default=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    ap.add_argument('--timeout',type=int,default=600)
    args=ap.parse_args()
    cli_version=subprocess.run(['codex','--version'],capture_output=True,text=True,check=True).stdout.strip()
    source_sha256={name:hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()
                   for name in ['run_eval.py','isolation.py','cases.py',*sorted(p.name for p in (ROOT/'scripts').glob('case_*.py'))]}
    workroot=ROOT/'.work'
    workroot.mkdir(exist_ok=True,mode=0o700)
    manifest=json.loads((ROOT/'manifest.json').read_text())
    batch=ROOT/'results'/args.run_id
    batch.mkdir(exist_ok=True)
    if (batch/'manifest.json').exists():
        if json.loads((batch/'manifest.json').read_text())!=manifest:
            ap.error('Run-id already belongs to a different corpus; use a new run-id')
    else:
        shutil.copyfile(ROOT/'manifest.json',batch/'manifest.json')
    if args.cases and set(args.cases)-{c['id'] for c in manifest}:
        ap.error('Unknown case')
    for c in manifest:
        if args.cases and c['id'] not in args.cases: continue
        out=ROOT/'results'/c['id']/'runs'/args.run_id
        out.mkdir(parents=True,exist_ok=False)
        shutil.copyfile(ROOT/'manifest.json',out/'manifest.json')
        prompt=PROMPT.format(task=c['task'])
        (out/'prompt.md').write_text(prompt)
        snapshot=out/'input'; snapshot.mkdir()
        for name in c['files']:
            shutil.copyfile(ROOT/'eval'/c['id']/name,snapshot/name)
        shutil.copyfile(ROOT/'results'/c['id']/'reference.md',out/'reference.md')
        # Prepare host-side files inside the project; strict mode exposes only
        # the selected subdirectories through an allowlist mount namespace.
        with tempfile.TemporaryDirectory(prefix='case-',dir=workroot) as temp:
            base=Path(temp)
            work=base/'documents'; work.mkdir()
            runtime=base/'runtime'; runtime.mkdir(mode=0o700)
            delivery=base/'delivery'; delivery.mkdir()
            # Auth is only bootstrapped from the existing login, never logged or committed.
            # All child runtime writes remain under .work; temporary credential copy is removed.
            login=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'auth.json'
            if login.exists():
                shutil.copyfile(login,runtime/'auth.json')
                (runtime/'auth.json').chmod(0o600)
            env=os.environ.copy(); env['CODEX_HOME']=str(runtime)
            env['TMPDIR']=str(base)
            hashes={}
            for name in c['files']:
                source=snapshot/name
                shutil.copyfile(source,work/name)
                hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
            command=['codex','exec','--ignore-user-config','--ignore-rules','--ephemeral',
                     '--model',args.model,'--sandbox','read-only','--skip-git-repo-check',
                     '-c',f'model_reasoning_effort="{args.effort}"','--cd',str(work),'--json',
                     '--output-last-message',str(out/'answer.md'),'-']
            isolation_checks=None
            preflight_error=None
            if args.isolation=='strict':
                from isolation import prefix, probe
                try:
                    wrapper=prefix(work,runtime,delivery)
                    isolation_checks=probe(wrapper,ROOT,c['files'])
                    command[command.index('--cd')+1]='/case'
                    command[command.index('--output-last-message')+1]='/output/answer.md'
                    command=wrapper+command
                except (OSError,RuntimeError,subprocess.SubprocessError) as error:
                    preflight_error=str(error)
            start=time.monotonic()
            print(f'START {c["id"]} {args.model}',flush=True)
            with (out/'events.jsonl').open('w') as stdout, (out/'stderr.log').open('w') as stderr:
                try:
                    if preflight_error:
                        raise RuntimeError('Isolation preflight failed: '+preflight_error)
                    proc=subprocess.run(command,input=prompt,text=True,stdout=stdout,stderr=stderr,timeout=args.timeout,env=env)
                    if args.isolation=='strict' and (delivery/'answer.md').exists():
                        shutil.copyfile(delivery/'answer.md',out/'answer.md')
                    status='completed' if proc.returncode==0 and (out/'answer.md').exists() and (out/'answer.md').stat().st_size else 'error'
                    code=proc.returncode
                except (OSError,RuntimeError) as error:
                    status='error'; code=None
                    stderr.write(str(error)+'\n')
                except subprocess.TimeoutExpired:
                    status='timeout'; code=None
                except KeyboardInterrupt:
                    status='interrupted'; code=None
            receipt=dict(case=c['id'],model_requested=args.model,reasoning_effort=args.effort,status=status,exit_code=code,
                         duration_seconds=round(time.monotonic()-start,2),input_sha256=hashes,command=command,
                         isolation=('Bubblewrap allowlist filesystem; host project and user home not mounted; read-only case at /case.' if args.isolation=='strict' else 'Fresh case-only working directory; read-only Codex sandbox. Not OS-level read confinement.'),
                         isolation_mode=args.isolation,isolation_checks=isolation_checks,
                         cli_version=cli_version,source_sha256=source_sha256,
                         timestamp_utc=datetime.now(timezone.utc).isoformat())
            (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
            print(f'END {c["id"]}: {status} ({receipt["duration_seconds"]}s)',flush=True)
            # Stop on infrastructure failure rather than misclassifying it as an adversarial win.
            if status!='completed':
                print((out/'stderr.log').read_text()[-3000:],flush=True)
                raise SystemExit(1)

if __name__=='__main__': main()
