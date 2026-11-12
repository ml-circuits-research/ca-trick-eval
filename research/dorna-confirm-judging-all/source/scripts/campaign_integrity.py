"""Fail-closed checks for preregistered, immutable experimental input packages."""
import hashlib
import json
from pathlib import Path

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify_frozen(suite, project):
    data=json.loads((suite/'freeze.json').read_text())
    for name,digest in data['files'].items():
        path=suite/name
        assert path.resolve().is_relative_to(suite), name
        assert not path.is_symlink(), name
        assert sha(path)==digest, f'Frozen input changed: {name}'
    for name,digest in data['runtime_sources'].items():
        assert sha(project/name)==digest, f'Frozen runtime changed: {name}'
    expected={n for n in data['files'] if n.startswith('eval/')}
    actual={p.relative_to(suite).as_posix() for p in (suite/'eval').rglob('*') if p.is_file()}
    assert actual==expected, 'Unexpected or missing case input'
    return data

def verify_allocation(freeze,args):
    matches=[x for x in freeze['allocation'] if x['run_id']==args.run_id]
    assert len(matches)==1, 'Run must be allocated before inference'
    run=matches[0]
    assert args.model==run['model'], 'Model differs from allocation'
    assert args.prompt_profile==freeze['prompt_profile'], 'Prompt profile differs'
    assert args.effort==freeze['reasoning_effort'], 'Effort differs'
    assert args.timeout==freeze['timeout_seconds'], 'Timeout differs'
    assert set(args.cases or freeze['case_ids'])==set(run['case_ids']), 'Case allocation differs'
