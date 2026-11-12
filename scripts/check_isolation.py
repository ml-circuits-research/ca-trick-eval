#!/usr/bin/env python3
"""Offline checks of actual filesystem confinement, without an agent or credentials."""
import json
import os
import subprocess
import tempfile
from pathlib import Path
from isolation import prefix,probe
ROOT=Path(__file__).resolve().parents[1]

def main():
    workroot=ROOT/'.work'; workroot.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='isolation-check-',dir=workroot) as temp:
        base=Path(temp)
        case=base/'documents'; case.mkdir()
        runtime=base/'runtime'; runtime.mkdir()
        delivery=base/'delivery'; delivery.mkdir()
        (case/'evidence.md').write_text('Public case evidence.\n')
        secret=base/'reference-must-not-be-visible.txt'; secret.write_text('HIDDEN_REFERENCE_CANARY')
        command=prefix(case,runtime,delivery)
        os.environ['CA_EVAL_SYNTHETIC_CONTEXT_CANARY']='must-not-reach-child'
        try:
            checks=probe(command,ROOT,['evidence.md'])
        finally:
            del os.environ['CA_EVAL_SYNTHETIC_CONTEXT_CANARY']
        code='''from pathlib import Path
import errno
import sys
assert Path('/case/evidence.md').read_text() == 'Public case evidence.\\n'
for source in sys.argv[1:]:
    assert not Path(source).exists(), source
    assert not (Path('/proc/self/root')/source.lstrip('/')).exists(), source
try:
    Path('/case/evidence.md').write_text('overwrite')
except OSError as error:
    assert error.errno in (errno.EROFS,errno.EACCES,errno.EPERM)
else:
    raise AssertionError('case is writable')
Path('/output/answer.md').write_text('Review output only.')
'''
        hidden=[str(ROOT),str(ROOT/'manifest.json'),str(ROOT/'results'),str(secret)]
        subprocess.run(command+['python3','-c',code,*hidden],check=True)
        assert (delivery/'answer.md').read_text()=='Review output only.'
        assert (case/'evidence.md').read_text()=='Public case evidence.\n'
        print('OK: project, manifest, results and sibling canary invisible, including through /proc/self/root; case read-only; answer delivery works.')
        print(json.dumps(checks))
if __name__=='__main__': main()
