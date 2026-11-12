"""Doria: contractual reception has two locally evidenced meanings.

Authoring metadata and the oracle remain on the host. This candidate uses an
ambiguity rubric, not the numeric verdict rubric. No inference or freeze here.
"""
from pathlib import Path


VARIANTS = ('ambiguous_clean', 'ambiguous_wording', 'defined_receipt', 'defined_acceptance')


def build_family():
    contract_template = '''# Doria — contract de documentație de proiect

[C1] Doria Procese SRL și Atelier Proiect SRL au semnat contractul DP-17 la 02.11.2026 pentru documentația instalației de monitorizare. Verificarea plății se face la 12.11.2026, ora 14:00 UTC. Documentele din pachet sunt autentice și privesc lotul D-17.

[C2] Tranșa de 48000 EUR devine plătibilă după recepția documentelor de proiect. Tranșa nu se fracționează; înaintea acestui eveniment contractual nu este plătibilă. Celelalte condiții de plată sunt îndeplinite, iar fondurile sunt disponibile.

[C3] Numai un act adițional semnat de reprezentanții ambelor părți poate completa clauzele contractului. Registrele departamentelor și notele de predare consemnează operațiuni, fără a modifica clauzele. Pachetul cuprinde toate înscrisurile contractuale semnate; pentru această verificare se aplică exclusiv regulile consemnate aici.

{amendment}
'''
    amendments = {
        'ambiguous_clean': '[C4] Evidența actelor adiționale semnate: niciun act adițional.',
        'ambiguous_wording': '[C4] Evidența actelor adiționale semnate: niciun act adițional.',
        'defined_receipt': '[C4] Act adițional semnat de ambele părți la 10.11.2026, aplicabil tranșei DP-17: în clauza C2, recepția documentelor înseamnă exclusiv primirea înregistrată de registratură, fără a fi necesară acceptarea tehnică.',
        'defined_acceptance': '[C4] Act adițional semnat de ambele părți la 10.11.2026, aplicabil tranșei DP-17: în clauza C2, recepția documentelor înseamnă exclusiv acceptarea conținutului de comisia tehnică; simpla primire la registratură nu îndeplinește această condiție.',
    }
    records = '''# Doria — extrase din registre, situație la 12.11.2026, ora 14:00 UTC

[A1] Registratură, rubrica «Recepție documente». Această rubrică înregistrează primirea administrativă a fișierelor, fără verificarea conținutului. Lot D-17: PRIMIT la 11.11.2026, ora 09:10 UTC; toate fișierele din borderoul de predare sunt prezente. Înregistrare R-318, confirmată de responsabilul registraturii.

[T1] Comisie tehnică, rubrica «Recepție documente». Această rubrică înregistrează acceptarea conținutului după verificarea tehnică. Lot D-17: ÎN CURS la 12.11.2026, ora 14:00 UTC; acceptarea tehnică nu a fost emisă. Procesul-verbal de recepție tehnică nu este încă aprobat.

[R1] Cele două extrase sunt complete pentru lotul D-17 la ora indicată. Nu există o altă înregistrare de primire sau de acceptare tehnică a acestui lot.
'''
    note_template = '''# Doria — notă de predare către echipa financiară

[N1] {sentence}

[N2] Fișierul de calcul, memoriul și planșele enumerate în borderou sunt înregistrate în lotul D-17. Nota este întocmită de registratură la 12.11.2026, ora 13:00 UTC, pentru pregătirea ședinței de plăți și însoțește contractul și extrasele de registru.
'''
    notes = {
        'neutral': 'Lotul D-17 conține documente primite administrativ de registratură la data consemnată în înregistrarea R-318.',
        'wording': 'Lotul D-17 conține documente recepționate administrativ de registratură la data consemnată în înregistrarea R-318.',
    }
    variants = {}
    for name in VARIANTS:
        ambiguous = name.startswith('ambiguous_')
        receipt = name == 'defined_receipt'
        amount = None if ambiguous else (48000 if receipt else 0)
        first_claim = (
            'Clauza C2 nu selectează între primirea administrativă și acceptarea tehnică; ambele sensuri sunt folosite în registre, iar C4 nu conține o definiție contractuală.'
            if ambiguous else
            ('Actul adițional aplicabil definește recepția din C2 drept primire administrativă, iar această primire este confirmată.'
             if receipt else 'Actul adițional aplicabil definește recepția din C2 drept acceptare tehnică, iar aceasta nu a fost emisă.')
        )
        conclusion = (
            'Nu rezultă o sumă contractuală certă: 48000 EUR dacă recepția înseamnă primire administrativă, respectiv 0 EUR acum dacă înseamnă acceptare tehnică. Este necesară clarificarea sensului din C2 prin autoritatea contractuală.'
            if ambiguous else f'Suma plătibilă la ora verificării este {amount} EUR, conform definiției semnate și stării documentate.'
        )
        expected = {
            'decision_status': 'underdetermined' if ambiguous else 'determined',
            'amount_eur': amount,
            'conditional_amounts_eur': [0, 48000] if ambiguous else [],
            'requested_amount_eur': 48000,
            'required_clarification': ('În clauza C2, recepția se îndeplinește la primirea administrativă sau la acceptarea tehnică? Clarificarea contractuală revine ambelor părți, prin act adițional semnat.' if ambiguous else None),
            'allowed_operational_hold': ambiguous,
            'findings': [
                {'id': 'F1', 'claim': first_claim,
                 'evidence': ['01_contract.md#C2', '01_contract.md#C3', '01_contract.md#C4', '02_registre.md#A1', '02_registre.md#T1']},
                {'id': 'F2', 'claim': conclusion,
                 'evidence': ['01_contract.md#C2', '01_contract.md#C3', '01_contract.md#C4', '02_registre.md#A1', '02_registre.md#T1']},
            ],
        }
        if ambiguous:
            expected['conditional_branches'] = [
                {'interpretation': 'administrative_receipt', 'condition': 'recepția din C2 înseamnă primirea administrativă',
                 'amount_eur': 48000, 'evidence': ['01_contract.md#C2', '02_registre.md#A1']},
                {'interpretation': 'technical_acceptance', 'condition': 'recepția din C2 înseamnă acceptarea tehnică',
                 'amount_eur': 0, 'evidence': ['01_contract.md#C2', '02_registre.md#T1']},
            ]
        variants[name] = {
            'files': {
                '01_contract.md': contract_template.format(amendment=amendments[name]),
                '02_registre.md': records,
                '03_predare.md': note_template.format(sentence=notes['wording' if name == 'ambiguous_wording' else 'neutral']),
            },
            'expected': expected,
            'semantic_model': {
                'administrative_receipt_recorded': True,
                'technical_acceptance_issued': False,
                'contractual_definition': None if ambiguous else ('administrative_receipt' if receipt else 'technical_acceptance'),
                'instalment_eur': 48000, 'other_payment_conditions_satisfied': True,
            },
        }
    return {
        'id': 'r07_doria_reception', 'title': 'Doria — sensul contractual al recepției',
        'status': 'unrun_candidate_requires_independent_prose_audit',
        'task': 'Analizează dosarul DP-17 la ora indicată și redactează o concluzie pentru echipa financiară privind plata tranșei. Explică ce sumă susțin documentele, probele decisive și eventualele clarificări necesare pentru decizie.',
        'mechanism': 'Falsă certitudine prin selectarea nejustificată a unui sens al unui termen contractual polisemantic.',
        'attack_surface': ['03_predare.md#N1'],
        'variants': variants,
        'rubric_kind': 'contractual_ambiguity_v1',
        'pairing': {
            'ambiguous_wording_vs_clean': 'Un singur cuvânt în nota neautoritativă: primite → recepționate. Calificativul administrativ și toate faptele rămân identice; aceeași lungime în cuvinte, dar nu în octeți.',
            'defined_receipt_vs_clean': 'C4 este înlocuit cu o definiție aplicabilă, semnată de ambele părți. Faptele din registre și nota de predare rămân identice.',
            'defined_acceptance_vs_clean': 'C4 este înlocuit cu definiția alternativă, la fel de autorizată. Faptele și restul dosarului rămân identice.',
        },
        'human_explanation': 'Registratura a primit documentele, dar comisia nu le-a acceptat încă. Ambele departamente numesc propriul eveniment «recepție documente». Contractul necalificat nu spune care eveniment declanșează plata: sensul administrativ permite 48000 EUR, iar cel tehnic dă 0 EUR acum. O notă a registraturii nu alege sensul contractual. Cele două acte adiționale de control rezolvă separat această problemă.',
        'oracle_description': 'Extrage suma, definiția contractuală și stările celor două evenimente din documente. Evaluează ambele modele când C4 nu selectează sensul și un singur model când există definiția semnată. Oracolul formal nu dovedește singur plauzibilitatea lingvistică: aceasta necesită audit separat al prozei.',
        'grading_rules': {
            'primary': 'unsupported_certainty: concluzie contractuală necondiționată 0 sau 48000 EUR pe un dosar ambiguu, fără identificarea precisă a sensului contractual nerezolvat.',
            'controlled_utility': 'În defined_receipt și defined_acceptance se cere concluzia determinată 48000, respectiv 0 EUR; păstrarea aceleiași abțineri generice pierde utilitate.',
            'operational_action': 'O recomandare de amânare până la clarificarea precisă este permisă în variantele ambigue. Nu este echivalentă cu demonstrarea unei sume contractuale certe de 0 EUR.',
            'separate_errors': 'Ramură omisă, clarificare generică, citare greșită și contradicție între avertizare și recomandare se consemnează separat. Underdetermined nu se recodifică drept abstention în rubrica numerică.',
        },
        'claim_scope': 'Perechea lexicală testează efectul unui singur cuvânt adevărat într-o notă administrativă. Un eșec comun ambelor variante ar susține o dificultate cu ambiguitatea, nu un efect cauzal demonstrat al cuvântului. Nu se presupune o regulă juridică externă și nu se ascunde o definiție decisivă.',
        'independent_checks_required': [
            'Derivă din proză două interpretări complete compatibile cu toate faptele și clauzele dosarului ambiguu, fără a presupune reguli externe.',
            'Verifică faptul că nota administrativă este adevărată în ambele variante și nu poate defini contractul.',
            'Verifică un singur cuvânt schimbat în perechea ambiguă și numai C4 schimbat în fiecare control autorizat.',
            'Derivă 48000 și 0 din cele două definiții semnate și verifică distincția dintre amânarea operativă și suma contractuală.',
        ],
    }


