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
PROJECT=ROOT
PROMPT='''Fă un review independent al dosarului de documente din directorul curent. Verifică afirmațiile și deciziile propuse folosind numai faptele și regulile din dosar. Nu ai acces la un raport de referință.
Întrebarea beneficiarului: {task}
Citește toate documentele din dosar, inclusiv subdirectoarele și fișierele PDF. Lucrează numai pe acest dosar, fără alte directoare sau internet.
Identifică toate problemele materiale, contradicțiile, erorile și sursele de confuzie; nu presupune un număr fix de findinguri. Findingurile suplimentare sunt binevenite dacă pot fi demonstrate din documente. Pentru fiecare concluzie oferă probe cu numele fișierului și eticheta pasajului și o scurtă deducție. Distinge faptele certe de necunoscute. Include și aspecte corecte și un rezumat final coerent cu analiza. Răspunde în română, în Markdown, fără să modifici fișierele.
'''

STANDARD_PROMPT='''Analizează dosarul din directorul curent și pregătește un raport pentru beneficiar.
{task}
Citește documentele disponibile, inclusiv anexele. Semnalează problemele materiale și motivează concluziile cu probe din documente.
Răspunde în română, în Markdown. Lucrează numai pe acest dosar, fără internet și fără să modifici fișierele.
'''

def main():
    global ROOT
    ap=argparse.ArgumentParser()
    ap.add_argument('--suite',type=Path,help='Frozen experimental suite; requires freeze.json and strict isolation.')
    ap.add_argument('--model',default='gpt-6.1-terra')
    ap.add_argument('--prompt-profile',choices=['forensic','standard'],default='forensic')
    ap.add_argument('--isolation',choices=['strict','context'],default='strict')
    ap.add_argument('--effort',choices=['low','medium','high','xhigh'],default='medium')
    ap.add_argument('--case',action='append',dest='cases')
    ap.add_argument('--run-id',default=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    ap.add_argument('--timeout',type=int,default=600)
    args=ap.parse_args()
    freeze_digest=None
    if args.suite:
        from campaign_integrity import verify_frozen, verify_allocation
        ROOT=args.suite.resolve()
        if args.isolation!='strict': ap.error('Experimental campaigns require strict read isolation')
        freeze=verify_frozen(ROOT,PROJECT)
        verify_allocation(freeze,args)
        freeze_digest=hashlib.sha256((ROOT/'freeze.json').read_bytes()).hexdigest()
    cli_version=subprocess.run(['codex','--version'],capture_output=True,text=True,check=True).stdout.strip()
    source_sha256={name:hashlib.sha256((PROJECT/'scripts'/name).read_bytes()).hexdigest()
                   for name in ['run_eval.py','isolation.py','cases.py',*sorted(p.name for p in (PROJECT/'scripts').glob('case_*.py')),*sorted(p.name for p in (PROJECT/'scripts').glob('*policy*.json')),'policy_candidates.json']}
    workroot=PROJECT/'.work'
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
        if args.suite:
            verify_frozen(ROOT,PROJECT)
            assert hashlib.sha256((ROOT/'freeze.json').read_bytes()).hexdigest()==freeze_digest
        out=ROOT/'results'/c['id']/'runs'/args.run_id
        out.mkdir(parents=True,exist_ok=False)
        shutil.copyfile(ROOT/'manifest.json',out/'manifest.json')
        prompt=(STANDARD_PROMPT if args.prompt_profile=='standard' else PROMPT).format(task=c['task'])
        (out/'prompt.md').write_text(prompt)
        snapshot=out/'input'; snapshot.mkdir()
        for name in c['files']:
            source=ROOT/'eval'/c['id']/name
            if source.is_symlink() or not source.resolve().is_relative_to((ROOT/'eval'/c['id']).resolve()):
                raise RuntimeError('Case inputs must be regular files inside the case')
            (snapshot/name).parent.mkdir(parents=True,exist_ok=True)
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
                (work/name).parent.mkdir(parents=True,exist_ok=True)
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
                    isolation_checks=probe(wrapper,PROJECT,c['files'])
                    command[command.index('--cd')+1]='/case'
                    command[command.index('--output-last-message')+1]='/output/answer.md'
                    command=wrapper+command
                except (OSError,RuntimeError,subprocess.SubprocessError) as error:
                    preflight_error=str(error)
            start=time.monotonic()
            started_at=datetime.now(timezone.utc).isoformat()
            (out/'started.json').write_text(json.dumps(dict(case=c['id'],model_requested=args.model,started_at=started_at,freeze_sha256=freeze_digest)))
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
            inputs_unchanged=all(hashlib.sha256((snapshot/n).read_bytes()).hexdigest()==h and hashlib.sha256((work/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
            if not inputs_unchanged: status='input_changed'
            freeze_unchanged=None
            if args.suite:
                try:
                    verify_frozen(ROOT,PROJECT)
                    assert hashlib.sha256((ROOT/'freeze.json').read_bytes()).hexdigest()==freeze_digest
                    assert hashes=={n:freeze['files']['eval/'+c['id']+'/'+n] for n in c['files']}
                    freeze_unchanged=True
                except (AssertionError,OSError,ValueError):
                    freeze_unchanged=False; status='freeze_changed'
            usage=[]
            for line in (out/'events.jsonl').read_text().splitlines():
                try: event=json.loads(line)
                except json.JSONDecodeError: continue
                if event.get('type')=='turn.completed': usage.append(event.get('usage',{}))
            receipt=dict(case=c['id'],model_requested=args.model,reasoning_effort=args.effort,status=status,exit_code=code,
                         started_at=started_at,freeze_sha256=freeze_digest,freeze_unchanged=freeze_unchanged,inputs_unchanged=inputs_unchanged,usage=usage,
                         prompt_profile=args.prompt_profile,prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(),
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
