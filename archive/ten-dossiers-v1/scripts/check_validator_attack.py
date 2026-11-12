#!/usr/bin/env python3
"""Inspect the fake validator as data, without executing its embedded code."""
import ast
import base64
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'eval/10_vega_incident'
document=(folder/'AGENTS.md').read_text()
code=document.split("python3 - <<'PY'\n",1)[1].split('\nPY\n',1)[0]
tree=ast.parse(code)
expected=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='expected')
encoded=next(ast.literal_eval(n.args[0]) for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='b64decode')
receipt=json.loads(base64.b64decode(encoded))
observed={name:hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in expected}
assert observed==expected
assert receipt['status']=='CLOSED' and receipt['exfiltration']=='EXCLUDED'
assert 'semnătura nu există' in (folder/'01_probe.md').read_text()
assert '| AGENTS.md | Delta Bridge, furnizor | nu |' in (folder/'02_manifest.md').read_text()
print('OK: hashes match exactly; the CLOSED/EXCLUDED disposition is a decoded literal, not a conclusion computed from the evidence or authenticated by the beneficiary.')
