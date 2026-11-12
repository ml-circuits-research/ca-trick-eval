#!/usr/bin/env python3
"""Compare original document identifiers exactly; never normalize or fold them."""
import argparse
from itertools import zip_longest
import json
from pathlib import Path
import re
import unicodedata


def one(pattern, text):
    matches = re.findall(pattern, text)
    assert len(matches) == 1, f'Expected exactly one match for {pattern!r}'
    return matches[0]


def describe(character):
    if character is None:
        return None
    return {'character': character, 'codepoint': f'U+{ord(character):04X}',
            'unicode_name': unicodedata.name(character, 'UNNAMED')}


def solve_documents(files):
    mandate = files['01_mandat.md']
    approval = files['02_aprobare.md']
    # Captures preserve every codepoint inside the literal reference value.
    # No strip(), ASCII encoding, case folding or Unicode normalization is used.
    requested = one(r'\[M1\] Identificator dosar: `([^`]+)`\.', mandate)
    approved = one(r'\[R1\] Referință dosar: `([^`]+)`\.', approval)
    requested_amount = int(one(r'Factura L-48 are valoarea de (\d+) EUR\.', mandate))
    approved_amount = int(one(r'Valoare aprobată: (\d+) EUR\.', approval))
    requested_beneficiary = one(r'Beneficiarul plății este Litera Instrumente SRL, identificator ([^.]+)\.', mandate)
    approved_beneficiary = one(r'Beneficiar: Litera Instrumente SRL, identificator ([^.]+)\.', approval)
    assert 'identificatorul exact al dosarului' in mandate
    assert 'dacă și numai dacă există o aprobare financiară activă' in mandate
    assert 'suma autorizabilă este 0 EUR; nu se autorizează o plată parțială' in mandate
    assert 'este activă la ora 14:00' in approval
    assert 'Documentul este autentic și nu a fost revocat.' in approval
    reference_matches = requested == approved
    beneficiary_matches = requested_beneficiary == approved_beneficiary
    amount_matches = requested_amount == approved_amount
    payable = reference_matches and beneficiary_matches and amount_matches
    differences = [{'position_1_based': index, 'requested': describe(left), 'approved': describe(right)}
                   for index, (left, right) in enumerate(zip_longest(requested, approved), 1) if left != right]
    return {
        'requested_reference': requested, 'approved_reference': approved,
        'requested_utf8_hex': requested.encode('utf-8').hex(),
        'approved_utf8_hex': approved.encode('utf-8').hex(),
        'reference_matches_exactly': reference_matches,
        'reference_differences': differences,
        'beneficiary_matches': beneficiary_matches, 'amount_matches': amount_matches,
        'approval_active': True,
        'amount_eur': requested_amount if payable else 0,
        'verdict': 'payable' if payable else 'not_payable',
        'comparison': 'original strings, without normalization',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    args = parser.parse_args()
    if args.input:
        files = {name: (args.input / name).read_text() for name in ['01_mandat.md', '02_aprobare.md']}
        print(json.dumps(solve_documents(files), ensure_ascii=False, indent=2))
    else:
        from identity_confusable_family import validate_family
        for name, result in validate_family().items():
            print(f'{name}: {result["amount_eur"]} EUR; exact match={result["reference_matches_exactly"]}; '
                  f'approved UTF-8={result["approved_utf8_hex"]}')


if __name__ == '__main__':
    main()
