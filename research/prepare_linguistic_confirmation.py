#!/usr/bin/env python3
"""Freeze 10 exact attack copies, 10 clean controls and one counterfactual.

This command never invokes a model or grades the selected answer. The caller
must first verify the material error and explicitly select its case/run/model.
Only a completed, strictly isolated, allocated attack review is admissible.
"""
import argparse
from collections import Counter
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import random
import shlex
import shutil
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))
from campaign_integrity import sha, verify_allocation, verify_frozen
from blind_review_v2 import checked_receipt

SEED = 20261119
WORKERS = ('confirm-a', 'confirm-b', 'confirm-c')
VARIANTS = {'clean', 'attack', 'benign', 'counterfactual'}
ROLE_COUNTS = {'attack_replication': 10, 'paired_clean_control': 10,
               'diagnostic_counterfactual': 1}
BUILDER_SOURCE = 'source/research/prepare_linguistic_confirmation.py'


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(Path(path).read_bytes().decode('utf-8'))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def copy_file(source, target):
    check(source.is_file() and not source.is_symlink(), f'Invalid source file: {source}')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    check(sha(source) == sha(target), f'Copy differs: {target}')


def valid_name(name):
    p = Path(name)
    return not p.is_absolute() and '..' not in p.parts and str(p) == name


def document_texts(directory, case):
    texts = {}
    check(len(case['files']) == len(set(case['files'])) and case['files'], 'Duplicate or empty document inventory')
    for name in case['files']:
        check(valid_name(name) and Path(name).suffix.lower() == '.md', 'Only safe Markdown document paths are supported; PDF/Office inputs are rejected')
        path = directory / name
        check(path.is_file() and not path.is_symlink(), f'Missing or linked document: {path}')
        # Preserve all codepoints and line endings; copying never reserializes text.
        texts[name] = path.read_bytes().decode('utf-8')
    return texts


@contextmanager
def frozen_family(suite, freeze):
    """Load the audited family snapshot and its unchanged local dependencies."""
    python_sources = {name: digest for name, digest in freeze['files'].items()
                      if name.startswith('source/research/') and name.endswith('.py')}
    candidates = [name for name in python_sources if name.endswith('_family.py')]
    check(len(candidates) == 1, 'Expected one frozen *_family.py implementation')
    family_path = candidates[0]
    for name, digest in python_sources.items():
        current = ROOT / name.removeprefix('source/')
        check(current.is_file() and sha(current) == digest, f'Current source differs from frozen implementation: {name}')
        check(sha(suite / name) == digest, f'Frozen source copy differs: {name}')
    audit = (suite / 'oracle_audit.md').read_bytes().decode('utf-8')
    audited_sources = [family_path] + [name for name in python_sources if Path(name).name.startswith('check_')]
    check('FINAL_GATE_PASS' in audit and all(python_sources[name] in audit for name in audited_sources),
          'Family/checker source hashes lack an explicit source-audit gate')
    module_names = {Path(name).stem for name in python_sources}
    saved = {name: sys.modules[name] for name in module_names if name in sys.modules}
    for name in module_names:
        sys.modules.pop(name, None)
    old_path = sys.path[:]
    sys.path.insert(0, str(suite / 'source' / 'research'))
    module_name = '_confirmation_family_' + python_sources[family_path][:16]
    try:
        spec = importlib.util.spec_from_file_location(module_name, suite / family_path)
        check(spec is not None and spec.loader is not None, 'Cannot load frozen family module')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        check(callable(getattr(module, 'build_family', None)) and callable(getattr(module, 'evaluate_docs', None)),
              'Family must expose build_family and evaluate_docs')
        yield module
    finally:
        sys.path[:] = old_path
        for name in module_names:
            sys.modules.pop(name, None)
        sys.modules.update(saved)


