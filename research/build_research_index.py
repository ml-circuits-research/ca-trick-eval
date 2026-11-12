#!/usr/bin/env python3
"""Update only the marked research matrix, preserving the historical index."""
import argparse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from build_pilot_report import (
    ROOT, consensus_records, e, freeze_errors, link, load_adjudications,
    load_judgments, read_json, run_record, sha,
)
from build_pdf_report import MODELS, eligible_judge_dirs, load_author_review

START = '<!-- RESEARCH-MATRIX:START -->'
END = '<!-- RESEARCH-MATRIX:END -->'
HISTORICAL_HEADING = '<h2>Matrice caz × model</h2>'


def campaign(suite, judging_dirs, version=2):
    if not (suite / 'freeze.json').exists() or not (suite / 'catalog.json').exists():
        return {'records': [], 'resolved': [], 'errors': [], 'present': False, 'version': version}
    try:
        freeze, catalog = read_json(suite / 'freeze.json'), read_json(suite / 'catalog.json')
        digest = sha(suite / 'freeze.json')
        errors = freeze_errors(suite, freeze)
        by_id = {c['case_id']: c for c in catalog}
        records = [run_record(suite, freeze, digest, by_id[cid], a, errors)
                   for a in freeze['allocation'] for cid in a['case_ids']]
        eligible, judge_errors, _ = eligible_judge_dirs(judging_dirs, digest, rubric_version=version)
        _, loading_errors = load_judgments(eligible, records, digest)
        errors.extend(judge_errors + loading_errors)
        if version == 1:
            _, audit_errors = load_adjudications(suite, digest, records)
        else:
            _, audit_errors = load_author_review(suite, digest, records)
        errors.extend(audit_errors)
        return {'records': records, 'resolved': consensus_records(records), 'errors': errors,
                'present': True, 'version': version}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {'records': [], 'resolved': [], 'errors': [f'{suite.name}: {exc}'],
                'present': True, 'version': version}


def final_kind(score, version):
    """Version 1's broad error class needs an explicit final-decision subtype."""
    if score.get('subtype') == 'contradictory_report_corrected':
        return 'corrected_opening'
    if score.get('subtype') == 'wrong_final_decision':
        return 'wrong_final'
    if score['classification'] == 'correct':
        return 'correct'
    if score['classification'] == 'abstention':
        return 'abstention'
    return 'wrong_final' if version == 2 else 'unresolved_final'


def summary(data, model, family=None, role=None):
    def selected(record):
        return (record['allocation']['model'] == model
                and (family is None or record['case']['family'] == family)
                and (role is None or record['case'].get('role') == role))
    records = [r for r in data['records'] if selected(r)]
    scores = [x['score'] for x in data['resolved'] if selected(x['record'])]
    counts = Counter(final_kind(s, data['version']) for s in scores)
    secondary_corrections = sum(bool(x['record'].get('author_review', {}).get('corrected_opening'))
                                and final_kind(x['score'], data['version']) == 'correct'
                                for x in data['resolved'] if selected(x['record']))
    return {'allocated': len(records), 'valid': sum(r['valid'] for r in records),
            'planned': sum(r['status'] == 'planned' for r in records),
            'graded': len(scores), 'known_final': len(scores) - counts['unresolved_final'],
            'correct': counts['correct'] + counts['corrected_opening'],
            'wrong': counts['wrong_final'], 'corrected': counts['corrected_opening'] + secondary_corrections,
            'abstention': counts['abstention'], 'unresolved_final': counts['unresolved_final'],
            'finding_issues': sum(any(v in {'partial', 'miss', 'fail'} for v in s['findings'].values()) for s in scores),
            'cli_versions': sorted({r['receipt']['cli_version'] for r in records if r['valid']})}


def confirmation_subline(data, output):
    if not data['present']:
        return '<small>Confirmarea separată: încă nealocată.</small>'
    attack = summary(data, 'gpt-6-luna', role='attack_replication')
    control = summary(data, 'gpt-6-luna', role='paired_faithful_ocr_control')
    if not attack['graded'] and not control['graded']:
        content = 'Confirmare separată: în evaluare; 0/10 atacuri și 0/10 controale clasificate.'
    else:
        wrong = f'{attack["wrong"]}/10' if attack['graded'] else '—/10'
        correct = f'{control["correct"]}/10' if control['graded'] else '—/10'
        content = (f'Confirmare separată: atac greșit {wrong} ({attack["graded"]}/10 evaluate); '
                   f'OCR fidel corect {correct} ({control["graded"]}/10 evaluate).')
    return '<small class="confirmation">' + e(content) + ' ' + link(ROOT / 'docs' / 'dorna-confirmation.html', 'Detalii', output) + '</small>'


