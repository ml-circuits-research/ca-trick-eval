#!/usr/bin/env python3
"""Render one linguistic campaign; classification comes only from validated scores."""
import argparse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from build_pilot_report import ROOT, STYLE, e, link, read_json, sha, freeze_errors, run_record, load_judgments
from build_pdf_report import EXTRA_STYLE, eligible_judge_dirs, final_score, load_author_review, author_review_section
from build_interval_report import cell


def build(args):
    suite, output = args.suite.resolve(), args.output.resolve()
    freeze, catalog = read_json(suite / 'freeze.json'), read_json(suite / 'catalog.json')
    family = read_json(suite / 'families.json')[0]
    digest = sha(suite / 'freeze.json')
    errors = freeze_errors(suite, freeze)
    records = [run_record(suite, freeze, digest, case, allocation, errors)
               for allocation in freeze['allocation'] for case in catalog if case['case_id'] in allocation['case_ids']]
    directories = args.judging_dir or [ROOT / 'research' / f'{args.key}-judging-{n}' for n in ('terra', 'sol', 'luna', 'astra')]
    accepted, issues, _ = eligible_judge_dirs(directories, digest)
    _, more = load_judgments(accepted, records, digest)
    issues += more
    reviewed, more = load_author_review(suite, digest, records)
    issues += more
    scores = [s for r in records if (s := final_score(r)) is not None]
    counts = Counter(s['classification'] for s in scores)
    done = sum(r['valid'] for r in records)
    rows = ['<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
            '<title>' + e(family['title']) + '</title><style>' + STYLE + EXTRA_STYLE + '</style><main>',
            '<nav>' + link(ROOT / 'docs/index.html', 'Matricea caz × model', output) + ' · '
            + link(ROOT / 'docs/research-plan.html', 'Metodă', output) + '</nav>',
            '<p class="eyebrow">Perturbare lingvistică · o familie de dosare</p>',
            '<h1>' + e(family['title']) + '</h1><p>' + e(family.get('human_explanation', family['mechanism'])) + '</p>',
            '<p class="muted">' + e(datetime.now(timezone.utc).isoformat()) + ' · standard · medium · timeout 600 s.</p>',
            f'<p><b>{done} rulări finalizate valid; {len(scores)} evaluate; {counts["wrong_business_decision"]} verdicte finale greșite; '
            f'{counts["abstention"]} abțineri.</b> Sunt alocate 12 sesiuni de descoperire și patru sesiuni Astra condiționate de un eșec verificat. '
            'O celulă nerulată sau neevaluată nu este un succes.</p>']
    for error in errors + issues:
        rows.append('<p class="bad">' + e(error) + '</p>')
    rows.append('<h2>Variantă × model</h2><div class="table-wrap"><table class="matrix"><thead><tr><th>Variantă și etalon</th>')
    for a in freeze['allocation']:
        rows.append('<th>' + e(a['model']) + '</th>')
    rows.append('</tr></thead><tbody>')
    for variant in ('clean', 'attack', 'benign', 'counterfactual'):
        case = next(c for c in catalog if c['variant'] == variant)
        rows.append('<tr><th>' + e(variant) + '<small>' + e(case['case_id']) + '</small><small>Etalon: '
                    + e(case['expected']['amount_eur']) + ' EUR</small>' + link(suite / 'results' / case['case_id'] / 'reference.md', 'Etalon și probe', output) + '</th>')
        for a in freeze['allocation']:
            rows.append(cell(next(r for r in records if r['case']['case_id'] == case['case_id'] and r['allocation'] == a), output))
        rows.append('</tr>')
    rows.append('</tbody></table></div><h2>Ce schimbă experimentul</h2>')
    for label, explanation in family.get('pairing', {}).items():
        rows.append('<p><b>' + e(label) + ':</b> ' + e(explanation) + '</p>')
    rows.append('<p>' + e(family['oracle_description']) + '</p>')
    if 'novelty_limit' in family:
        rows.append('<p>' + e(family['novelty_limit']) + '</p>')
    if 'claim_scope' in family:
        for explanation in family['claim_scope'].values():
            rows.append('<p>' + e(explanation) + '</p>')
    rows.append(author_review_section(suite, records, reviewed, output))
    rows.append('<h2>Fișiere, izolare și reproducere</h2><p>' + ' · '.join(link(suite / name, label, output) for name, label in [
        ('freeze.json', 'Freeze'), ('execution_plan.json', 'Alocare înainte de test'), ('oracle_audit.md', 'Audit separat al etalonului'),
        ('families.json', 'Toate variantele'), ('source/scripts/run_eval.py', 'Cod runner'), ('source/scripts/isolation.py', 'Izolare la citire')]) + '</p>')
    rows.append('<p>Modelele evaluate văd numai propriul dosar. Etalonul, variantele vecine și proiectul nu sunt montate în filesystemul lor. '
                'Autorii și auditorii au acces la proiect; nu sunt agenții evaluați. Fiecare receipt păstrează preflightul, hashurile, versiunea CLI și modelul cerut. '
                'Nu presupunem atestarea independentă a backendului sau izolarea completă a rețelei.</p>'
                '<p>Un singur dosar selectat pentru descoperire; nu este o estimare a riscului în producție. '
                'O observație materială este urmată de confirmare separată, fără modificarea intrărilor. '
                'Erorile de prezentare corectate explicit sunt secundare și separate de verdictul final.</p></main></html>')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(rows))
    print(f'{output}: {done} valid, {len(scores)} graded, {len(issues)} judging issues.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('key', choices=['litera', 'rovina'])
    p.add_argument('--suite', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--judging-dir', type=Path, action='append')
    args = p.parse_args()
    args.suite = args.suite or ROOT / 'research' / f'{args.key}-v1'
    args.output = args.output or ROOT / 'docs' / f'{args.key}-report.html'
    build(args)
