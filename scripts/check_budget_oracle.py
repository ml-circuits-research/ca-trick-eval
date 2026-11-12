#!/usr/bin/env python3
"""Independent integer-currency oracle and reproduction of the stated IEEE calculation."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
    folder=ROOT/'eval/08_lintea_buget'
    policy=(folder/'01_mandat.md').read_text();rows=(folder/'02_registru.md').read_text()
    budget=int(re.search(r'Bugetul aprobat este de ([\d.]+) EUR',policy)[1].replace('.',''))
    amounts=[int(x.replace('.','')) for x in re.findall(r'^\| L\d+ \|[^|]+\| ([\d.]+) \|',rows,re.M)]
    assert len(amounts)==3 and sum(amounts)==budget==100000
    reported=0.0
    for amount in amounts:reported+=amount/1000
    assert reported>budget/1000 and f'{reported:.2f}'==f'{budget/1000:.2f}'
    print(f'OK: integer total={sum(amounts)} EUR <= {budget}; floating total={reported!r} kEUR > {budget/1000!r}; display hides only the implementation error.')
if __name__=='__main__':main()
