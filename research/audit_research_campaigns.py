#!/usr/bin/env python3
"""Audit completed research receipts and frozen inputs; no semantic scoring."""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from build_pilot_report import ROOT, read_json, run_record, sha

sys.path.insert(0, str(ROOT / 'scripts'))
from campaign_integrity import verify_frozen

BUSINESS = ['pilot-v1', 'orizont-confirm-v1', 'dorna-pdf-v1', 'dorna-confirm-v1', 'atria-v1']
JUDGING = ['pilot-judging'] + ['confirm-judging-' + x for x in 'abc'] + [
    'dorna-judging-' + x for x in ('terra', 'sol', 'luna')] + [
    'dorna-confirm-judging-all', 'dorna-confirm-judging-b'] + [
    'atria-judging-' + x for x in ('terra', 'sol', 'luna')]


def main():
    records, threads, pending, errors = [], [], [], []
    for suite_name in BUSINESS + JUDGING:
        suite = ROOT / 'research' / suite_name
        freeze = verify_frozen(suite, ROOT)
        digest = sha(suite / 'freeze.json')
        if (suite / 'catalog.json').exists():
            cases = {c['case_id']: c for c in read_json(suite / 'catalog.json')}
        else:
            cases = {c['id']: dict(c, case_id=c['id']) for c in read_json(suite / 'manifest.json')}
        for allocation in freeze['allocation']:
            for case_id in allocation['case_ids']:
                record = run_record(suite, freeze, digest, cases[case_id], allocation, [])
                if record['status'] == 'planned' and suite_name == 'pilot-v1' and allocation['run_id'] == 'pilot-luna':
                    pending.append({'suite': suite_name, 'run_id': allocation['run_id'], 'case_id': case_id,
                                    'reason': 'Conditional discovery branch not launched; recorded in phase-one report.'})
                    continue
                assert record['valid'], (suite_name, case_id, allocation['run_id'], record['errors'], record['status'])
                events = [json.loads(line) for line in (record['dir'] / 'events.jsonl').read_text().splitlines()]
                ids = [event['thread_id'] for event in events if event.get('type') == 'thread.started']
                assert len(ids) == 1, (suite_name, case_id, 'Expected exactly one fresh thread')
                threads.extend(ids)
                item_types = Counter(event.get('item', {}).get('type') for event in events if event.get('type') == 'item.completed')
                receipt = record['receipt']
                records.append({'suite': suite_name, 'role': 'business_review' if suite_name in BUSINESS else 'anonymous_judging',
                                'case_id': case_id, 'run_id': allocation['run_id'],
                                'model_requested': receipt['model_requested'], 'cli_version': receipt['cli_version'],
                                'thread_id': ids[0], 'receipt_sha256': sha(record['dir'] / 'receipt.json'),
                                'answer_sha256': sha(record['dir'] / 'answer.md'), 'freeze_sha256': digest,
                                'strict_read_and_environment_isolation': True,
                                'inputs_and_prompt_match_frozen_allocation': True,
                                'completed_item_types': dict(item_types)})
    assert len(threads) == len(set(threads)), 'Session reuse detected'
    work = ROOT / '.work'
    work_count = len(list(work.iterdir())) if work.exists() else 0
    assert work_count == 0, 'Private runtime cleanup is incomplete'
    output = {
        'created_at': datetime.now(timezone.utc).isoformat(), 'status': 'passed',
        'script_sha256': sha(Path(__file__)), 'completed_sessions': len(records),
        'unique_threads': len(set(threads)), 'roles': dict(Counter(r['role'] for r in records)),
        'cli_versions': dict(Counter(r['cli_version'] for r in records)),
        'unlaunched_allocations': pending, 'private_runtime_directories_remaining': work_count,
        'limitations': ['Technical integrity only; semantic judgments are separate.',
                       'Repeated inputs are not independent business dossiers.',
                       'Requested model ID and CLI version are recorded; backend identity is not independently attested.',
                       'This does not certify complete network isolation or prove the internal use of pixels.'],
        'records': records,
    }
    path = ROOT / 'research/phase2_integrity_audit.json'
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ('status', 'completed_sessions', 'unique_threads', 'roles', 'cli_versions')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
