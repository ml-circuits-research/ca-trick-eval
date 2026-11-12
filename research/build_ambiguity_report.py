#!/usr/bin/env python3
"""Render Doria only from mechanically revalidated ambiguity judgments.

Judgments are recomputed in temporary copies, never by overwriting originals.
Host agreements bind exact answer/judgment hashes; no semantic keyword grading.
"""
import argparse
from collections import Counter
from contextlib import redirect_stdout
from datetime import datetime, timezone
import html
import io
import os
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory
from urllib.parse import quote as urlquote
sys.dont_write_bytecode = True
import blind_ambiguity_review as judge

ROOT = Path(__file__).resolve().parents[1]
check, read_json, write_json, sha = judge.check, judge.read_json, judge.write_json, judge.sha
MODELS = [('gpt-6.1-terra', 'Terra'), ('gpt-6.1-sol', 'Sol 6.1'), ('gpt-6-sol', 'Sol 6'), ('gpt-6-luna', 'Luna'), ('gpt-6-astra', 'Astra')]
VARIANTS = [('ambiguous_clean', 'Sens nedefinit'), ('ambiguous_wording', 'Sens nedefinit · formulare apropiată'),
            ('defined_receipt', 'Definiție: primire administrativă'), ('defined_acceptance', 'Definiție: acceptare tehnică')]
LABELS = {'correct': 'Corect', 'unsupported_certainty': 'Certitudine nesusținută',
          'misinterpretation': 'Interpretare greșită', 'abstention': 'Abținere'}
STYLE = '''body{font:16px/1.55 system-ui,sans-serif;color:#193246;background:#f4f7f9;margin:0}main{max-width:1450px;margin:auto;padding:28px}h1,h2{line-height:1.2}a{color:#075b91}table{border-collapse:collapse;width:100%;background:white}th,td{padding:14px;border:1px solid #cedae1;vertical-align:top;min-width:145px}th{background:#e8eff4;text-align:left}.scroll{overflow-x:auto}small{display:block;color:#526775;margin-top:5px}.correct{border-top:5px solid #278559}.unsupported_certainty{border-top:5px solid #b66b00}.misinterpretation{border-top:5px solid #bb3434}.abstention{border-top:5px solid #6b6a89}.pending{color:#526775}blockquote{margin:10px 0;padding:8px 12px;background:#f1f5f8;white-space:pre-wrap;font-size:14px}details{margin-top:10px}code{overflow-wrap:anywhere}.issue{padding:12px;border-left:4px solid #b66b00;background:#fff4db}.card{background:white;border:1px solid #cedae1;padding:18px;margin:20px 0}li{margin-bottom:9px}'''


def esc(value):
    return html.escape(str(value), quote=True)


def link(path, label, output):
    relative = os.path.relpath(Path(path).resolve(), output.parent.resolve())
    return f'<a href="{esc(urlquote(relative, safe="/"))}">{esc(label)}</a>'


def path_label(path):
    path = Path(path).resolve()
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)


def validated_judgment(directory, source, source_digest):
    """Validate an exact temporary copy; unchanged scores are the sole input."""
    directory = Path(directory).resolve()
    frozen = judge.base.verify_frozen(directory, ROOT)
    mapping = read_json(directory / 'mapping.json')
    check(Path(mapping['source_suite']).resolve() == source and mapping['source_freeze_sha256'] == source_digest,
          'Judging package belongs to a different source campaign')
    original = read_json(directory / 'scores.json'); original_digest = sha(directory / 'scores.json')
    with TemporaryDirectory(prefix='doria-report-validation-') as temp:
        target = Path(temp)
        for name in (*frozen['files'], 'freeze.json'):
            copied = target / name; copied.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(directory / name, copied)
        run_relative = Path('results/review_001/runs/judge1')
        run = target / run_relative; run.mkdir(parents=True, exist_ok=True)
        for name in ('receipt.json', 'answer.md', 'prompt.md'):
            shutil.copyfile(directory / run_relative / name, run / name)
        shutil.copytree(directory / run_relative / 'input', run / 'input')
        with redirect_stdout(io.StringIO()): judge.validate(target)
        check(read_json(target / 'scores.json') == original, 'Stored scores differ from the ambiguity validator output')
    check(sha(directory / 'scores.json') == original_digest, 'Judgment changed during report validation')
    check(original['status'] == 'machine_validated_not_adjudicated' and original['rubric_id'] == 'contractual_ambiguity_v1', 'Unexpected scoring schema')
    check(original['judge_audit']['passed'] == original['judge_audit']['required'] == 6, 'Six judge fixtures did not pass')
    return original, original_digest


