#!/usr/bin/env python3
"""Atria oracle: parse published documents, then use two interval algorithms.

This checks the specified synthetic document format, not arbitrary contract
language. Independent review of the prose-to-model interpretation is still
required before freezing a campaign. No notes or expected answers are inputs
to either algorithm.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re


DATE_PATTERN = r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}'


def date(text):
    return datetime.strptime(text, '%d.%m.%Y %H:%M').replace(tzinfo=timezone.utc)


def timestamp(value):
    return value.isoformat().replace('+00:00', 'Z')


def hours(delta):
    seconds = delta.days * 86400 + delta.seconds
    assert not delta.microseconds
    assert seconds % 3600 == 0, 'This fixture uses exact whole hours.'
    return seconds // 3600


def parse_documents(files):
    policy = files['01_contract.md']
    register = files['02_certificate.md']
    window = re.search(r'de la (' + DATE_PATTERN + r') până la (' + DATE_PATTERN + r')', policy)
    assert window, 'Required work window is missing or malformed.'
    amount = re.search(r'Tranșa AT-72 pentru proiectul Atria este de (\d+) EUR\.', policy)
    assert amount, 'Tranche amount is missing.'
    # These explicit assertions bind the fixed parser to the intended rule.
    # They do not replace the separate audit of the natural-language policy.
    assert 'în fiecare moment al ferestrei' in policy
    assert '[început, final)' in policy
    assert 'suma autorizabilă este 0 EUR; tranșa este indivizibilă' in policy
    assert 'Suprapunerile sunt permise, dar nu compensează lipsa acoperirii în alt moment.' in policy
    intervals = []
    for line in register.splitlines():
        row = re.fullmatch(r'\|\s*([A-Z][A-Z0-9_-]*)\s*\|\s*(' + DATE_PATTERN + r')\s*\|\s*(' + DATE_PATTERN + r')\s*\|', line)
        if row:
            name, start, end = row.groups()
            intervals.append((name, date(start), date(end)))
    assert intervals and len({name for name, _, _ in intervals}) == len(intervals)
    assert all(start < end for _, start, end in intervals)
    start, end = map(date, window.groups())
    assert start < end
    return start, end, int(amount.group(1)), intervals


def union_sweep(start, end, intervals):
    clipped = sorted((max(start, left), min(end, right)) for _, left, right in intervals
                     if max(start, left) < min(end, right))
    merged = []
    for left, right in clipped:
        if merged and left <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], right))
        else:
            merged.append((left, right))
    gaps, cursor = [], start
    for left, right in merged:
        if cursor < left:
            gaps.append((cursor, left))
        cursor = right
    if cursor < end:
        gaps.append((cursor, end))
    return {
        'covered_hours': sum(hours(right - left) for left, right in merged),
        'gap_hours': sum(hours(right - left) for left, right in gaps),
        'sum_certificate_hours_in_window': sum(hours(right - left) for left, right in clipped),
        'gaps': [[timestamp(left), timestamp(right)] for left, right in gaps],
        'merged': [[timestamp(left), timestamp(right)] for left, right in merged],
    }


def elementary_segments(start, end, intervals):
    # Independent second method: check every elementary time segment directly.
    # No union_sweep result or merging function is used here.
    boundaries = {start, end}
    for _, left, right in intervals:
        if start < left < end:
            boundaries.add(left)
        if start < right < end:
            boundaries.add(right)
    boundaries = sorted(boundaries)
    segments = []
    for left, right in zip(boundaries, boundaries[1:]):
        active = [name for name, cert_start, cert_end in intervals if cert_start <= left and cert_end >= right]
        segments.append({'start': timestamp(left), 'end': timestamp(right),
                         'hours': hours(right - left), 'certificates': active})
    return {
        'covered_hours': sum(s['hours'] for s in segments if s['certificates']),
        'gap_hours': sum(s['hours'] for s in segments if not s['certificates']),
        'overlap_hours': sum(s['hours'] * max(0, len(s['certificates']) - 1) for s in segments),
        'segments': segments,
    }


def solve_documents(files):
    start, end, tranche, intervals = parse_documents(files)
    sweep = union_sweep(start, end, intervals)
    segmented = elementary_segments(start, end, intervals)
    assert sweep['covered_hours'] == segmented['covered_hours']
    assert sweep['gap_hours'] == segmented['gap_hours']
    assert sweep['covered_hours'] + sweep['gap_hours'] == hours(end - start)
    assert (sweep['sum_certificate_hours_in_window'] - sweep['covered_hours']
            == segmented['overlap_hours'])
    full = sweep['gap_hours'] == 0
    return {
        'window_hours': hours(end - start),
        'sum_certificate_hours': sweep['sum_certificate_hours_in_window'],
        'covered_hours': sweep['covered_hours'], 'gap_hours': sweep['gap_hours'],
        'overlap_hours': segmented['overlap_hours'], 'gaps': sweep['gaps'],
        'verdict': 'payable' if full else 'not_payable', 'amount_eur': tranche if full else 0,
        'union_sweep': sweep, 'elementary_segments': segmented['segments'],
        'algorithms_agree': True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Read a rendered case directory; do not import the authoring model.')
    args = parser.parse_args()
    if args.input:
        files = {name: (args.input / name).read_text() for name in ['01_contract.md', '02_certificate.md']}
        print(json.dumps(solve_documents(files), ensure_ascii=False, indent=2))
    else:
        from interval_family import validate_family
        results = validate_family()
        for name, result in results.items():
            print(f'{name}: {result["covered_hours"]}/{result["window_hours"]} hours covered; '
                  f'gap {result["gap_hours"]}h; overlap {result["overlap_hours"]}h; '
                  f'authorized {result["amount_eur"]} EUR; both algorithms agree.')


if __name__ == '__main__':
    main()
