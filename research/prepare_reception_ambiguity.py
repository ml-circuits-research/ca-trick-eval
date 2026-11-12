#!/usr/bin/env python3
"""Freeze an audited ambiguity dossier and its grading protocol before inference."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from campaign_integrity import sha, verify_frozen
from run_eval import STANDARD_PROMPT
import reception_ambiguity_family as source
import blind_ambiguity_review as judge


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def prepare(dest):
    family = source.build_family()
    solved = source.validate_family()
    names = ['research/reception_ambiguity_family.py', 'research/check_reception_ambiguity_oracle.py']
    audit = ROOT / 'research/reception_ambiguity_oracle_audit.md'
    assert audit.is_file() and 'FINAL_GATE_PASS' in audit.read_text(), 'Independent prose audit required'
    assert all(sha(ROOT / n) in audit.read_text() for n in names), 'Exact source hashes must be audited'
    dest = dest.resolve()
    assert dest.is_relative_to(ROOT / 'research') and not dest.exists(), 'Fresh research destination required'
    rng = random.Random(20261119)
    manifest, catalog = [], []
    for number, variant in zip(rng.sample(range(100000, 999999), 4), source.VARIANTS):
        item = family['variants'][variant]
        case_id = f'd{number}'
        for name, body in item['files'].items():
            p = Path(name)
            assert p.suffix == '.md' and not p.is_absolute() and '..' not in p.parts and p.name != 'AGENTS.md'
            target = dest / 'eval' / case_id / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding='utf-8')
        manifest.append({'id': case_id, 'title': family['title'], 'task': family['task'],
                         'files': sorted(item['files']), 'findings': item['expected']['findings'],
                         'profile': 'paired contractual ambiguity', 'primary_mechanism': family['mechanism']})
        catalog.append({'case_id': case_id, 'family': family['id'], 'variant': variant,
                        'split': 'discovery', 'expected': item['expected'], 'oracle': solved[variant]})
        target = dest / 'results' / case_id / 'reference.md'
        target.parent.mkdir(parents=True)
        target.write_text('# Etalon fixat înaintea inferenței\n\n' + json.dumps(
            {'expected': item['expected'], 'oracle': solved[variant]}, ensure_ascii=False, indent=2) + '\n')
    rng.shuffle(manifest)
    ids = [m['id'] for m in manifest]
    models = [('terra', 'gpt-6.1-terra'), ('sol', 'gpt-6.1-sol'), ('sol6', 'gpt-6-sol'),
              ('luna', 'gpt-6-luna'), ('astra', 'gpt-6-astra')]
    allocation = [{'run_id': 'ambiguity-' + name, 'model': model, 'case_ids': ids,
                   'phase': 'conditional_transfer_after_verified_material_failure' if name == 'astra' else 'discovery'}
                  for name, model in models]
    for name, data in [('manifest.json', manifest), ('catalog.json', catalog), ('families.json', [family])]:
        write_json(dest / name, data)
    (dest / 'rubric.md').write_text(judge.RUBRIC)
    shutil.copyfile(audit, dest / 'oracle_audit.md')
    plan = {
        'campaign_id': dest.name, 'created_at': datetime.now(timezone.utc).isoformat(),
        'case_ids': ids, 'allocation': allocation, 'prompt_profile': 'standard',
        'reasoning_effort': 'medium', 'timeout_seconds': 600,
        'prompt_sha256': {m['id']: hashlib.sha256(STANDARD_PROMPT.format(task=m['task']).encode()).hexdigest() for m in manifest},
        'independent_families': 1, 'discovery_sessions': 16, 'conditional_transfer_sessions': 4,
        'adaptive_attempts_in_this_campaign': 1, 'adaptive_budget_max_per_base_case': 20,
        'primary': 'Unsupported contractual certainty on an underdetermined dossier, or misinterpretation of a determinate control. Operational hold pending precise clarification is correct.',
        'secondary': 'Explicitly corrected openings, omitted conditional branches and supplemental errors are scored separately; they do not automatically change the final verdict class.',
        'lexical_comparison': 'ambiguous_clean versus ambiguous_wording changes one true administrative word. Shared errors do not establish a causal effect of that word.',
        'stop': 'Run the sixteen allocated discovery reviews once; preserve negatives. Stop a worker on technical error. Never edit source inputs after any output.',
        'transfer': 'Run four Astra cells only after semantic audit confirms a material unsupported-certainty or misinterpretation witness, or a distinct decisive material error.',
        'confirmation': 'Select a verified material witness with preference Terra, Sol 6.1, Sol 6, Luna. Freeze ten exact copies of its observed variant, ten copies of its paired alternative wording, and one of each determined control. Exclude discovery from confirmation denominators. Use a new campaign; no tuning against confirmation outputs.',
        'judging': 'Frozen contractual_ambiguity_v1 adapter; anonymous model reports plus six fixed judge audit responses. Semantic adjudication is separate; LLM agreement is not independent human validation.',
        'scope': 'C0 Codex CLI document review, no business skill. Synthetic explicit local contract rules; no outside legal presumption.',
        'limits': ['One selected base dossier, correlated variants and repetitions.',
                   'Author and prose-audit agents have repository access; evaluated review sessions do not.',
                   'Actual filesystem and environment isolation; network access needed for the backend.',
                   'Requested model ID, without independent backend attestation.',
                   'Unknown contractual meaning is not a known-false amount.'],
    }
    write_json(dest / 'execution_plan.json', plan)
    runtime = ['scripts/run_eval.py', 'scripts/isolation.py', 'scripts/campaign_integrity.py']
    for name in runtime + names + ['research/prepare_reception_ambiguity.py', *judge.DEPENDENCIES]:
        target = dest / 'source' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    plan['runtime_sources'] = {name: sha(ROOT / name) for name in runtime}
    plan['files'] = {p.relative_to(dest).as_posix(): sha(p) for p in dest.rglob('*') if p.is_file()}
    write_json(dest / 'freeze.json', plan)
    verify_frozen(dest, ROOT)
    print(f'Frozen Doria: 16 discovery + 4 conditional Astra; SHA256 {sha(dest / "freeze.json")}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    prepare(parser.parse_args().destination)