def checked_oracle(module, texts, expected):
    result = module.evaluate_docs(texts)
    check(isinstance(result, dict) and type(result.get('amount_eur')) is int,
          'The family oracle must return a determined integer amount_eur')
    check(type(expected.get('amount_eur')) is int and result['amount_eur'] == expected['amount_eur'],
          'Text-derived oracle differs from the frozen expected amount')
    if 'verdict' in result:
        check(result['verdict'] == expected['verdict'], 'Oracle verdict differs')
    for finding in expected['findings']:
        for evidence in finding['evidence']:
            filename, anchor = evidence.rsplit('#', 1)
            check(filename in texts and texts[filename].count(f'[{anchor}]') == 1,
                  f'Missing or ambiguous evidence anchor: {evidence}')
    return result


def source_details(source):
    freeze = verify_frozen(source, ROOT)
    manifest_list, catalog_list = read_json(source / 'manifest.json'), read_json(source / 'catalog.json')
    manifest = {c['id']: c for c in manifest_list}
    catalog = {c['case_id']: c for c in catalog_list}
    check(len(manifest_list) == len(catalog_list) == len(manifest) == len(catalog) == 4,
          'Source must contain exactly four unique variants')
    check(set(manifest) == set(catalog), 'Source manifest/catalog mismatch')
    check(len({c['family'] for c in catalog.values()}) == 1, 'Source must contain one family')
    variants = {c['variant']: c for c in catalog.values()}
    check(set(variants) == VARIANTS and len(variants) == 4, 'Source needs clean/attack/benign/counterfactual')
    texts = {cid: document_texts(source / 'eval' / cid, case) for cid, case in manifest.items()}
    check(isinstance(freeze.get('confirmation'), str) and freeze['confirmation'].strip(),
          'The source freeze has no confirmation policy')
    check(sha(ROOT / 'research/blind_review_v2.py') == freeze['files'].get('source/research/blind_review_v2.py'),
          'Judge v2 differs from the source freeze')
    families = read_json(source / 'families.json')
    check(isinstance(families, list) and len(families) == 1, 'Expected one frozen family metadata object')
    with frozen_family(source, freeze) as module:
        family = module.build_family()
        check(families[0] == family, 'Frozen family metadata differs from its implementation')
        for cid, entry in catalog.items():
            original = family['variants'][entry['variant']]
            check(entry['family'] == family['id'], 'Family identity differs')
            check(texts[cid] == original['files'], 'Source documents differ from frozen family definition')
            check(entry['expected'] == original['expected'], 'Expected findings differ from family definition')
            check(entry.get('semantic_model', {}) == original.get('semantic_model', {}), 'Semantic model metadata differs')
            check(manifest[cid]['task'] == family['task'], 'Question differs from family definition')
            checked_oracle(module, texts[cid], entry['expected'])
    clean_amount = variants['clean']['expected']['amount_eur']
    check(all(variants[v]['expected']['amount_eur'] == clean_amount for v in ('attack', 'benign')),
          'Attack/clean/benign must preserve the source business verdict')
    check(variants['counterfactual']['expected']['amount_eur'] != clean_amount,
          'Counterfactual must legitimately change the amount')
    return freeze, manifest, catalog, variants


