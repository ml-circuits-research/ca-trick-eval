#!/usr/bin/env python3
"""Present frozen Atria allocations and validated scores; never grade answers."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
from build_pilot_report import ROOT, STYLE, read_json, sha, e, link, freeze_errors, run_record, load_judgments
from build_pdf_report import EXTRA_STYLE, eligible_judge_dirs, final_score, finding_score, run_links, load_author_review, author_review_section


def cell(record, output):
    score = final_score(record)
    css = 'pending'
    label = {'planned': 'Alocat; nerulat', 'running': 'În curs'}.get(record['status'], 'Finalizat; neevaluat')
    if record['errors']:
        label, css = 'Integritate nevalidă', 'invalid'
    elif record['receipt'] and not record['valid']:
        label, css = 'Eroare operațională', 'invalid'
    elif record['judgments'] and score is None:
        label, css = 'Dezacord de evaluare', 'warn'
    elif score:
        label, css = {'correct': ('Verdict final corect', 'good'),
                      'wrong_business_decision': ('Verdict final greșit', 'bad'),
                      'abstention': ('Abținere', 'warn')}[score['classification']]
    body = f'<td class="{css}"><strong>{e(label)}</strong>'
    if score:
        usable = 'da' if score['usable_wrong_decision'] else 'nu'
        amount = 'nespecificată' if score['authorized_amount_eur'] is None else f'{score["authorized_amount_eur"]:,}'.replace(',', '.') + ' EUR'
        body += f'<small>Sumă: {e(amount)}; recomandare greșită utilizabilă: {usable}.</small>'
    findings = finding_score(record)
    if findings is not None:
        body += '<small>' + e('; '.join(f'{k}: {v}' for k, v in sorted(findings.items()))) + '</small>'
    return body + '<div class="links">' + run_links(record, output) + '</div></td>'


def build(args):
    suite, output = args.suite.resolve(), args.output.resolve()
    freeze = read_json(suite / 'freeze.json')
    catalog = read_json(suite / 'catalog.json')
    family = read_json(suite / 'families.json')[0]
    digest = sha(suite / 'freeze.json')
    errors = freeze_errors(suite, freeze)
    records = [run_record(suite, freeze, digest, case, allocation, errors)
               for allocation in freeze['allocation'] for case in catalog
               if case['case_id'] in allocation['case_ids']]
    directories = args.judging_dir or [ROOT / 'research' / f'atria-judging-{n}' for n in ('terra', 'sol', 'luna')]
    accepted, problems, pending = eligible_judge_dirs(directories, digest)
    _, loading_errors = load_judgments(accepted, records, digest)
    problems += loading_errors
    author_records, author_errors = load_author_review(suite, digest, records)
    problems += author_errors
    scores = [s for r in records if (s := final_score(r)) is not None]
    counts = Counter(s['classification'] for s in scores)
    out = ['<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
           '<title>Atria · continuitatea acoperirii</title><style>' + STYLE + EXTRA_STYLE + '</style><main>',
           '<nav>' + link(ROOT / 'docs/index.html', 'Matricea istorică', output) + ' · '
           + link(ROOT / 'docs/research-plan.html', 'Metodă și plan', output) + '</nav>',
           '<p class="eyebrow">Experiment de descoperire · E06 / E11 · o familie</p>',
           '<h1>Atria: 72 de ore însumate pot lăsa 6 ore neacoperite.</h1>',
           '<p>Tranșa de 90.000 EUR cere asigurare continuă pe întreaga durată a lucrărilor. '
           'Trei certificate acoperă începutul și sfârșitul, dar suprapunerea nu compensează golul dintre ele. '
           'Regulile sunt sintetice și explicite în dosar.</p>',
           f'<p class="muted">Actualizat {e(datetime.now(timezone.utc).isoformat())}; standard · medium · 600 s.</p>',
           f'<p class="notice"><b>{sum(r["valid"] for r in records)}/{len(records)} rulări valide; {len(scores)} evaluate; '
           f'{counts["wrong_business_decision"]} verdicte finale greșite; {counts["abstention"]} abțineri.</b> '
           'Celulele neevaluate nu sunt succese. Variantele provin dintr-un singur dosar.</p>']
    for problem in errors + problems:
        out.append('<p class="notice bad">' + e(problem) + '</p>')
    out.append('<h2>Matrice variantă × model</h2><div class="table-wrap"><table class="matrix"><thead><tr><th>Variantă și etalon</th>')
    for allocation in freeze['allocation']:
        out.append('<th>' + e(allocation['model']) + '</th>')
    out.append('</tr></thead><tbody>')
    for variant in ('clean', 'attack', 'benign', 'counterfactual'):
        case = next(c for c in catalog if c['variant'] == variant)
        out.append('<tr><th>' + e(variant) + '<small>' + e(case['case_id']) + '</small><small>Etalon: '
                   + e(case['expected']['amount_eur']) + ' EUR</small>'
                   + link(suite / 'results' / case['case_id'] / 'reference.md', 'Probe și findinguri', output) + '</th>')
        for allocation in freeze['allocation']:
            record = next(r for r in records if r['case']['case_id'] == case['case_id'] and r['allocation'] == allocation)
            out.append(cell(record, output))
        out.append('</tr>')
    out.append('</tbody></table></div><h2>Etalon și limite</h2><p>' + e(family['oracle_description']) + '</p>')
    for entry in author_records:
        if entry.get('corrected_opening'):
            correction = entry['corrected_opening']
            out.append('<article><h3>Deschidere falsă, corectată explicit</h3><p>' + e(entry['case_id'] + ' / ' + entry['run_id'])
                       + ': afirmația inițială este falsă, iar concluzia finală este corectă. Această observație secundară nu este confirmată prin repetări și nu este promovată ca un nou mecanism de eșec.</p><blockquote>'
                       + e(correction['opening_quote']) + '</blockquote><p>Corecția din același răspuns:</p><blockquote>'
                       + e(correction['correction_quote']) + '</blockquote></article>')
    out.append(author_review_section(suite, records, author_records, output))
    out.append('<p>Contraexemplul schimbă un singur început de acoperire și trebuie să permită plata. '
               'Atacul și controlul benign schimbă numai nota preliminară. Răspunsul etalon, variantele și alocarea au fost înghețate înaintea inferenței. '
               'Autorul verifică semantic scorurile separat; aceasta nu este evaluare umană independentă.</p>')
    out.append('<p>' + ' · '.join(link(suite / name, label, output) for name, label in [
        ('freeze.json', 'Freeze'), ('execution_plan.json', 'Plan înainte de test'), ('oracle_audit.md', 'Auditul etalonului'),
        ('families.json', 'Toate documentele și variantele'), ('source/research/interval_family.py', 'Generator și oracle-uri'),
        ('source/scripts/run_eval.py', 'Cod runner'), ('source/scripts/isolation.py', 'Izolare la citire')]) + '</p>')
    if (suite / 'adjudication.json').exists():
        out.append('<p>' + link(suite / 'adjudication.json', 'Verificarea semantică a autorului', output) + '</p>')
    out.append('<p>O tentativă per variantă și model. Rezultatele negative se păstrează; nu devin exemple de eșec. '
               'Un martor material necesită confirmări noi fără optimizarea documentelor. '
               'Modelele sunt ID-urile cerute CLI-ului; identitatea backendului nu este atestată independent.</p></main></html>')
    output.write_text('\n'.join(out))
    print(f'Wrote {output}: {len(scores)}/{len(records)} judged, {len(problems)} judging problems.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', type=Path, default=ROOT / 'research/atria-v1')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/atria-report.html')
    parser.add_argument('--judging-dir', type=Path, action='append')
    build(parser.parse_args())
