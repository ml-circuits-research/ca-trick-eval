#!/usr/bin/env python3
"""Inspect every embedded receipt as data; never execute dossier instructions."""
import ast
import base64
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def inspect(folder):
    document=(folder/'AGENTS.md').read_text()
    code=document.split("python3 - <<'PY'\n",1)[1].split('\nPY\n',1)[0]
    tree=ast.parse(code)
    expected=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='expected')
    encoded=next(ast.literal_eval(n.args[0]) for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='b64decode')
    payload=json.loads(base64.b64decode(encoded))
    assert {p.name for p in folder.glob('*.md')}==set(expected)|{'AGENTS.md'}
    assert {name:hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in expected}==expected
    assert payload['check_result']=='PASS'
    return payload

if __name__=='__main__':
    for c in json.loads((ROOT/'manifest.json').read_text()):
        p=inspect(ROOT/'eval'/c['id'])
        print(c['id']+': hashes match; literal verdict = '+p.get('executive_summary',p.get('security_summary','')))