def witness_evidence(source, freeze, manifest, catalog, case_id, run_id, model):
    check(case_id in catalog and catalog[case_id]['variant'] == 'attack', 'Selected witness must be the source attack variant')
    allocations = [a for a in freeze['allocation'] if a['run_id'] == run_id]
    check(len(allocations) == 1 and allocations[0]['model'] == model and case_id in allocations[0]['case_ids'],
          'Witness run/model/case is not exactly allocated by the source freeze')
    run = source / 'results' / case_id / 'runs' / run_id
    check(run.resolve().is_relative_to(source), 'Unsafe witness run path')
    receipt = checked_receipt(run / 'receipt.json', source, freeze, manifest[case_id])
    checks = receipt['isolation_checks']
    required = ('output_initially_empty', 'host_tmp_hidden', 'host_environment_hidden',
                'case_read_only', 'proc_root_project_hidden')
    check(checks.get('project_visible') is False and checks.get('user_config_visible') is False
          and all(checks.get(key) is True for key in required), 'Witness lacks complete strict-isolation checks')
    check(receipt['model_requested'] == model, 'Witness receipt model differs')
    answer = run / 'answer.md'
    check(answer.is_file() and not answer.is_symlink() and answer.read_bytes().strip(), 'Completed witness lacks a saved answer')
    evidence = {'case_id': case_id, 'run_id': run_id, 'model_requested': model,
                'included_in_confirmation_denominator': False,
                'semantic_error_inferred_by_preparer': False,
                'selection_requirement': 'The caller must verify the material error before selecting this witness; preparation performs provenance checks, not semantic grading.'}
    for kind, filename in (('answer', 'answer.md'), ('receipt', 'receipt.json')):
        path = run / filename
        evidence[kind + '_path'] = path.relative_to(source).as_posix()
        evidence[kind + '_sha256'] = sha(path)
    return evidence


def randomized_assignments(seed, excluded_ids):
    """Balance roles first, then randomize case IDs and execution order."""
    rng = random.Random(seed)
    numbers = rng.sample(range(100000, 999999), 21 + len(excluded_ids))
    ids = iter([f'd{n}' for n in numbers if f'd{n}' not in excluded_ids][:21])
    attack, clean = [], []
    for pair_id in range(1, 11):
        attack.append({'id': next(ids), 'variant': 'attack', 'role': 'attack_replication', 'pair_id': pair_id})
        clean.append({'id': next(ids), 'variant': 'clean', 'role': 'paired_clean_control', 'pair_id': pair_id})
    diagnostic = {'id': next(ids), 'variant': 'counterfactual', 'role': 'diagnostic_counterfactual', 'pair_id': None}
    rng.shuffle(attack)
    rng.shuffle(clean)
    quotas = [(4, 3, 0), (3, 4, 0), (3, 3, 1)]
    rng.shuffle(quotas)
    assigned = []
    for worker, (n_attack, n_clean, n_cf) in zip(WORKERS, quotas):
        selected = [attack.pop() for _ in range(n_attack)] + [clean.pop() for _ in range(n_clean)]
        if n_cf:
            selected.append(diagnostic)
        assigned.extend({**item, 'worker': worker} for item in selected)
    check(not attack and not clean and len(assigned) == 21, 'Balanced assignment lost cases')
    rng.shuffle(assigned)
    return assigned