def model_cell(data, model, family, output, extra=''):
    stats = summary(data, model, family)
    if not data['present']:
        return '<td class="pending"><strong>În pregătire; neevaluat</strong><small>Fără campanie înghețată și scoruri validate.</small>' + extra + '</td>'
    if data['errors'] and not data['records']:
        return '<td class="pending"><strong>Date nevalide sau indisponibile</strong><small>Nicio concluzie de model; vezi erorile de validare.</small>' + extra + '</td>'
    if not stats['allocated']:
        return '<td class="pending"><strong>Nealocat</strong><small>Modelul nu are rulări alocate în această familie.</small>' + extra + '</td>'
    if not stats['graded']:
        label = 'Alocat; nerulat' if stats['planned'] == stats['allocated'] else 'Fără scoruri validate'
        return (f'<td class="pending"><strong>{label}</strong><small>0/{stats["allocated"]} evaluate; '
                f'{stats["valid"]}/{stats["allocated"]} finalizate valid.</small>' + extra + '</td>')
    style = ('bad' if stats['wrong'] else 'incomplete' if any(stats[k] for k in ('corrected', 'abstention', 'unresolved_final', 'finding_issues'))
             else 'good' if stats['graded'] == stats['allocated'] else 'pending')
    out = [f'<td class="{style}"><strong>Verdicte finale greșite: {stats["wrong"]}/{stats["known_final"]}</strong>',
           f'<small>{stats["graded"]}/{stats["allocated"]} evaluate · {stats["valid"]}/{stats["allocated"]} finalizate valid.</small>',
           f'<small>Final corect: {stats["correct"]}; abținere: {stats["abstention"]}.</small>',
           '<small>' + e(', '.join(stats['cli_versions'])) + '</small>']
    if stats['finding_issues']:
        out.append(f'<small>Rulări cu findinguri incomplete, omise sau false: {stats["finding_issues"]}/{stats["graded"]}.</small>')
    if stats['corrected']:
        out.append(f'<small>Deschidere greșită, corectată explicit: {stats["corrected"]}/{stats["graded"]}.</small>')
    if stats['unresolved_final']:
        out.append(f'<small>{stats["unresolved_final"]} clasificări vechi fără subtip final verificat; excluse din numitorul verdictului final.</small>')
    out.extend([extra, '</td>'])
    return ''.join(out)


def replace_fragment(original, fragment):
    if START in original or END in original:
        if original.count(START) != 1 or original.count(END) != 1:
            raise ValueError('Research matrix markers must occur exactly once.')
        before, remainder = original.split(START, 1)
        _, after = remainder.split(END, 1)
        return before + fragment + after
    if original.count(HISTORICAL_HEADING) != 1:
        raise ValueError('Could not locate exactly one historical matrix heading.')
    return original.replace(HISTORICAL_HEADING, fragment + HISTORICAL_HEADING, 1)


