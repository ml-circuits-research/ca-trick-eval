#!/usr/bin/env python3
"""Independent calculations from the generated evidence, not from receipts."""
from datetime import date, timedelta, datetime, timezone
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import re
import unicodedata

ROOT=Path(__file__).resolve().parents[1]
def documents(case):
    return '\n'.join(p.read_text() for p in sorted((ROOT/'eval'/case).glob('*.md')) if p.name!='AGENTS.md')

def nova():
    selected={}
    for line in documents('05_nova_facturi').splitlines():
        cols=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cols)!=6 or not re.fullmatch(r'L\d{3}[a-d]',cols[0]): continue
        _,key,revision,kind,amount,status=cols
        if status!='POST': continue
        key=''.join(ch for ch in unicodedata.normalize('NFKC',key) if unicodedata.category(ch)!='Cf')
        key=''.join('-' if unicodedata.category(ch)=='Pd' else ch for ch in key)
        pair=(key,kind)
        if pair not in selected or int(revision)>selected[pair][0]:
            selected[pair]=(int(revision),Decimal(amount))
    assert len(selected)==80
    fact=sum(v for (k,t),(r,v) in selected.items() if t=='FACT')
    credit=sum(v for (k,t),(r,v) in selected.items() if t=='CREDIT')
    assert fact==Decimal('5148.76') and credit==Decimal('90.20')
    assert fact-credit==Decimal('5058.56')
    print(f'Nova: FACT={fact}, CREDIT={credit}, net={fact-credit} EUR.')

def atlas():
    text=documents('08_atlas_economii')
    ratios=[Fraction(int(a),int(b)) for a,b in re.findall(r'(\d+)/(\d+)',text)]
    assert len(ratios)==4
    before=Fraction(9,10)*ratios[0]+Fraction(1,10)*ratios[1]
    after=Fraction(9,10)*ratios[2]+Fraction(1,10)*ratios[3]
    assert before==Fraction(82,100) and after==Fraction(875,1000)
    print(f'Atlas: {float(before*100):g}% -> {float(after*100):g}%, change={float((after-before)*100):g}pp.')

def meridian():
    text=documents('04_meridian_contract')
    assert '30 zile calendaristice' in text and '10,11,12,13,14 iulie inclusiv' in text
    day=date(2026,7,1); counted=0
    while counted<30:
        day+=timedelta(days=1)
        if not date(2026,7,10)<=day<=date(2026,7,14): counted+=1
    assert day==date(2026,8,5)
    print(f'Meridian: day30 after the signed suspension={day.isoformat()}.')

def iris():
    text=documents('01_port_iris'); states={'IR-071':True,'IR-017':True}
    amounts={'IR-071':48000,'IR-017':8000}
    events=[]
    for line in text.splitlines():
        cols=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cols)!=7 or not re.fullmatch(r'e\d+',cols[0]): continue
        eid,kind,key,op,effective,imported,signatures=cols
        moment=datetime.fromisoformat(effective.replace('Z','+00:00'))
        if kind=='O' and signatures=='2' and moment<=datetime(2026,6,12,12,tzinfo=timezone.utc):
            events.append((moment,key,op))
    for _,key,op in sorted(events): states[key]=op=='A'
    total=sum(amounts[key] for key,active in states.items() if active)
    assert states=={'IR-071':True,'IR-017':True} and total==56000
    print(f'Iris: {states}, total={total} EUR.')

if __name__=='__main__':
    iris(); meridian(); nova(); atlas()