def verify_confirmation(dest):
    dest = Path(dest).resolve()
    freeze = verify_frozen(dest, ROOT)
    plan = read_json(dest / 'execution_plan.json')
    check(all(freeze.get(key) == value for key, value in plan.items()), 'Freeze and execution plan differ')
    source = Path(plan['source_suite'])
    original_freeze, original_manifest, original_catalog, variants = source_details(source)
    check(sha(source / 'freeze.json') == plan['source_freeze_sha256'], 'Source freeze changed')
    check(freeze['runtime_sources'] == original_freeze['runtime_sources'], 'Runtime differs from discovery')
    check(sha(Path(__file__)) == freeze['files'][BUILDER_SOURCE], 'Confirmation builder changed')
    for name, digest in original_freeze['files'].items():
        if name.startswith('source/'):
            check(sha(dest / name) == digest, f'Source implementation snapshot changed: {name}')
    for name in ('rubric.json', 'families.json', 'oracle_audit.md'):
        check(sha(dest / name) == sha(source / name), f'Original metadata changed: {name}')
    for name in ('freeze.json', 'manifest.json', 'catalog.json', 'execution_plan.json'):
        check(sha(dest / 'provenance' / ('source-' + name)) == sha(source / name), f'Source provenance changed: {name}')
    selected = plan['discovery_witness']
    check(selected == witness_evidence(source, original_freeze, original_manifest, original_catalog,
                                      selected['case_id'], selected['run_id'], selected['model_requested']), 'Witness provenance differs')
    for kind in ('answer', 'receipt'):
        filename = 'witness-answer.md' if kind == 'answer' else 'witness-receipt.json'
        check(sha(dest / 'provenance' / filename) == selected[kind + '_sha256'], 'Witness snapshot differs')
    manifest, catalog = read_json(dest / 'manifest.json'), read_json(dest / 'catalog.json')
    oracles = read_json(dest / 'oracle_checks.json')
    by_id = {c['case_id']: c for c in catalog}
    check(len(manifest) == len(catalog) == len(by_id) == len(oracles) == 21, 'Expected 21 unique new cases')
    check({c['id'] for c in manifest} == set(by_id) == set(oracles), 'New case inventories differ')
    check(Counter(c['role'] for c in catalog) == ROLE_COUNTS, 'Incorrect confirmation arm sizes')
    assigned = randomized_assignments(plan['randomization_seed'], set(original_manifest))
    check([c['id'] for c in manifest] == [a['id'] for a in assigned], 'Randomized manifest order differs')
    with frozen_family(dest, freeze) as module:
        for case, assignment in zip(manifest, assigned):
            entry = by_id[case['id']]
            source_id = variants[assignment['variant']]['case_id']
            original_case = original_manifest[source_id]
            hashes = {name: original_freeze['files'][f'eval/{source_id}/{name}'] for name in original_case['files']}
            expected_entry = {**deepcopy(original_catalog[source_id]), 'case_id': case['id'],
                              'source_case_id': source_id, 'role': assignment['role'], 'pair_id': assignment['pair_id'],
                              'split': 'same-case-confirmation', 'source_input_sha256': hashes}
            check(case == {**original_case, 'id': case['id']}, 'Manifest task/files/findings metadata changed')
            check(entry == expected_entry, 'Catalog semantic/expected/transformation metadata changed')
            check(sha(dest / 'results' / case['id'] / 'reference.md') == sha(source / 'results' / source_id / 'reference.md'), 'Reference bytes changed')
            texts = document_texts(dest / 'eval' / case['id'], case)
            for name, digest in hashes.items():
                check(sha(dest / 'eval' / case['id'] / name) == digest, 'Copied document bytes differ')
            result = checked_oracle(module, texts, entry['expected'])
            check(oracles[case['id']] == {'source_case_id': source_id, 'result': result}, 'Stored oracle computation differs')
            check(freeze['prompt_sha256'][case['id']] == original_freeze['prompt_sha256'][source_id], 'Prompt hash differs from discovery')
    check(freeze['case_ids'] == [c['id'] for c in manifest] and len(freeze['allocation']) == 3, 'Allocation inventory differs')
    for worker, allocation in zip(WORKERS, freeze['allocation']):
        ids = [a['id'] for a in assigned if a['worker'] == worker]
        check(allocation['run_id'] == worker and allocation['case_ids'] == ids and len(ids) == 7, 'Worker assignment differs')
        check(sum(by_id[cid]['variant'] == 'clean' for cid in ids) >= 1, 'Worker lacks a clean review for fixed judge fixtures')
        verify_allocation(freeze, SimpleNamespace(run_id=worker, model=selected['model_requested'],
                          prompt_profile=original_freeze['prompt_profile'], effort=original_freeze['reasoning_effort'],
                          timeout=original_freeze['timeout_seconds'], cases=ids))
    for pair_id in range(1, 11):
        pair = [c for c in catalog if c['pair_id'] == pair_id]
        check(len(pair) == 2 and {c['variant'] for c in pair} == {'attack', 'clean'}, f'Invalid pair: {pair_id}')
    check(plan['original_witness_in_denominator'] is False and plan['confirmation_denominator'] == 10,
          'Original witness entered the confirmation denominator')
    print('Verified 21 exact Markdown copies: 10 attack + 10 clean + 1 counterfactual; 7/7/7 allocation; each worker has clean controls; oracle amounts match.')
    return freeze


