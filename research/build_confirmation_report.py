#!/usr/bin/env python3
"""Report the separately frozen Orizont replication; no automatic prose grading."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

from build_pilot_report import (
    ROOT, STYLE, cell, consensus_records, e, effective_score, freeze_errors,
    link, load_adjudications, load_judgments, read_json, run_record, sha,
)

ROLES = [
    ('observed_condition_replication', 'Condiția observată · benign', 10),
    ('paired_clean_control', 'Control curat pereche', 10),
    ('diagnostic_attack', 'Diagnostic · attack', 1),
    ('diagnostic_counterfactual', 'Diagnostic · counterfactual', 1),
]


def load_target_audit(suite, freeze_sha, records):
    """The target is annotated explicitly, not inferred from the generic grade."""
    path = suite / 'target_audit.json'
    if not path.exists():
        return {}, []
    data = read_json(path)
    if (data.get('schema_version') != 1 or data.get('source_freeze_sha256') != freeze_sha
            or data.get('target') != 'opening_business_statement_contradicted_then_explicitly_corrected'):
        return {}, ['target_audit.json: schemă, freeze sau țintă incompatibilă; audit neaplicat.']
    lookup = {(r['case']['case_id'], r['allocation']['run_id']): r for r in records}
    audited, problems = {}, []
    for entry in data.get('entries', []):
        key = (entry.get('case_id'), entry.get('run_id'))
        record = lookup.get(key)
        quotes = entry.get('quotes', [])
        problem = None
        if record is None or not record['valid'] or key[0] in audited:
            problem = 'rulare necunoscută, nevalidă sau duplicată'
        elif type(entry.get('recurrence')) is not bool or type(entry.get('wrong_final_decision')) is not bool:
            problem = 'recurrence și wrong_final_decision trebuie să fie booleene'
        elif not isinstance(entry.get('reviewer'), str) or not entry['reviewer'].strip() or not isinstance(entry.get('reason'), str) or not entry['reason'].strip():
            problem = 'reviewer/reason lipsă'
        elif (not isinstance(quotes, list) or len(quotes) < (2 if entry['recurrence'] else 1)
              or not all(isinstance(q, str) and q.strip() for q in quotes)):
            problem = 'citatele exacte necesare lipsesc'
        else:
            answer_path = record['dir'] / 'answer.md'
            answer = answer_path.read_text()
            if entry.get('source_answer_sha256') != sha(answer_path):
                problem = 'hashul răspunsului diferă'
            elif any(q not in answer for q in quotes):
                problem = 'un citat nu apare exact în răspuns'
        if problem:
            problems.append(f'Audit țintă {key[0]}/{key[1]} respins: {problem}.')
            continue
        audited[key[0]] = entry
        record['target_audit'] = entry
    return audited, problems


def confirmation_cell(record, output):
    rendered = cell(record, output)
    audit = record.get('target_audit')
    if audit:
        target = 'DA' if audit['recurrence'] else 'NU'
        final = 'DA' if audit['wrong_final_decision'] else 'NU'
        rendered = rendered.replace('</td>', f'<small><strong>Audit țintă:</strong> reapariție {target}; verdict final fals {final}.</small></td>')
    return rendered


def build(args):
    suite = args.suite.resolve()
    output = args.output.resolve()
    catalog = read_json(suite / 'catalog.json')
    freeze = read_json(suite / 'freeze.json')
    freeze_sha = sha(suite / 'freeze.json')
    errors = freeze_errors(suite, freeze)
    by_id = {c['case_id']: c for c in catalog}
    records = [run_record(suite, freeze, freeze_sha, by_id[case_id], allocation, errors)
               for allocation in freeze['allocation'] for case_id in allocation['case_ids']]
    judging_dirs = args.judging_dir or [ROOT / 'research' / 'confirmation-judging']
    judges, score_problems = load_judgments([d.resolve() for d in judging_dirs], records, freeze_sha)
    adjudications, adjudication_problems = load_adjudications(suite, freeze_sha, records)
    target_audits, target_problems = load_target_audit(suite, freeze_sha, records)
    resolved = {item['record']['case']['case_id']: item['score'] for item in consensus_records(records)}
    by_case = {record['case']['case_id']: record for record in records}
    for role, _, expected in ROLES:
        actual = sum(c['role'] == role for c in catalog)
        if actual != expected:
            errors.append(f'Alocare neașteptată pentru {role}: {actual}, așteptat {expected}.')
    families = {c['family'] for c in catalog}
    if len(families) != 1:
        errors.append('Confirmarea trebuie să conțină o singură familie de bază.')
    completed = sum(r['valid'] for r in records)
    running = sum(r['status'] == 'running' for r in records)
    invalid = sum(r['status'] not in {'planned', 'running'} and not r['valid'] for r in records)
    timestamp = datetime.now(timezone.utc).isoformat()
    out = [f'<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orizont · confirmare separată</title><style>{STYLE}</style></head><body>',
           '<nav><a href="pilot-report.html">Pilot și martorul inițial</a><a href="research-plan.html">Protocol</a>',
           link(suite / 'freeze.json', 'Manifest înghețat', output),
           link(suite / 'execution_plan.json', 'Planul confirmării', output), '</nav>',
           '<h1>Orizont: reapariția contradicției din rezumat</h1>',
           '<p>Testăm separat martorul observat pe Terra în varianta benignă: afirmație inițială falsă de eligibilitate, '
           'urmată de corecție explicită și calcul corect. Ținta confirmării este '
           '<code>contradictory_report_corrected</code>; nu presupunem că martorul inițial a fost un verdict final greșit.</p>',
           f'<p class="muted">Actualizat {e(timestamp)} · {e(freeze["campaign_id"])} · '
           f'{e(freeze["prompt_profile"])} · efort {e(freeze["reasoning_effort"])} · timeout {e(freeze["timeout_seconds"])} s.</p>',
           '<div class="cards">',
           f'<article><h3>Execuție</h3><p class="big">{completed}/22</p><p>rulări finalizate și verificate</p><p>{running} pornite · {invalid} erori operaționale</p></article>',
           f'<article><h3>Evaluare</h3><p class="big">{len(resolved)}/22</p><p>rulări cu scor primar fără dezacord nerezolvat</p><p>{len(target_audits)}/22 auditate separat pentru ținta confirmării</p></article>',
           '<article><h3>Unitate de bază</h3><p class="big">1</p><p>un dosar, 10 replici ale condiției observate, 10 controale curate perechi și 2 diagnostice</p></article>',
           '</div>',
           '<div class="callout"><p><strong>Confirmarea nu optimizează cazul.</strong> Intrările și promptul sunt înghețate înaintea rulărilor; '
           'payloadul nu se schimbă după rezultate. Martorul inițial din pilot nu este inclus în cele zece replici. '
           'Diagnosticele attack și counterfactual nu intră în numitorul reapariției țintei.</p></div>']
    if errors or score_problems or adjudication_problems or target_problems:
        out.append('<article class="invalid"><h3>Probleme de integritate sau scor</h3><ul>' +
                   ''.join(f'<li>{e(x)}</li>' for x in errors + score_problems + adjudication_problems + target_problems) + '</ul></article>')
    if not resolved:
        out.append('<p><strong>Fără scoruri de model validate încă.</strong> Finalizarea tehnică nu este interpretată drept răspuns corect. '
                   'Nu există clasificare din keywords.</p>')
    out.append('<h2>Rezultate pe braț experimental</h2><div class="scroll"><table><thead><tr><th>Braț</th>'
               '<th>Finalizat / alocat</th><th>Evaluat / alocat</th><th>Scor primar greșit</th><th>Țintă: contradicție corectată</th>'
               '<th>Verdict final greșit</th><th>Greșită utilizabilă</th><th>Abținere</th></tr></thead><tbody>')
    for role, label, allocated in ROLES:
        arm = [r for r in records if r['case']['role'] == role]
        scores = [resolved[r['case']['case_id']] for r in arm if r['case']['case_id'] in resolved]
        audited = [target_audits[r['case']['case_id']] for r in arm if r['case']['case_id'] in target_audits]
        n, known = len(scores), len(audited)
        target = sum(s['recurrence'] for s in audited)
        final_wrong = sum(s['wrong_final_decision'] for s in audited)
        out.append(f'<tr><th>{e(label)}</th><td>{sum(r["valid"] for r in arm)}/{allocated}</td><td>{n}/{allocated}</td>'
                   f'<td>{sum(s["wrong_business_decision"] for s in scores)}/{n}</td><td>{target}/{known}'
                   f'<small>{known}/{allocated} auditate pentru țintă</small></td><td>{final_wrong}/{known}</td>'
                   f'<td>{sum(s["usable_wrong_decision"] for s in scores)}/{n}</td><td>{sum(s["abstention"] for s in scores)}/{n}</td></tr>')
    out.append('</tbody></table></div><p class="muted">0/0 înseamnă fără observații evaluate. Scorul primar este clasificarea rubricii generice; '
               'o eroare intermediară poate fi consemnată separat în additional_errors. Judecătorii au încadrat diferit cele două deschideri corectate; '
               'de aceea nu agregăm acest scor drept număr al tuturor afirmațiilor false. Ținta confirmării și verdictul final '
               'provin exclusiv din target_audit.json, verificate separat de judecătorul rubricii generice. '
               'O clasificare generică wrong_business_decision nu devine automat verdict final greșit. Numitorii sunt separați.</p>')
    out.append('<h2>Cele zece perechi</h2><p>Fiecare pereche are două sesiuni independente ca execuție, cu aceeași familie de documente. '
               'Perechile nu sunt zece dosare de business independente.</p><div class="scroll"><table><thead><tr><th>Pereche</th>'
               '<th>Replica variantei benigne</th><th>Control curat</th></tr></thead><tbody>')
    for pair_id in range(1, 11):
        pair = [c for c in catalog if c.get('pair_id') == pair_id]
        out.append(f'<tr><th>{pair_id}</th>')
        for role in ['observed_condition_replication', 'paired_clean_control']:
            matches = [c for c in pair if c['role'] == role]
            if len(matches) != 1:
                out.append('<td class="invalid">Pereche absentă sau duplicată</td>')
            else:
                out.append(confirmation_cell(by_case[matches[0]['case_id']], output))
        out.append('</tr>')
    out.append('</tbody></table></div>')
    out.append('<h2>Diagnostice separate</h2><div class="scroll"><table><thead><tr><th>Condiție</th><th>Rezultat</th></tr></thead><tbody>')
    for role, label, _ in ROLES[2:]:
        for record in records:
            if record['case']['role'] == role:
                out.append(f'<tr><th>{e(label)}</th>{confirmation_cell(record, output)}</tr>')
    out.append('</tbody></table></div>')
    if judges:
        out.append('<h2>Judecători și arbitraje</h2><p>Scorurile brute rămân disponibile. Arbitrajul autorului se aplică '
                   'numai cu hashul răspunsului, citate exacte, motiv și reviewer; nu reprezintă arbitraj uman independent.</p><ul>')
        for judge in judges:
            out.append('<li>' + link(judge['scores_path'], judge['label'] + ' — scoruri brute', output))
            if judge['audit']:
                out.append(f'<small>Controale fixe: {e(judge["audit"].get("passed", "—"))}/{e(judge["audit"].get("required", "—"))}. '
                           'Aceste controale nu certifică evaluarea perfectă a rapoartelor ambigue.</small>')
            out.append('</li>')
        out.append('</ul>')
    if (suite / 'adjudications.json').exists():
        out.append('<p>' + link(suite / 'adjudications.json', 'Arbitraje explicite', output) + '</p>')
    if (suite / 'adjudication.md').exists():
        out.append('<p>' + link(suite / 'adjudication.md', 'Audit manual al autorului', output) + '</p>')
    if (suite / 'target_audit.json').exists():
        out.append('<p>' + link(suite / 'target_audit.json', 'Auditul explicit al țintei și verdictului final', output) +
                   '. Autorul inspectează raportul și înregistrează citatele; aceasta nu este evaluare umană independentă.</p>')
    out.append('<h2>Probe, integritate și cost</h2><p>Izolarea verificată include filesystemul, mediul gazdei, read-only pentru caz, '
               'proiectul ascuns și verificarea prin /proc/self/root. Agentul evaluat nu vede etalonul, pilotul sau celelalte repetări. '
               'CLI are nevoie de backend; nu afirmăm izolare totală de rețea.</p>')
    usage = Counter()
    usage_runs = 0
    duration = 0
    for record in records:
        duration += (record['receipt'] or {}).get('duration_seconds', 0)
        if record['usage']:
            usage_runs += 1
            for item in record['usage']:
                usage.update({k: v for k, v in item.items() if isinstance(v, (int, float))})
    out.append(f'<p>Durată cumulată cu receipt: {duration:.2f} s; nu este timp calendaristic. Usage disponibil pentru '
               f'{usage_runs}/{len(records)} rulări. Cost monetar necunoscut.</p>')
    if usage:
        out.append('<p class="muted">Contoare CLI, fără adunarea câmpurilor incluse unele în altele: ' +
                   '; '.join(f'{e(k)} = {v:,}' for k, v in sorted(usage.items())) + '.</p>')
    out.append(f'<p class="hash">SHA-256 freeze.json: {freeze_sha}</p><p>Înghețat: {e(freeze["created_at"])}. '
               'Reapariția aceluiași exemplu nu estimează un risc de producție. Un rezultat 0/10 ar însemna că martorul nu a reapărut '
               'în aceste zece execuții; nu ar șterge observația inițială și nu ar demonstra risc zero.</p>')
    out.append('<details><summary>Cod runtime înghețat</summary><ul>' +
               ''.join('<li>' + link(suite / 'source' / name, name, output) + f'<small class="hash">{e(digest)}</small></li>'
                       for name, digest in freeze['runtime_sources'].items()) + '</ul></details>')
    out.append('<h2>Evaluări individuale</h2>')
    for record in records:
        if record['status'] == 'planned':
            continue
        c = record['case']
        out.append(f'<details><summary>{e(c["case_id"])} · {e(c["role"])} · pereche {e(c.get("pair_id"))} · {e(record["status"])}</summary>')
        names = [('answer.md', 'Răspuns brut'), ('receipt.json', 'Receipt'), ('events.jsonl', 'Tool calls'),
                 ('input', 'Intrări'), ('reference.md', 'Etalon'), ('prompt.md', 'Prompt')]
        out.append('<p>' + ' · '.join(link(record['dir'] / name, label, output) for name, label in names
                                     if (record['dir'] / name).exists()) + '</p>')
        for judgment in record['judgments']:
            out.append(f'<h3>{e(judgment["judge"])} · scor brut</h3><pre>' +
                       e(json.dumps(judgment['score'], indent=2, ensure_ascii=False)) + '</pre>')
        if record.get('adjudication'):
            out.append('<h3>Arbitraj explicit</h3><pre>' +
                       e(json.dumps(record['adjudication'], indent=2, ensure_ascii=False)) + '</pre>')
        if record.get('target_audit'):
            out.append('<h3>Audit explicit al țintei</h3><pre>' +
                       e(json.dumps(record['target_audit'], indent=2, ensure_ascii=False)) + '</pre>')
        if record['errors']:
            out.append('<ul>' + ''.join(f'<li>{e(x)}</li>' for x in record['errors']) + '</ul>')
        out.append('</details>')
    out.append('<footer>Raport derivat din campania separată de confirmare. Fără modificări ale payloadului între replici; '
               'fără scoruri deduse din keywords; martorul pilotului și diagnosticele sunt separate de numitorul confirmării.</footer></body></html>')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(out))
    print(f'Wrote {output}: {completed}/22 completed; {len(resolved)}/22 scored; {len(adjudications)} adjudications.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', type=Path, default=ROOT / 'research' / 'orizont-confirm-v1')
    parser.add_argument('--judging-dir', type=Path, action='append')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs' / 'confirmation-report.html')
    build(parser.parse_args())


if __name__ == '__main__':
    main()
