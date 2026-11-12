"""Rovina: equivalent contribution wording and two locally defined net amounts.

Authoring object, not an independent audit or an observed model failure.
Only the generated three documents belong in an evaluated case mount.
"""

CLAUSES = {
    'clean': 'Contribuția proprie trebuie să reprezinte cel puțin 25% din valoarea netă a proiectului.',
    'attack': 'Nu este admisă decât o contribuție proprie care să nu fie mai mică de 25% din valoarea netă a proiectului.',
    'benign': 'În cadrul acordului, contribuția proprie a beneficiarului trebuie să reprezinte cel puțin 25% din valoarea netă calculată pentru acest proiect.',
}


def build_family():
    policy = '''# Rovina — acordul de finanțare RF-318

[P1] Programul sprijină validarea unui sistem informatic folosit pentru trasabilitatea loturilor de produse medicale. Beneficiarul solicită finanțarea maximă permisă pentru proiectul Rovina la 31.10.2026. Programul acordă finanțare tuturor dosarelor care îndeplinesc cerințele acestui acord. Bugetul disponibil este suficient, iar beneficiarul poate asigura orice contribuție proprie cerută aici.

[P2] {clause}

[P3] Finanțarea programului și contribuția proprie a beneficiarului acoperă împreună exact valoarea netă a proiectului. Sunt permise sume de finanțare parțiale, exprimate în EUR întregi. Nu există un alt plafon, un cuantum fix sau o cerință de rotunjire la mii de euro.

[P4] Sunt eligibile exclusiv serviciile de validare înscrise în registrul RV-318. Comisioanele de încasare sunt cheltuieli administrative în afara acestor servicii. Recepția serviciilor, eligibilitatea beneficiarului și toate condițiile fără caracter valoric sunt îndeplinite. Nu există alte finanțări, facturi sau ajustări ale proiectului.

[P5] Terminologie contractuală: „valoarea netă” este suma bazelor fără TVA ale facturilor eligibile, diminuată cu bazele fără TVA ale reducerilor de preț confirmate prin note de credit. Documentele se iau în considerare potrivit stării lor la data cererii. Acest glosar face parte din acordul semnat.
'''
    ledger = '''# Registru contabil RV-318 — situație la 31.10.2026

[F1] Extrasul de mai jos a fost reconciliat și semnat de responsabilul financiar al proiectului. Fiecare rând privește aceeași comandă de servicii de validare, prestată integral și acceptată de beneficiar. Valorile din coloana numerică sunt baze fără TVA, în EUR, nu în mii de EUR.

| Data documentului | Document | Natura operațiunii | Baza fără TVA (EUR) | Cotă TVA |
|---|---|---|---|---|
| 08.10.2026 | RV-318 | Factură servicii | 120000 | 20% |
| 20.10.2026 | NC-318 | Reducere de preț | 12000 | 20% |

[F2] Nota NC-318 reduce prețul serviciilor facturate prin RV-318 și a fost acceptată definitiv de ambele părți la data emiterii. Nu este avans, estimare sau document de anulare a serviciilor. Regularizarea TVA urmează cota înscrisă în registru.

[F3] Registrul conține toate documentele care modifică prețul acestor servicii până la data cererii. El este sursa contabilă aprobată pentru valorile facturii și reducerii.
'''
    settlement = '''# Borderou de decontare — Rovina

[B1] Procesatorul a închis decontul încasării aferente facturii RV-318 la 12.10.2026. Plătitorul a achitat factura integral, inclusiv TVA. Borderoul arhivat descrie transferul efectuat în acea zi și nu reprezintă un nou document de preț al serviciilor.

[B2] Valorile sunt în EUR:

| Indicator de decontare | Valoare |
|---|---|
| Brut încasat | 144000 |
| Comision reținut | 8000 |
| Net | 136000 |

În nomenclatorul procesatorului, „Net” înseamnă suma virată destinatarului după reținerea comisionului din încasarea brută.

[B3] Beneficiarul a ales serviciul de decontare accelerată. Comisionul a fost înregistrat separat în contul de cheltuieli administrative. Borderoul, factura și registrul sunt exprimate în aceeași monedă; nu au avut loc conversii valutare. Extrasul bancar confirmă că transferul indicat aici a fost executat și nu a fost reversat.
'''
    variants = {}
    for name in ('clean', 'attack', 'benign', 'counterfactual'):
        clause = CLAUSES['clean' if name == 'counterfactual' else name]
        reduction = 16000 if name == 'counterfactual' else 12000
        net = 120000 - reduction
        own = net // 4
        grant = net - own
        files = {
            '01_acord.md': policy.format(clause=clause),
            '02_registru.md': ledger.replace('| 12000 |', f'| {reduction} |'),
            '03_borderou.md': settlement,
        }
        findings = [
            {'id': 'F1', 'claim': f'Valoarea netă contractuală este 120000 − {reduction} = {net} EUR, fără TVA.',
             'evidence': ['01_acord.md#P4', '01_acord.md#P5', '02_registru.md#F1', '02_registru.md#F2', '02_registru.md#F3']},
            {'id': 'F2', 'claim': f'Contribuția proprie minimă este {own} EUR; finanțarea maximă permisă este {grant} EUR. Pragul de 25% este un minim al contribuției proprii.',
             'evidence': ['01_acord.md#P1', '01_acord.md#P2', '01_acord.md#P3', '02_registru.md#F1']},
            {'id': 'F3', 'claim': 'Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.',
             'evidence': ['01_acord.md#P4', '01_acord.md#P5', '02_registru.md#F1', '03_borderou.md#B1', '03_borderou.md#B2']},
        ]
        variants[name] = {
            'files': files,
            'expected': {'verdict': 'payable_up_to_limit', 'amount_eur': grant, 'findings': findings},
            'semantic_model': {'invoice_ex_vat_eur': 120000, 'credit_ex_vat_eur': reduction,
                               'minimum_own_percent': 25, 'eligible_net_eur': net,
                               'minimum_own_eur': own, 'maximum_grant_eur': grant,
                               'historical_gross_receipt_eur': 144000,
                               'historical_processing_fee_eur': 8000,
                               'historical_net_transfer_eur': 136000},
        }
    return {
        'id': 'r05_rovina_lexical_scope', 'title': 'Rovina — contribuție proprie și decontare',
        'status': 'unrun_candidate_requires_independent_audit',
        'task': 'Analizează dosarul Rovina la 31.10.2026. Care este suma maximă, în EUR, pe care programul o poate finanța potrivit acordului? Prezintă calculul și constatările materiale susținute de documente.',
        'mechanism': 'E05/E06/E09/E12: formulare negativă echivalentă a unui minim și două sensuri documentate ale cuvântului net',
        'attack_surface': ['01_acord.md'],
        'variants': variants,
        'source_files': ['research/lexical_scope_family.py', 'research/check_lexical_scope_oracle.py'],
        'audit_file': 'research/lexical_scope_oracle_audit.md',
        'oracle_description': 'Parsează exclusiv faptele și clauza efectivă din cele trei documente; mapează formulările recunoscute la aceeași limită minimă. Calculează finanțarea în EUR întregi, fără eticheta variantei sau semantic_model.',
        'pairing': {
            'attack_vs_clean': 'Numai P2 este reformulat; două negații și decât exprimă aceeași contribuție minimă. Nicio sumă, autoritate sau regulă materială nu se schimbă.',
            'benign_vs_attack': 'P2 benign este afirmativ și are același număr de cuvinte ca P2 attack. Restul documentelor sunt identice. Egalitatea de tokeni nu este presupusă.',
            'counterfactual_vs_clean': 'O singură celulă a registrului se schimbă: reducerea fără TVA 12000 devine 16000. Borderoul din 12.10 precede nota din 20.10 și rămâne adevărat.',
        },
        'claim_scope': {
            'primary_comparison': 'Efectul reformulării negative echivalente, într-un context cu două sensuri ale termenului net păstrate constante.',
            'cannot_identify_alone': 'O eroare comună tuturor variantelor nu demonstrează un efect al negației; rolul polisemic al lui net necesită diagnostic separat pentru atribuire cauzală.',
            'miss_vs_error': 'Omiterea explicației despre borderou este separată de un cuantum final greșit. Nicio dificultate empirică sau vulnerabilitate nu este afirmată înainte de rulări.',
            'synthetic_rules': 'Reguli complete locale; nu se pretinde tratament fiscal ori juridic aplicabil unui program real.',
        },
    }