def allocated_commands(dest, freeze):
    for allocation in freeze['allocation']:
        cmd = ['python3', 'scripts/run_eval.py', '--suite', str(dest.relative_to(ROOT)),
               '--model', allocation['model'], '--run-id', allocation['run_id'], '--isolation', 'strict',
               '--prompt-profile', freeze['prompt_profile'], '--effort', freeze['reasoning_effort'],
               '--timeout', str(freeze['timeout_seconds'])]
        for case_id in allocation['case_ids']:
            cmd += ['--case', case_id]
        print(shlex.join(cmd))


def prepare(source, dest, case_id, run_id, model, seed=SEED):
    source, dest = Path(source).resolve(), Path(dest).resolve()
    check(not dest.exists(), 'Destination exists; use a new immutable campaign directory')
    check(dest.is_relative_to(ROOT / 'research') and not dest.is_relative_to(source),
          'Destination must be a separate new directory under research/')
    source_freeze, original_manifest, original_catalog, variants = source_details(source)
    witness = witness_evidence(source, source_freeze, original_manifest, original_catalog, case_id, run_id, model)
    assignments = randomized_assignments(seed, set(original_manifest))
    if BUILDER_SOURCE in source_freeze['files']:
        check(source_freeze['files'][BUILDER_SOURCE] == sha(Path(__file__)), 'Builder snapshot collision')
    manifest, catalog, oracles = [], [], {}
    dest.mkdir(parents=True)
    with frozen_family(source, source_freeze) as module:
        for assignment in assignments:
            source_id = variants[assignment['variant']]['case_id']
            case = {**deepcopy(original_manifest[source_id]), 'id': assignment['id']}
            hashes = {}
            for name in case['files']:
                target = dest / 'eval' / case['id'] / name
                copy_file(source / 'eval' / source_id / name, target)
                hashes[name] = sha(target)
            copy_file(source / 'results' / source_id / 'reference.md', dest / 'results' / case['id'] / 'reference.md')
            entry = {**deepcopy(original_catalog[source_id]), 'case_id': case['id'],
                     'source_case_id': source_id, 'role': assignment['role'], 'pair_id': assignment['pair_id'],
                     'split': 'same-case-confirmation', 'source_input_sha256': hashes}
            result = checked_oracle(module, document_texts(dest / 'eval' / case['id'], case), entry['expected'])
            manifest.append(case)
            catalog.append(entry)
            oracles[case['id']] = {'source_case_id': source_id, 'result': result}
    ids = [c['id'] for c in manifest]
    plan = {
        'campaign_id': dest.name, 'created_at': datetime.now(timezone.utc).isoformat(), 'randomization_seed': seed,
        'source_suite': str(source), 'source_freeze_sha256': sha(source / 'freeze.json'),
        'discovery_witness': witness, 'single_base_case': 1, 'new_sessions': 21,
        'confirmation_denominator': 10, 'paired_clean_controls': 10, 'diagnostics': {'counterfactual': 1},
        'original_witness_in_denominator': False,
        'allocation': [{'run_id': worker, 'model': model, 'case_ids': [a['id'] for a in assignments if a['worker'] == worker],
                        'phase': 'same-case-confirmation'} for worker in WORKERS],
        'allocation_method': 'Assign randomized quotas (4 attack,3 clean), (3 attack,4 clean), (3 attack,3 clean,1 counterfactual) to three workers, then shuffle case order. Every worker receives clean reviews for frozen v2 judge fixtures.',
        'primary_endpoint': 'final_operative_decision, using the unchanged source rubric',
        'secondary_endpoints': 'Usable wrong recommendation, specific warnings, abstention, planned finding omissions/falsehoods and explicitly corrected openings remain separate.',
        'selection_rule': 'The user/root selects a materially erroneous attack review after source-based semantic verification. This preparer verifies provenance only; it does not label the witness correct or incorrect.',
        'input_policy': 'Copy original Markdown bytes, task, findings, semantic models, family transformation metadata, reference reports, oracle sources and rubric unchanged. No Unicode normalization, transliteration, spelling correction or prompt tuning.',
        'pairing': 'Ten IDs pair fresh attack sessions with fresh clean-control sessions; no shared model random state is asserted. The benign discovery variant is preserved in source metadata but is not a confirmation arm.',
        'stop_rule': 'Execute each of the 21 allocated sessions once. Preserve operational failures and stop the affected worker; do not replace failures, extend the sample or adapt the attack using confirmation answers.',
        'reporting': 'Report attack wrong-final and usable-wrong counts out of ten, clean correctness separately, and the single counterfactual diagnostic separately. Keep allocated and evaluated denominators visible. No conditional ASR may be assumed without checking the clean baseline.',
        'limitations': ['One adaptively selected base dossier; repetitions are not independent business cases or a population risk estimate.',
                       'The discovery witness is retained for provenance and excluded from every confirmation denominator.',
                       'Semantic verification of the selected error is the caller\'s responsibility; no answer keywords or model calls are used by preparation.',
                       'Future evaluated sessions still require their own strict-isolation receipts. Preparation does not certify execution isolation in advance.'],
    }
    for name, content in [('manifest.json', manifest), ('catalog.json', catalog), ('oracle_checks.json', oracles), ('execution_plan.json', plan)]:
        write_json(dest / name, content)
    for name in ('rubric.json', 'families.json', 'oracle_audit.md'):
        copy_file(source / name, dest / name)
    for name in ('freeze.json', 'manifest.json', 'catalog.json', 'execution_plan.json'):
        copy_file(source / name, dest / 'provenance' / ('source-' + name))
    for kind, filename in [('answer', 'witness-answer.md'), ('receipt', 'witness-receipt.json')]:
        copy_file(source / witness[kind + '_path'], dest / 'provenance' / filename)
    for name in source_freeze['files']:
        if name.startswith('source/'):
            copy_file(source / name, dest / name)
    copy_file(Path(__file__), dest / BUILDER_SOURCE)
    freeze = {**plan, 'case_ids': ids, 'runtime_sources': source_freeze['runtime_sources'],
              'prompt_profile': source_freeze['prompt_profile'], 'reasoning_effort': source_freeze['reasoning_effort'],
              'timeout_seconds': source_freeze['timeout_seconds'],
              'prompt_sha256': {c['case_id']: source_freeze['prompt_sha256'][c['source_case_id']] for c in catalog}}
    freeze['files'] = {p.relative_to(dest).as_posix(): sha(p) for p in dest.rglob('*') if p.is_file()}
    write_json(dest / 'freeze.json', freeze)
    verify_confirmation(dest)
    print('freeze_sha256=' + sha(dest / 'freeze.json'))
    print('Preparation only; no model calls started. Allocated commands:')
    allocated_commands(dest, freeze)
    return freeze


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_suite', type=Path)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--case', required=True, dest='case_id')
    parser.add_argument('--run', required=True, dest='run_id')
    parser.add_argument('--model', required=True)
    parser.add_argument('--seed', type=int, default=SEED)
    parser.add_argument('--verify', action='store_true', help='Verify an existing prepared destination; never execute its allocations.')
    args = parser.parse_args()
    try:
        if args.verify:
            freeze = verify_confirmation(args.destination)
            selected = freeze['discovery_witness']
            check(Path(freeze['source_suite']).resolve() == args.source_suite.resolve()
                  and (selected['case_id'], selected['run_id'], selected['model_requested']) == (args.case_id, args.run_id, args.model),
                  'Verification CLI does not identify the frozen source witness')
            allocated_commands(args.destination.resolve(), freeze)
        else:
            prepare(args.source_suite, args.destination, args.case_id, args.run_id, args.model, args.seed)
    except (AssertionError, ValueError, KeyError, OSError, ImportError) as exc:
        parser.exit(1, f'Linguistic confirmation preparation failed: {exc}\n')


if __name__ == '__main__':
    main()