def build(args):
    output = args.output.resolve()
    if not output.exists():
        raise ValueError('The historical index must already exist; this builder only inserts its marked section.')
    pilot = campaign(ROOT / 'research' / 'pilot-v1', [ROOT / 'research' / 'pilot-judging'], version=1)
    dorna = campaign(ROOT / 'research' / 'dorna-pdf-v1', [ROOT / 'research' / f'dorna-judging-{x}' for x in ('terra', 'sol', 'luna')])
    atria = campaign(args.atria_suite.resolve(), [ROOT / 'research' / f'atria-judging-{x}' for x in ('terra', 'sol', 'luna')])
    confirmation_suite = ROOT / 'research' / 'dorna-confirm-v1'
    confirmation_judge = ROOT / 'research' / 'dorna-confirm-judging-all'
    confirmation = campaign(confirmation_suite, [confirmation_judge])
    note_path = confirmation_suite / 'judging_execution_note.json'
    if note_path.exists():
        note = read_json(note_path)
        if ((ROOT / note['primary_judge_suite']).resolve() != confirmation_judge.resolve()
                or sha(confirmation_judge / 'freeze.json') != note['primary_freeze_sha256']):
            confirmation['resolved'] = []
            confirmation['errors'].append('Judecarea primară a confirmării diferă de nota de execuție; metricile nu sunt afișate.')
    rows = [
        ('Orizont', 'Entitate, perioadă și unitate', pilot, 'r01_orizont_scope', 'pilot-report.html'),
        ('Meridian', 'Data aplicării unei derogări', pilot, 'r02_meridian_effective', 'pilot-report.html'),
        ('Vela', 'Proveniența pierdută în rezumate', pilot, 'vela', 'pilot-report.html'),
        ('Dorna PDF', 'Pagina vizibilă și stratul OCR fals', dorna, 'dorna_pdf', 'dorna-report.html'),
        ('Atria', 'Durată însumată versus acoperire continuă', atria, None, 'atria-report.html'),
    ]
    timestamp = datetime.now(timezone.utc).isoformat()
    fragment = [START, '<section id="research-current" aria-labelledby="research-heading">',
                '<style>#research-current small{display:block;margin-top:6px}#research-current td{vertical-align:top;min-width:220px;font-size:.88rem}'
                '#research-current th,#research-current td{vertical-align:top;padding:14px}#research-current .confirmation{border-top:1px solid #bbcdd7;padding-top:8px}'
                '#research-current .research-warning{background:#fff4ce;padding:14px 18px;border-left:4px solid #a76b0b}</style>',
                '<h2 id="research-heading">Cercetarea curentă: verdict final și probe</h2>',
                '<p>Fiecare rând reprezintă o familie investigată. Rezultatele negative și cele încă neevaluate rămân vizibile; '
                'rândurile nu reprezintă automat cazuri care păcălesc modelele. Fiecare familie de descoperire are patru variante perechi.</p>',
                f'<p class="meta">Actualizat {e(timestamp)} · Codex CLI · standard · medium · izolare strictă la citire verificată din receipts.</p>',
                '<div class="scroll"><table><thead><tr><th scope="col">Familie / raport</th>'
                + ''.join(f'<th scope="col">{label}<small><code>{model}</code></small></th>' for model, label in MODELS)
                + '</tr></thead><tbody>']
    for name, description, data, family, page in rows:
        page_path = ROOT / 'docs' / page
        title = link(page_path, name, output) if page_path.exists() else e(name)
        fragment.append(f'<tr><th scope="row">{title}<small>{e(description)}</small>')
        if name == 'Orizont' and (ROOT / 'docs' / 'confirmation-report.html').exists():
            fragment.append('<small>' + link(ROOT / 'docs' / 'confirmation-report.html', 'Confirmarea deschiderii corectate', output) + '</small>')
        fragment.append('</th>')
        for model, _ in MODELS:
            extra = confirmation_subline(confirmation, output) if name == 'Dorna PDF' and model == 'gpt-6-luna' else ''
            fragment.append(model_cell(data, model, family, output, extra))
        fragment.append('</tr>')
    fragment.append('</tbody></table></div><p><strong>Astra nu a fost rulat în aceste faze.</strong> Coloanele arată identificatorii ceruți, fără atestarea independentă a backendului. '
                    'Variantele și repetările aceluiași dosar nu sunt mecanisme independente. O deschidere greșită revocată explicit este separată de verdictul final greșit.</p>'
                    '<p>Scorurile sunt încărcate numai după validarea provenienței și a citatelor. Pentru pilot, subtipul din arbitrajul explicit validat separă contradicția corectată de decizia finală. '
                    'Pentru Dorna și Atria, rubrica v2 judecă decizia operativă finală. Confirmările Dorna au propriul numitor de 10 și folosesc numai judecarea primară a lotului complet; '
                    'nu se adună cu cele patru variante de descoperire. Scanul clean inițial nu a fost rezolvat de Luna, deci nu raportăm un ASR condiționat de succesul acestuia.</p>')
    problems = list(dict.fromkeys(problem for data in (pilot, dorna, atria, confirmation) for problem in data['errors']))
    if problems:
        fragment.append('<details class="research-warning"><summary>Intrări sau scoruri neaplicate</summary><ul>'
                        + ''.join(f'<li>{e(x)}</li>' for x in problems) + '</ul></details>')
    fragment.append('<p class="meta">Matricea istorică și versiunile anterioare ale configurațiilor sunt păstrate mai jos, cu metricile lor originale.</p></section>' + END)
    original = output.read_text()
    updated = replace_fragment(original, '\n'.join(fragment))
    output.write_text(updated)
    print(f'Updated marked research matrix in {output}; historical content preserved; {len(problems)} reported validation problems.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'docs' / 'index.html')
    parser.add_argument('--atria-suite', type=Path, default=ROOT / 'research' / 'atria-v1')
    build(parser.parse_args())


if __name__ == '__main__':
    main()
