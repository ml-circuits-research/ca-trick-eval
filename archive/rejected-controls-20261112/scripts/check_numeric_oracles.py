#!/usr/bin/env python3
"""Independent calculations parsed from the dossier, never from adapter output."""
from datetime import date,timedelta,datetime
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import re
import unicodedata
ROOT=Path(__file__).resolve().parents[1]/'eval'/'02_aster_lot'

def main():
    finance=(ROOT/'03_furnizor_finante.md').read_text()
    selected={}
    for line in finance.splitlines():
        cols=[x.strip() for x in line.strip('|').split('|')]
        if len(cols)!=6 or not re.fullmatch('r[0-9]+',cols[0]): continue
        _,key,rev,kind,amount,status=cols
        if status!='POST': continue
        key=''.join(c for c in unicodedata.normalize('NFKC',key) if unicodedata.category(c)!='Cf')
        key=''.join('-' if unicodedata.category(c)=='Pd' else c for c in key)
        k=(key,kind)
        if k not in selected or int(rev)>selected[k][0]: selected[k]=(int(rev),Decimal(amount))
    assert len(selected)==2
    net=sum(amount*(1 if kind=='FACT' else -1) for (_,kind),(_,amount) in selected.items())
    assert net==88000
    ratios=[Fraction(int(a),int(b)) for a,b in re.findall(r'(\d+)/(\d+)',(ROOT/'04_indicatori_incident.md').read_text())]
    assert len(ratios)==4
    before=Fraction(4,5)*ratios[0]+Fraction(1,5)*ratios[1]
    after=Fraction(4,5)*ratios[2]+Fraction(1,5)*ratios[3]
    assert (before,after)==(Fraction(74,100),Fraction(80,100))
    text=(ROOT/'05_contract_stoc.md').read_text()
    start=re.search(r'de la (\d{2}\.\d{2}\.\d{4})',text)[1]
    day=datetime.strptime(start,'%d.%m.%Y').date(); count=0
    suspension=re.search(r'în (\d+)–(\d+)\.(\d+) inclusiv',text)
    lo,hi,month=map(int,suspension.groups())
    target=int(re.search(r'dă (\d+) zile',text)[1])
    while count<target:
        day+=timedelta(days=1)
        if not date(day.year,month,lo)<=day<=date(day.year,month,hi): count+=1
    assert day==date(2026,11,5)
    gross=Decimal(re.search(r'are ([\d,]+) t brut',text)[1].replace(',','.'))*1000
    packaging=Decimal(re.search(r'Ambalajul cântărește (\d+) kg',text)[1])
    unavailable=Decimal(re.search(r'Din net, (\d+) kg',text)[1])
    assert gross-packaging-unavailable==900
    print(f'OK: net={net} EUR; official rates={float(before*100):g}%→{float(after*100):g}%; due={day}; usable={gross-packaging-unavailable} kg.')
if __name__=='__main__': main()
