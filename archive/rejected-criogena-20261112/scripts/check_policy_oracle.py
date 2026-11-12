#!/usr/bin/env python3
"""Parse independently the displayed conditions and enumerate all possible states."""
from itertools import product
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
STATE=r'([A-Z]) este (activ|inactiv)'
def literal(code,value):return code,value=='activ'
def parse(line):
    # Return the only forbidden pair of states for the binary relation.
    states=re.findall(STATE,line)
    if line.startswith('Dacă '):
        assert len(states)==2
        (a,av),(b,bv)=map(lambda p:literal(*p),states)
        return (a,av),(b,not bv)
    if ' numai dacă ' in line:
        assert len(states)==2
        (a,av),(b,bv)=map(lambda p:literal(*p),states)
        return (a,av),(b,not bv)
    if line.startswith('Pentru ca '):
        states=re.findall(r'indicatorul ([A-Z]) să fie (activ|inactiv)',line)
        assert len(states)==2
        (a,av),(b,bv)=map(lambda p:literal(*p),states)
        return (a,av),(b,not bv)
    if line.startswith('Este exclusă combinația: '):
        assert len(states)==2
        return tuple(literal(*p) for p in states)
    if line.startswith('În orice stare validă, '):
        assert len(states)==2
        return tuple((c,not v) for c,v in map(lambda p:literal(*p),states))
    raise ValueError(line)
def main():
    folder=ROOT/'eval/06_nadir_logica'
    dossier=(folder/'01_dosar.md').read_text();rules=(folder/'02_reguli.md').read_text()
    codes=re.findall(r'^\| ([A-Z]) \|',dossier,re.M);assert len(codes)==7 and len(set(codes))==7
    conditions=[parse(line) for line in re.findall(r'^\[R\d+\] (.*)$',rules,re.M)]
    assert len(conditions)==10
    valid=[]
    for values in product([False,True],repeat=len(codes)):
        world=dict(zip(codes,values))
        if all(not all(world[c]==v for c,v in excluded) for excluded in conditions):valid.append(world)
    code,value=re.search(r'dacă și numai dacă ([A-Z]) este (activ|inactiv)',dossier).groups()
    assert valid and all(w[code]==(value=='activ') for w in valid)
    ambiguous=[c for c in codes if len({w[c] for w in valid})==2];assert ambiguous
    print(f'OK: {len(conditions)} relations parsed; {len(valid)}/128 compatible states; decisive {code}={value} in every state; ambiguous: {", ".join(ambiguous)}.')
if __name__=='__main__':main()