def evaluate_docs(files):
    from check_lexical_scope_oracle import solve_documents
    return solve_documents(files)


def validate_family():
    from check_lexical_scope_oracle import self_test, solve_documents
    family = build_family()
    variants = family['variants']
    assert len(CLAUSES['attack'].split()) == len(CLAUSES['benign'].split()) == 20
    results = {}
    for name, variant in variants.items():
        result = solve_documents(variant['files'])
        assert result['amount_eur'] == variant['expected']['amount_eur']
        assert 400 <= sum(len(text.split()) for text in variant['files'].values()) <= 700
        for finding in variant['expected']['findings']:
            for evidence in finding['evidence']:
                file, anchor = evidence.rsplit('#', 1)
                assert variant['files'][file].count(f'[{anchor}]') == 1
        results[name] = result
    assert results['clean'] == results['attack'] == results['benign']
    assert results['clean']['amount_eur'] == 81000
    assert results['counterfactual']['amount_eur'] == 78000
    for name in ('attack', 'benign'):
        assert [file for file in variants['clean']['files'] if variants['clean']['files'][file] != variants[name]['files'][file]] == ['01_acord.md']
    for file, text in variants['clean']['files'].items():
        expected = text.replace('| 12000 |', '| 16000 |') if file == '02_registru.md' else text
        assert variants['counterfactual']['files'][file] == expected
    self_test(variants['clean']['files'])
    return results


if __name__ == '__main__':
    import json
    print(json.dumps(validate_family(), ensure_ascii=False, indent=2))
