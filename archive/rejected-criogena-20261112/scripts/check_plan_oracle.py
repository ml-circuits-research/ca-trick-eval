#!/usr/bin/env python3
"""Independent information-set feasibility test parsed from the published table."""
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
def main():
    text=(ROOT/'eval/07_criogena_plan/02_scenarii.md').read_text()
    groups=defaultdict(list)
    for line in text.splitlines():
        cols=[x.strip() for x in line.strip('|').split('|')]
        if len(cols)==7 and cols[0] in ['S1','S2','S3']:groups[cols[2]].append(cols)
    assert sum(map(len,groups.values()))==3
    bounds={};witnesses={}
    for carrier,start in [('Aurora',3),('Boreal',5)]:
        score=0;witness={}
        for signal,rows in groups.items():
            options={pack:sum(row[start+offset]=='PASS' for row in rows) for offset,pack in enumerate(['P','A'])}
            best=max(options,key=options.get);score+=options[best];witness[signal]=best
        bounds[carrier]=score;witnesses[carrier]=witness
    expected=2 if len(groups)==2 else 3
    assert max(bounds.values())==expected
    print(f'OK: independent information-set bounds={bounds}; achievable best={expected}/3 scenarios; policies={witnesses}. No probabilities assumed.')
if __name__=='__main__':main()