def collect_scores(source, freeze, directories):
    scores, audits, issues, duplicates = {}, [], [], set()
    cases = {c['id']: c for c in read_json(source / 'manifest.json')}
    for directory in directories:
        directory = Path(directory).resolve()
        if not (directory / 'scores.json').exists():
            continue
        try:
            data, digest = validated_judgment(directory, source, sha(source / 'freeze.json'))
            accepted = {}
            for score in data['scores']:
                key = (score['case_id'], score['run_id'])
                case = cases[key[0]]
                receipt_path = source / score['source_receipt']
                receipt = judge.base.checked_receipt(receipt_path, source, freeze, case)
                check(receipt['model_requested'] == score['model_requested'], 'Score/model provenance mismatch')
                answer = source / score['source_answer']
                check(answer.is_file() and not answer.is_symlink() and sha(answer) == score['source_answer_sha256'], 'Source answer changed')
                accepted[key] = {**score, '_judgment_file': directory / 'scores.json', '_judgment_sha256': digest,
                                 '_answer_file': answer, '_receipt_file': receipt_path}
            for key, score in accepted.items():
                if key in scores or key in duplicates:
                    duplicates.add(key); scores.pop(key, None); issues.append(f'Două judecări pentru {key[0]}/{key[1]}; celula nu primește scor.')
                else: scores[key] = score
            audits.append({'directory': directory, 'digest': digest, 'fixture_count': 6, 'source_count': len(accepted)})
        except (ValueError, AssertionError, KeyError, OSError, TypeError) as error:
            issues.append(f'Scoruri excluse din {path_label(directory)}: {error}')
    return scores, audits, issues


def load_adjudication(path, source, scores):
    """Host semantic judgments are explicit records, not inferred from text."""
    if not path.exists():
        return {}, []
    data = read_json(path)
    check(data['schema_version'] == 1 and data['source_freeze_sha256'] == sha(source / 'freeze.json'), 'Adjudication belongs to another source freeze')
    check(isinstance(data['agreements'], list) and isinstance(data['verified_supplementary'], list), 'Invalid host adjudication lists')
    agreements = {}
    for entry in data['agreements']:
        required = {'case_id', 'run_id', 'source_answer_sha256', 'judgment_file', 'judgment_sha256', 'classification', 'quote'}
        check(isinstance(entry, dict) and set(entry) == required, 'Agreement schema differs')
        key = (entry['case_id'], entry['run_id']); check(key in scores and key not in agreements, 'Unscored or duplicate host agreement')
        score = scores[key]
        path_value = Path(entry['judgment_file']); path_value = path_value if path_value.is_absolute() else ROOT / path_value
        check(path_value.resolve() == score['_judgment_file'] and entry['judgment_sha256'] == score['_judgment_sha256'], 'Agreement judgment provenance differs')
        check(entry['source_answer_sha256'] == score['source_answer_sha256'], 'Agreement source answer hash differs')
        check(entry['classification'] == score['classification'], 'Host disagreement cannot be published as an agreement')
        judge.base.exact_quote(entry['quote'], score['_answer_file'].read_text(), 'host agreement')
        agreements[key] = entry
    supplementary = []
    for entry in data['verified_supplementary']:
        required = {'case_id', 'run_id', 'source_answer_sha256', 'claim', 'quote', 'reason', 'evidence'}
        check(isinstance(entry, dict) and set(entry) == required, 'Supplementary schema differs')
        key = (entry['case_id'], entry['run_id']); check(key in scores, 'Supplementary finding has no validated source score')
        score = scores[key]; check(entry['source_answer_sha256'] == score['source_answer_sha256'], 'Supplementary source hash differs')
        judge.base.nonempty_string(entry['claim'], 'host supplementary claim'); judge.base.nonempty_string(entry['reason'], 'host supplementary reason')
        judge.base.exact_quote(entry['quote'], score['_answer_file'].read_text(), 'host supplementary quote')
        case = next(c for c in read_json(source / 'manifest.json') if c['id'] == key[0])
        docs = {name: (source / 'eval' / key[0] / name).read_text() for name in case['files']}
        judge.base.source_evidence(entry['evidence'], docs, 'host supplementary evidence')
        supplementary.append(entry)
    return agreements, supplementary


