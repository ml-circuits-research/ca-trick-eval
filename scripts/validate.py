#!/usr/bin/env python3
"""Check corpus/reference integrity without calling a model."""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    assert len(manifest)==10
    assert len({c['id'] for c in manifest})==10
    tags=set(); findings=0
    for c in manifest:
        folder=ROOT/'eval'/c['id']
        assert set(p.name for p in folder.iterdir())==set(c['files'])
        assert 2 <= len(c['files']) <= 3
        assert (ROOT/'results'/c['id']/'reference.md').exists()
        for f in c['findings']:
            findings+=1; tags.update(f['tags'])
            assert f['claim'] and f['proof'] and f['evidence']
            for ref in f['evidence']:
                name,anchor=ref.split('#')
                assert name in c['files']
                assert len(re.findall(re.escape('['+anchor+']'),(folder/name).read_text()))==1,ref
        for receipt in (ROOT/'results'/c['id']).glob('runs/*/receipt.json'):
            data=json.loads(receipt.read_text())
            for name,digest in data['input_sha256'].items():
                snapshot=receipt.parent/'input'/name
                assert hashlib.sha256((snapshot if snapshot.exists() else folder/name).read_bytes()).hexdigest()==digest
    expected={m for m in re.findall(r'\| (T\d+) \|',(ROOT/'TAXONOMY.md').read_text())}
    assert tags<=expected
    print(f'OK: 10 cases, 30 documents, {findings} findings, {len(tags)}/{len(expected)} taxonomy categories covered, valid evidence anchors and run input hashes.')
if __name__=='__main__': main()
