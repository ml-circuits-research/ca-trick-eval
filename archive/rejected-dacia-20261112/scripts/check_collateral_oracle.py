#!/usr/bin/env python3
"""Independent max-flow and subset certificates, parsed from dossier tables."""
from collections import deque
from itertools import combinations
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]

def maxflow(loans,guarantees):
    residual={}
    def edge(a,b,amount):
        residual.setdefault(a,{})[b]=amount
        residual.setdefault(b,{})[a]=0
    for name,(cap,eligible) in guarantees.items():
        edge('source',name,cap)
        for loan in eligible: edge(name,loan,sum(loans.values()))
    for loan,amount in loans.items(): edge(loan,'sink',amount)
    total=0
    while True:
        parents={'source':None};queue=deque(['source'])
        while queue and 'sink' not in parents:
            a=queue.popleft()
            for b,cap in residual[a].items():
                if cap>0 and b not in parents: parents[b]=a;queue.append(b)
        if 'sink' not in parents: return total
        b='sink';amount=sum(loans.values())
        while parents[b] is not None:
            a=parents[b];amount=min(amount,residual[a][b]);b=a
        b='sink'
        while parents[b] is not None:
            a=parents[b];residual[a][b]-=amount;residual[b][a]+=amount;b=a
        total+=amount

def verify(loans,guarantees,allocation):
    used={g:0 for g in guarantees};covered={loan:0 for loan in loans}
    for guarantee,loan,amount in allocation:
        assert amount>=0 and loan in guarantees[guarantee][1]
        used[guarantee]+=amount;covered[loan]+=amount
    assert all(used[g]<=cap for g,(cap,_) in guarantees.items())
    assert all(covered[loan]<=cap for loan,cap in loans.items())
    return sum(covered.values())

def main():
    text=(ROOT/'eval/03_montis_garantii/02_registru.md').read_text()
    loans={};guarantees={}
    for line in text.splitlines():
        cols=[c.strip() for c in line.strip('|').split('|')]
        if len(cols)!=3: continue
        if cols[0] in ['N','E','V','S']: loans[cols[0]]=int(cols[2])
        if re.fullmatch(r'G[A-Z]',cols[0]): guarantees[cols[0]]=(int(cols[1]),set(cols[2].split(', ')))
    assert len(loans)==4 and len(guarantees)==3
    note=(ROOT/'eval/03_montis_garantii/03_nota.md').read_text()
    amount=int(re.search(r'garanție nouă de (\d+)',note)[1])
    for extra,target in [(False,None),(True,'S'),(True,'N')]:
        gs=guarantees|({'NEW':(amount,{target})} if extra else {})
        optimum=maxflow(loans,gs)
        worst_deficit=0
        for size in range(1,len(loans)+1):
            for subset in combinations(loans,size):
                demand=sum(loans[x] for x in subset)
                adjacent=sum(cap for cap,eligible in gs.values() if set(subset)&eligible)
                worst_deficit=max(worst_deficit,demand-adjacent)
        assert sum(loans.values())-optimum==worst_deficit
        expected=200 if target=='N' else 180
        assert optimum==expected
        witness=([('NEW','N',20),('GA','N',20),('GA','E',30),('GB','E',10),('GB','V',40),('GC','S',80)] if target=='N' else [('GA','N',40),('GA','E',10),('GB','E',10),('GB','V',40),('GC','S',80)])
        assert verify(loans,gs,witness)==optimum
        print(f'OK: extra={target or "none"}, max covered={optimum}, min uncovered={worst_deficit}; max-flow, exhaustive subset bound and witness agree.')
if __name__=='__main__':main()