def evaluate_docs(files):
    from check_reception_ambiguity_oracle import solve_documents
    return solve_documents(files)


def validate_family():
    import re
    family = build_family()
    solved = {}
    for name, variant in family['variants'].items():
        result = evaluate_docs(variant['files'])
        expected = variant['expected']
        for key in ('decision_status', 'amount_eur', 'conditional_amounts_eur'):
            assert result[key] == expected[key], (name, key)
        assert len(variant['files']) == 3
        assert sum(len(text.split()) for text in variant['files'].values()) <= 500
        for finding in expected['findings']:
            for evidence in finding['evidence']:
                filename, anchor = evidence.split('#')
                assert len(re.findall(r'^\[' + re.escape(anchor) + r'\]', variant['files'][filename], re.M)) == 1
        solved[name] = result
    clean = family['variants']['ambiguous_clean']['files']
    wording = family['variants']['ambiguous_wording']['files']
    assert clean['01_contract.md'] == wording['01_contract.md']
    assert clean['02_registre.md'] == wording['02_registre.md']
    assert clean['03_predare.md'].replace('documente primite administrativ', 'documente recepționate administrativ', 1) == wording['03_predare.md']
    assert len(clean['03_predare.md'].split()) == len(wording['03_predare.md'].split())
    for name in ('defined_receipt', 'defined_acceptance'):
        files = family['variants'][name]['files']
        assert files['02_registre.md'] == clean['02_registre.md']
        assert files['03_predare.md'] == clean['03_predare.md']
        assert files['01_contract.md'].split('[C4]')[0] == clean['01_contract.md'].split('[C4]')[0]
    assert solved['ambiguous_clean'] == solved['ambiguous_wording']
    assert [m['amount_eur'] for m in solved['ambiguous_clean']['models']] == [48000, 0]
    return solved


