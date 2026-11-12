#!/usr/bin/env python3
"""Narrow document-derived integer oracle for the synthetic Rovina family.

Accepted wording is explicit, never guessed from a variant ID. This parser
does not establish semantic equivalence; a separate prose audit must do that.
"""
from fractions import Fraction
import re


def single(pattern, text, label, flags=0):
    matches = re.findall(pattern, text, flags)
    assert len(matches) == 1, f'Missing or ambiguous {label}'
    return matches[0]


def minimum_percent(policy):
    clause = single(r'^\[P2\] (.+)$', policy, 'contribution clause', re.MULTILINE)
    patterns = (
        r'Contribuția proprie trebuie să reprezinte cel puțin (\d+)% din valoarea netă a proiectului\.',
        r'Nu este admisă decât o contribuție proprie care să nu fie mai mică de (\d+)% din valoarea netă a proiectului\.',
        r'În cadrul acordului, contribuția proprie a beneficiarului trebuie să reprezinte cel puțin (\d+)% din valoarea netă calculată pentru acest proiect\.',
    )
    matches = [re.fullmatch(pattern, clause) for pattern in patterns]
    matches = [match for match in matches if match is not None]
    assert len(matches) == 1, 'Unsupported contribution scope: separate prose interpretation required'
    percent = int(matches[0].group(1))
    assert 0 <= percent <= 100, 'Invalid contribution percentage'
    return percent


def maximum_grant(net_eur, own_percent):
    assert type(net_eur) is int and net_eur >= 0
    assert type(own_percent) is int and 0 <= own_percent <= 100
    # G + C = N; C >= p*N/100; integer G is therefore floor((100-p)*N/100).
    grant = net_eur * (100 - own_percent) // 100
    exact_minimum_own = Fraction(net_eur * own_percent, 100)
    assert Fraction(net_eur - grant) >= exact_minimum_own
    if grant < net_eur:
        assert Fraction(net_eur - (grant + 1)) < exact_minimum_own
    return grant


def solve_documents(files):
    policy = files['01_acord.md']
    ledger = files['02_registru.md']
    settlement = files['03_borderou.md']
    assert 'finanțarea maximă permisă' in policy
    assert 'acoperă împreună exact valoarea netă a proiectului' in policy
    assert 'Sunt permise sume de finanțare parțiale, exprimate în EUR întregi.' in policy
    assert 'suma bazelor fără TVA ale facturilor eligibile, diminuată cu bazele fără TVA ale reducerilor de preț confirmate prin note de credit' in policy
    assert 'Comisioanele de încasare sunt cheltuieli administrative în afara acestor servicii.' in policy
    assert 'baze fără TVA, în EUR, nu în mii de EUR' in ledger
    assert 'acceptată definitiv de ambele părți' in ledger
    invoice, vat_rate = single(r'^\| 08\.10\.2026 \| RV-318 \| Factură servicii \| (\d+) \| (\d+)% \|$', ledger, 'invoice in EUR', re.MULTILINE)
    credit, credit_rate = single(r'^\| 20\.10\.2026 \| NC-318 \| Reducere de preț \| (\d+) \| (\d+)% \|$', ledger, 'credit in EUR', re.MULTILINE)
    invoice, vat_rate, credit, credit_rate = map(int, (invoice, vat_rate, credit, credit_rate))
    assert vat_rate == credit_rate == 20
    assert 0 <= credit <= invoice
    assert 'la 12.10.2026' in settlement and 'după reținerea comisionului din încasarea brută' in settlement
    amounts = {}
    for label in ('Brut încasat', 'Comision reținut', 'Net'):
        amounts[label] = int(single(r'^\| ' + re.escape(label) + r' \| (\d+) \|$', settlement, label, re.MULTILINE))
    assert invoice * (100 + vat_rate) == amounts['Brut încasat'] * 100
    assert amounts['Brut încasat'] - amounts['Comision reținut'] == amounts['Net']
    percent = minimum_percent(policy)
    net = invoice - credit
    grant = maximum_grant(net, percent)
    return {
        'invoice_ex_vat_eur': invoice, 'credit_ex_vat_eur': credit, 'eligible_net_eur': net,
        'minimum_own_percent': percent, 'own_eur_at_maximum_grant': net - grant,
        'amount_eur': grant, 'historical_gross_receipt_eur': amounts['Brut încasat'],
        'historical_processing_fee_eur': amounts['Comision reținut'],
        'historical_net_transfer_eur': amounts['Net'],
    }


def self_test(clean_files):
    baseline = solve_documents(clean_files)
    assert baseline['eligible_net_eur'] == 108000 and baseline['amount_eur'] == 81000
    # Boundary and integer-unit cases: exact equality is admissible; the next
    # grant EUR violates the own-contribution floor. Never round floats.
    for net, percent, expected in ((108000, 25, 81000), (104000, 25, 78000),
                                   (101, 25, 75), (100, 25, 75), (3, 25, 2),
                                   (1, 25, 0), (0, 25, 0), (101, 0, 101), (101, 100, 0)):
        assert maximum_grant(net, percent) == expected
        feasible = [g for g in range(net + 1) if Fraction(net - g) >= Fraction(net * percent, 100)]
        assert expected == max(feasible)
    changed = dict(clean_files)
    changed['02_registru.md'] = changed['02_registru.md'].replace('| 12000 |', '| 16000 |')
    assert solve_documents(changed)['amount_eur'] == 78000
    # The historical cash transfer may change without changing the current
    # contract base, provided its own accounting identity remains valid.
    changed = dict(clean_files)
    changed['03_borderou.md'] = changed['03_borderou.md'].replace('| 8000 |', '| 9000 |').replace('| 136000 |', '| 135000 |')
    assert solve_documents(changed)['amount_eur'] == 81000
    for old, new in (('cel puțin 25%', 'cel mult 25%'),
                     ('cel puțin 25%', 'cel puțin 25 puncte de bază'),
                     ('baze fără TVA, în EUR, nu în mii de EUR', 'baze fără TVA, în mii de EUR')):
        changed = {name: text.replace(old, new) for name, text in clean_files.items()}
        try:
            solve_documents(changed)
        except AssertionError:
            pass
        else:
            raise AssertionError('Unsupported scope or unit was silently accepted')


if __name__ == '__main__':
    import json
    from lexical_scope_family import validate_family
    print(json.dumps(validate_family(), ensure_ascii=False, indent=2))