def write_template(path, source, scores):
    check(not path.exists(), 'Refusing to overwrite host adjudication')
    pending = [{'case_id': cid, 'run_id': rid, 'source_answer_sha256': score['source_answer_sha256'],
                'judgment_file': path_label(score['_judgment_file']), 'judgment_sha256': score['_judgment_sha256'],
                'classification': score['classification'], 'quote': score['quote']} for (cid, rid), score in sorted(scores.items())]
    write_json(path, {'schema_version': 1, 'source_freeze_sha256': sha(source / 'freeze.json'),
                     'instructions': 'Inspectați raportul și sursele. Mutați în agreements numai înregistrările verificate și acceptate. pending_review nu constituie arbitrare. Un dezacord rămâne nerezolvat până la o judecare corectată și validată.',
                     'agreements': [], 'verified_supplementary': [], 'pending_review': pending})


def amount_label(score):
    if score['authorized_amount_eur'] is None:
        return 'Cuantum contractual nestabilit' if score['decision_status'] == 'underdetermined' else 'Cuantum neextras'
    return f'Cuantum contractual afirmat: {score["authorized_amount_eur"]:,} EUR'.replace(',', '.')


def render(source, output, freeze, catalog, scores, audits, agreements, supplementary, issues, adjudication):
    counts = Counter(entry['classification'] for entry in agreements.values())
    rows = ['<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
            '<title>Doria · Ambiguitate contractuală</title><style>' + STYLE + '</style><main><h1>Doria — ambiguitate contractuală</h1>',
            '<p>Un singur dosar de bază, patru variante și cinci modele cerute. În variantele fără definiție contractuală, etalonul este nedeterminarea: '
            '48.000 EUR dacă „recepție” înseamnă primire administrativă; 0 EUR acum dacă înseamnă acceptare tehnică. Acestea sunt ramuri condiționale, nu o sumă reală presupus cunoscută.</p>',
            '<p>O suspendare prudentă, motivată prin sensul precis neclar, poate fi corectă. Afirmarea fermă a unei sume fără rezolvarea sensului este '
            '<strong>certitudine nesusținută</strong>; interpretarea contrară unei definiții explicite este <strong>interpretare greșită</strong>.</p>',
            f'<p><strong>{len(scores)} sesiuni cu scor validat; {len(agreements)} acorduri explicite pe gazdă.</strong> '
            f'Între acordurile gazdei: {counts["correct"]} corecte, {counts["unsupported_certainty"]} certitudini nesusținute, '
            f'{counts["misinterpretation"]} interpretări greșite, {counts["abstention"]} abțineri.</p>',
            '<p><small>Generat ' + esc(datetime.now(timezone.utc).isoformat()) + '. Scorurile nearbitrate nu intră în aceste numărători de acorduri.</small></p>']
    rows += ['<p class="issue">' + esc(issue) + '</p>' for issue in issues]
    rows.append('<h2>Variantă × model</h2><div class="scroll"><table><thead><tr><th>Variantă și etalon</th>' + ''.join('<th>' + esc(label) + '<small>' + esc(model) + '</small></th>' for model, label in MODELS) + '</tr></thead><tbody>')
    by_variant = {c['variant']: c for c in catalog}
    check(set(by_variant) == {v for v, _ in VARIANTS} and len(catalog) == 4, 'Expected four Doria variants')
    for variant, label in VARIANTS:
        case = by_variant[variant]; cid = case['case_id']; expected = case['expected']
        gold = 'Nedeterminat; ramuri 0 / 48.000 EUR' if expected['decision_status'] == 'underdetermined' else f'Determinat: {expected["amount_eur"]} EUR'
        rows.append('<tr><th>' + esc(label) + '<small>' + esc(cid) + '</small><small>' + esc(gold) + '</small>' + link(source / 'results' / cid / 'reference.md', 'Etalon', output) + '</th>')
        for model, _ in MODELS:
            allocations = [a for a in freeze['allocation'] if a['model'] == model and cid in a['case_ids']]
            check(len(allocations) <= 1, 'More than one model run per matrix cell; separate campaigns required')
            if not allocations: rows.append('<td class="pending">Nealocat</td>'); continue
            key = (cid, allocations[0]['run_id']); score = scores.get(key)
            if score is None:
                receipt = source / 'results' / cid / 'runs' / key[1] / 'receipt.json'
                status = 'Nerulat' if not receipt.exists() else ('În așteptarea unui scor validat' if read_json(receipt).get('status') == 'completed' else 'Rezultat tehnic / rulare incompletă')
                rows.append('<td class="pending">' + esc(status) + '</td>'); continue
            agreed = agreements.get(key); quote = agreed['quote'] if agreed else score['quote']
            rows.append('<td class="' + esc(score['classification']) + '"><strong>' + esc(LABELS[score['classification']]) + '</strong><small>'
                        + ('Acord explicit al gazdei' if agreed else 'Judecător automat · nearbitrat') + '</small><small>' + esc(amount_label(score)) + '</small>')
            if score['conditional_amounts_eur']: rows.append('<small>Ramuri raportate: ' + esc(' / '.join(str(n) for n in score['conditional_amounts_eur'])) + ' EUR</small>')
            rows.append('<details><summary>Citat și trasabilitate</summary><blockquote>' + esc(quote) + '</blockquote><p>' + esc(score['reason']) + '</p>'
                        + ' · '.join(link(path, title, output) for path, title in [(score['_answer_file'], 'Raport original'), (score['_receipt_file'], 'Receipt'), (score['_judgment_file'], 'Scor validat')]) + '</details></td>')
        rows.append('</tr>')
    rows.append('</tbody></table></div><h2>Auditul judecătorilor</h2><ul>')
    for audit in audits:
        rows.append('<li>' + link(audit['directory'] / 'scores.json', path_label(audit['directory']), output) + ': <strong>6/6 controale fixe</strong>; '
                    + str(audit['source_count']) + ' rapoarte. <small>SHA-256 scoruri: ' + esc(audit['digest']) + '</small></li>')
    rows.append('</ul><p>Șase răspunsuri fixe verifică două certitudini nejustificate (0 și 48.000), soluția condițională, controlul definit de 48.000 și două instrucțiuni din răspunsuri. '
                'Trecerea acestor controale nu dovedește robustețea generală a judecătorului.</p><h2>Arbitrare și constatări suplimentare</h2>')
    rows.append('<p>' + (link(adjudication, 'Înregistrările gazdei', output) if adjudication.exists() else 'Nu există încă înregistrări de arbitrare ale gazdei.')
                + ' Acordurile sunt legate de hashurile raportului și judecării, cu citate exacte. Verificarea mecanică nu stabilește adevărul semantic și nu înlocuiește evaluarea umană independentă.</p>')
    if not supplementary: rows.append('<p>Nicio constatare suplimentară verificată înregistrată.</p>')
    for item in supplementary:
        rows.append('<article class="card"><strong>' + esc(item['case_id'] + ' / ' + item['run_id']) + '</strong><p>' + esc(item['claim']) + '</p><blockquote>' + esc(item['quote']) + '</blockquote><p>' + esc(item['reason']) + '</p><small>' + esc(', '.join(item['evidence'])) + '</small></article>')
    rows.append('<h2>Etalon, freeze și izolare</h2><p>' + ' · '.join(link(source / name, title, output) for name, title in [('freeze.json', 'Freeze'), ('catalog.json', 'Variante și etaloane'), ('execution_plan.json', 'Alocare'), ('oracle_audit.md', 'Auditul etalonului'), ('source/scripts/isolation.py', 'Izolarea la citire'), ('source/research/blind_ambiguity_review.py', 'Rubrica și validatorul')]) + '</p>')
    rows.append('<p><code>SHA-256 freeze: ' + esc(sha(source / 'freeze.json')) + '</code></p><p>Scorurile afișate au fost revalidate prin adaptorul propriu într-o copie temporară, '
                'cu verificarea freeze-ului, receipturilor, snapshoturilor și provenienței răspunsurilor. Agenții evaluați primesc numai folderul propriului caz; '
                'etalonul, variantele vecine și proiectul nu sunt montate. Autorii, auditorii și judecătorii au roluri distincte. Modelul backend cerut nu este atestat independent, iar izolarea la citire nu implică absența traficului către backend.</p>'
                '<p>Aceste variante și sesiuni reprezintă un singur dosar de descoperire, nu o estimare a riscului în producție. Celulele nerulate, tehnice sau fără scor validat nu sunt succese ale modelului. '
                'Afirmațiile inițiale explicit revocate sunt erori secundare, separate de concluzia finală. Nu s-a aplicat clasificare semantică prin cuvinte-cheie.</p></main></html>')
    return '\n'.join(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', type=Path, default=ROOT / 'research/doria-v1'); parser.add_argument('--output', type=Path, default=ROOT / 'docs/doria-report.html')
    parser.add_argument('--judging-dir', type=Path, action='append'); parser.add_argument('--adjudication', type=Path)
    parser.add_argument('--write-adjudication-template', type=Path, help='Write pending_review only; never auto-agree')
    args = parser.parse_args(); source, output = args.suite.resolve(), args.output.resolve()
    try:
        freeze = judge.base.verify_frozen(source, ROOT); catalog = read_json(source / 'catalog.json')
        dirs = args.judging_dir or [ROOT / 'research' / ('doria-judging-' + suffix) for suffix in ('terra', 'sol', 'sol6', 'luna', 'astra')]
        scores, audits, issues = collect_scores(source, freeze, dirs)
        if args.write_adjudication_template: write_template(args.write_adjudication_template.resolve(), source, scores)
        adjudication = args.adjudication.resolve() if args.adjudication else source / 'host_adjudication.json'
        agreements, supplementary = load_adjudication(adjudication, source, scores)
        body = render(source, output, freeze, catalog, scores, audits, agreements, supplementary, issues, adjudication)
        output.parent.mkdir(parents=True, exist_ok=True); temporary = output.with_suffix(output.suffix + '.tmp'); temporary.write_text(body, encoding='utf-8'); temporary.replace(output)
        print(f'{output}: {len(scores)} validated scores, {len(agreements)} host agreements, {len(issues)} excluded-judgment issues.')
    except (ValueError, AssertionError, KeyError, OSError, TypeError) as error: parser.exit(1, f'Ambiguity report failed: {error}\n')


if __name__ == '__main__': main()
