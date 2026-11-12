#!/usr/bin/env python3
"""Validate evidence references, snapshot integrity and authored/generated consistency."""
import ast
import base64
import hashlib
import json
import re
import subprocess
from pathlib import Path
from cases import build
ROOT=Path(__file__).resolve().parents[1]

def inspect_adapter(folder):
    source=(folder/'AGENTS.md').read_text().split("python3 - <<'PYCODE'\n")[1].split('\nPYCODE')[0]
    tree=ast.parse(source)
    expected=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='expected')
    encoded=next(ast.literal_eval(n.args[0]) for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='b64decode')
    assert set(expected)=={p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}-{'AGENTS.md'}
    assert expected=={name:hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in expected}
    assert json.loads(base64.b64decode(encoded))['check_result']=='PASS'

def main():
    authored={c['id']:c for c in build()}
    manifest=json.loads((ROOT/'manifest.json').read_text())
    assert {c['id'] for c in manifest}==set(authored)
    assert {p.name for p in (ROOT/'eval').iterdir()}==set(authored)
    count=0
    for c in manifest:
        folder=ROOT/'eval'/c['id']
        assert set(c['files'])=={p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
        assert len({f['id'] for f in c['findings']})==len(c['findings'])
        assert c['findings']==authored[c['id']]['findings']
        for name,body in authored[c['id']]['documents'].items(): assert (folder/name).read_bytes()==(body if isinstance(body,bytes) else body.encode('utf-8'))
        for f in c['findings']:
            count+=1
            for ref in f['evidence']:
                name,anchor=ref.split('#')
                assert name in c['files']
                text=(subprocess.check_output(['pdftotext',str(folder/name),'-'],text=True) if name.endswith('.pdf') else (folder/name).read_text())
                assert len(re.findall(re.escape('['+anchor+']'),text))==1,ref
        assert (ROOT/'results'/c['id']/'reference.md').exists()
        if (folder/'AGENTS.md').exists(): inspect_adapter(folder)
        for receipt in (ROOT/'results'/c['id']).glob('runs/*/receipt.json'):
            r=json.loads(receipt.read_text())
            assert set(r['input_sha256'])=={p.relative_to(receipt.parent/'input').as_posix() for p in (receipt.parent/'input').rglob('*') if p.is_file()}
            for name,digest in r['input_sha256'].items():
                assert hashlib.sha256((receipt.parent/'input'/name).read_bytes()).hexdigest()==digest
            if r.get('isolation_mode')=='strict' and r.get('isolation_checks'):
                checks=r['isolation_checks']
                assert checks['project_visible'] is False and checks['user_config_visible'] is False
                assert checks['output_initially_empty'] is True and checks['host_tmp_hidden'] is True
                assert checks['case_files']==sorted(r['input_sha256'])
                command=r['command']
                assert command[0]=='bwrap' and '--unshare-pid' in command
                assert command[command.index('--cd')+1]=='/case'
                assert command[command.index('--output-last-message')+1]=='/output/answer.md'
    print(f'OK: {len(manifest)} dossiers; {count} planned findings; evidence anchors, generated sources, adapter fingerprints and run snapshots checked.')
if __name__=='__main__': main()
