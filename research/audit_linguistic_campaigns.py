#!/usr/bin/env python3
"""Audit the linguistic reviews without rewriting the earlier phase audit."""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from build_pilot_report import ROOT, read_json, run_record, sha

sys.path.insert(0, str(ROOT / 'scripts'))
from campaign_integrity import verify_frozen


def main():
    business = ['litera-v1', 'rovina-v1', 'doria-v1']
    judges = [f'{key}-judging-{model}' for key in ('litera', 'rovina', 'doria')
              for model in ('terra', 'sol', 'sol6', 'luna', 'astra')
              if (ROOT / 'research' / f'{key}-judging-{model}' / 'freeze.json').exists()]
    records, pending = [], []
    for name in business + judges:
        suite = ROOT / 'research' / name
        freeze = verify_frozen(suite, ROOT)
        digest = sha(suite / 'freeze.json')
        cases = ({c['case_id']: c for c in read_json(suite / 'catalog.json')}
                 if (suite / 'catalog.json').exists() else
                 {c['id']: dict(c, case_id=c['id']) for c in read_json(suite / 'manifest.json')})
        for allocation in freeze['allocation']:
            for cid in allocation['case_ids']:
                record = run_record(suite, freeze, digest, cases[cid], allocation, [])
                if record['status'] == 'planned':
                    assert allocation['phase'] == 'conditional_transfer_after_verified_material_failure', (name, allocation['run_id'], cid)
                    pending.append({'suite': name, 'case_id': cid, 'run_id': allocation['run_id'],
                                    'reason': 'Conditional transfer not launched; no verified material discovery witness.'})
                    continue
                assert record['valid'], (name, cid, record['status'], record['errors'])
                events = [json.loads(line) for line in (record['dir'] / 'events.jsonl').read_text().splitlines()]
                tids = [event['thread_id'] for event in events if event.get('type') == 'thread.started']
                assert len(tids) == 1, (name, cid, 'Expected one fresh session')
                receipt = record['receipt']
                records.append({'suite': name, 'role': 'business_review' if name in business else 'anonymous_judging',
                                'case_id': cid, 'run_id': allocation['run_id'], 'thread_id': tids[0],
                                'model_requested': receipt['model_requested'], 'cli_version': receipt['cli_version'],
                                'receipt_sha256': sha(record['dir'] / 'receipt.json'), 'answer_sha256': sha(record['dir'] / 'answer.md'),
                                'freeze_sha256': digest, 'strict_read_and_environment_isolation': True,
                                'inputs_and_prompt_match_frozen_allocation': True})
    prior = read_json(ROOT / 'research/phase2_integrity_audit.json')
    assert prior['status'] == 'passed'
    tids = [r['thread_id'] for r in records + prior['records']]
    assert len(tids) == len(set(tids)), 'Session reuse across or within phases'
    work = ROOT / '.work'
    assert not work.exists() or not list(work.iterdir()), 'Private runtime cleanup incomplete'
    output = {'created_at': datetime.now(timezone.utc).isoformat(), 'status': 'passed',
              'script_sha256': sha(Path(__file__)), 'completed_sessions': len(records),
              'roles': dict(Counter(r['role'] for r in records)),
              'cli_versions': dict(Counter(r['cli_version'] for r in records)),
              'prior_audit_sha256': sha(ROOT / 'research/phase2_integrity_audit.json'),
              'unique_threads_across_phases': len(tids), 'unlaunched_allocations': pending,
              'private_runtime_directories_remaining': 0, 'records': records,
              'limitations': ['Technical integrity only; semantic judgments are separate.',
                             'Variants are not independent dossiers. Requested backend identity is not independently attested.',
                             'Read isolation is not complete network isolation.']}
    path = ROOT / 'research/linguistic_integrity_audit.json'
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ('status', 'completed_sessions', 'roles', 'unique_threads_across_phases')}))


if __name__ == '__main__':
    main()