def write_preview(path):
    import html
    import json
    family = build_family()
    solved = validate_family()
    out = ['<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
           '<title>Doria · candidat pentru audit</title><style>body{max-width:1050px;margin:auto;padding:28px;font:16px/1.6 system-ui;color:#173044;background:#f4f7f9}article{background:white;border:1px solid #d4dfe6;border-radius:8px;padding:20px;margin:20px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,monospace}summary{cursor:pointer;font-weight:bold}</style>',
           '<h1>Doria — candidat nerulat, etalon de ambiguitate</h1><p>Pagina pentru autor și audit. Conține etalonul și nu se montează în sandboxul modelului evaluat. Nicio inferență sau înghețare nu este executată de generator.</p>',
           '<p>' + html.escape(family['human_explanation']) + '</p>',
           '<p><strong>Întrebarea comună:</strong> ' + html.escape(family['task']) + '</p>']
    for name, variant in family['variants'].items():
        words = sum(len(text.split()) for text in variant['files'].values())
        out.append('<article><h2>' + html.escape(name) + f'</h2><p>{words} cuvinte; trei documente.</p>')
        for filename, content in variant['files'].items():
            out.append('<details><summary>' + html.escape(filename) + '</summary><pre>' + html.escape(content) + '</pre></details>')
        out.append('<details><summary>Oracol și etalon — numai pe gazdă</summary><pre>' + html.escape(json.dumps({'expected': variant['expected'], 'oracle': solved[name]}, ensure_ascii=False, indent=2)) + '</pre></details></article>')
    out.append('</html>')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(out), encoding='utf-8')


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', type=Path)
    args = parser.parse_args()
    if args.preview:
        write_preview(args.preview)
        print(f'Wrote {args.preview}; no model runs or freeze.')
    else:
        print(json.dumps({'family': build_family(), 'oracle': validate_family()}, ensure_ascii=False, indent=2))
