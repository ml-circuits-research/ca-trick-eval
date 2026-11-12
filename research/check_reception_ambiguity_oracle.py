#!/usr/bin/env python3
"""Enumerate the locally supported contractual readings, without variant labels.

This is a fixture-specific formal checker. A separate prose audit must establish
that the two interpretations are plausible; enumeration alone cannot do that.
The administrative note is not a source of contractual authority.
"""
import argparse
import json
from pathlib import Path
import re


def one(pattern, text):
    matches = re.findall(pattern, text, re.M)
    assert len(matches) == 1, f'Expected one match for {pattern!r}'
    return matches[0]


def solve_documents(files):
    contract = files['01_contract.md']
    records = files['02_registre.md']
    amount = int(one(r'\[C2\] Tranșa de (\d+) EUR devine plătibilă după recepția documentelor de proiect\.', contract))
    assert 'Tranșa nu se fracționează; înaintea acestui eveniment contractual nu este plătibilă.' in contract
    assert 'Celelalte condiții de plată sunt îndeplinite' in contract
    assert 'Numai un act adițional semnat de reprezentanții ambelor părți poate completa clauzele contractului.' in contract
    assert 'fără a modifica clauzele' in contract
    assert 'Pachetul cuprinde toate înscrisurile contractuale semnate' in contract
    assert 'se aplică exclusiv regulile consemnate aici' in contract
    a1 = one(r'^\[A1\] (.+)$', records)
    t1 = one(r'^\[T1\] (.+)$', records)
    assert 'rubrica «Recepție documente»' in a1 and 'rubrica «Recepție documente»' in t1
    assert 'înregistrează primirea administrativă' in a1
    assert 'înregistrează acceptarea conținutului' in t1
    assert 'Lot D-17: PRIMIT' in a1
    assert 'Lot D-17: ÎN CURS' in t1 and 'acceptarea tehnică nu a fost emisă' in t1
    assert 'Nu există o altă înregistrare de primire sau de acceptare tehnică' in records
    facts = {'administrative_receipt': True, 'technical_acceptance': False}
    c4 = one(r'^\[C4\] (.+)$', contract)
    if c4 == 'Evidența actelor adiționale semnate: niciun act adițional.':
        definition = None
        interpretations = ['administrative_receipt', 'technical_acceptance']
    else:
        assert c4.startswith('Act adițional semnat de ambele părți la 10.11.2026, aplicabil tranșei DP-17: ')
        meaning = c4.split('în clauza C2, recepția documentelor înseamnă exclusiv ', 1)
        assert len(meaning) == 2
        if meaning[1] == 'primirea înregistrată de registratură, fără a fi necesară acceptarea tehnică.':
            definition = 'administrative_receipt'
        elif meaning[1] == 'acceptarea conținutului de comisia tehnică; simpla primire la registratură nu îndeplinește această condiție.':
            definition = 'technical_acceptance'
        else:
            raise AssertionError('Unreviewed contractual definition')
        interpretations = [definition]
    models = []
    for interpretation in interpretations:
        occurred = facts[interpretation]
        models.append({
            'contractual_interpretation': interpretation,
            'facts': dict(facts),
            'contractual_event_has_occurred': occurred,
            'amount_eur': amount if occurred else 0,
            'consistency': 'same factual records; only the interpretation of C2 differs when C4 has no definition',
        })
    outcomes = sorted({model['amount_eur'] for model in models})
    determined = len(outcomes) == 1
    return {
        'contractual_definition': definition,
        'decision_status': 'determined' if determined else 'underdetermined',
        'amount_eur': outcomes[0] if determined else None,
        'conditional_amounts_eur': [] if determined else outcomes,
        'models': models,
        'note_used_as_authority': False,
        'operational_hold_is_contractual_zero': False,
        'limitation': 'The two locally evidenced senses and their contractual plausibility require independent prose audit; the formal checker does not prove linguistic ambiguity.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    args = parser.parse_args()
    if args.input:
        files = {name: (args.input / name).read_text(encoding='utf-8') for name in ('01_contract.md', '02_registre.md')}
        print(json.dumps(solve_documents(files), ensure_ascii=False, indent=2))
    else:
        from reception_ambiguity_family import validate_family
        print(json.dumps(validate_family(), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
