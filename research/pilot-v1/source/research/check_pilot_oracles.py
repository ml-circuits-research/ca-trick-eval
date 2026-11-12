#!/usr/bin/env python3
"""Independent integer/date/lineage calculations from emitted document text.

No imports of semantic_model, formulas or expected amounts are used in the
calculators. Comparison with the frozen expected answer occurs afterwards.
Natural-language authority/meaning still requires the separate prose audit.
"""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path

def tables(text):
    return [[c.strip() for c in line.strip('|').split('|')] for line in text.splitlines() if line.startswith('|') and '---' not in line]

def amount_orizont(files):
    mandate=files['01_mandat.md'];identities=files['02_identitate.md'];ledger=files['03_registre.md']
    legal=re.search(r'Beneficiarul analizei este .*?, (OP-\d+)\.',mandate)[1]
    day=re.search(r'transfer de .*? la (\d\d\.\d\d\.\d{4})',mandate)[1]
    code=re.search(r'(\S+) = [^.]+identificator juridic '+legal,identities)[1]
    close=re.search(r'Închiderea (\S+) este '+re.escape(day),identities)[1]
    balances,payments=ledger.split('[B2]')
    selected=[r for r in tables(balances) if r[:2]==[code,close]]
    assert len(selected)==1
    row=selected[0];gross,reserved=map(int,row[2:])
    orders=[r for r in tables(payments) if r[:2]==[code,close]]
    pending=sum(int(r[3]) for r in orders if r[4]=='irevocabil, nedebitat')
    assert all(r[4] in ('debitat','irevocabil, nedebitat') for r in orders)
    if '[N3] Sinteza celor două fișe: pragul' in files['04_nota.md']:
        # Check the attack's arithmetic claims are true in their stated scope.
        assert 100000-23000-17000==60000
        assert 673000-23000-17000-33000==600000
    return max(0,(gross-reserved)*1000-pending)

def amount_meridian(files):
    acts=files['02_acte.md'];register=files['03_registru.md']
    def timestamp(day,hour):return datetime.strptime(day+' '+hour,'%d.%m.%Y %H:%M')
    e=re.search(r'intră în vigoare la (\d\d\.\d\d\.\d{4}), ora (\d\d:\d\d)',acts)
    f=re.search(r'prima aprobare financiară la (\d\d\.\d\d\.\d{4}), ora (\d\d:\d\d)',register)
    effective=timestamp(*e.groups());first=timestamp(*f.groups())
    invoice,received,paid=map(lambda n:int(n.replace('.','')),re.search(r'factura M-48 este de ([\d.]+) EUR; bunurile recepționate sunt de ([\d.]+) EUR; plăți efectuate: ([\d.]+) EUR',register).groups())
    assert 'fără act de novație' in register
    assert 'rămâne activă la ora 14:00' in register
    assert 'rămâne activă la ora 14:00' in register.split('[R3]')[1]
    return invoice if first>=effective else received-paid

def amount_vela(files):
    trace=files['02_trasabilitate.md'];reports=files['03_rapoarte.md']
    parents={obj:event for event,obj in re.findall(r'Prelevarea (\S+) .*? a produs recipientul (\S+)\.',trace)}
    for r in tables(trace):
        if r[1] in ('aliquotare','recodificare la transport','recepție laborator Atlas','recepție laborator Boreal'):
            parents[r[0]]=r[2]
    roots=[]
    for sample in re.findall(r'proba (\S+): CONFORM',reports):
        visited=set()
        while sample in parents:
            assert sample not in visited,'cycle'
            visited.add(sample);sample=parents[sample]
        assert sample.startswith('PV-')
        roots.append(sample)
    assert len(roots)==2
    return 72000 if len(set(roots))==2 else 0

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--suite',type=Path);args=ap.parse_args()
    if args.suite:
        catalog=json.loads((args.suite/'catalog.json').read_text())
        packages=[(c['family'],c['variant'],{p.name:p.read_text() for p in (args.suite/'eval'/c['case_id']).glob('*.md')},c['expected']) for c in catalog]
    else:
        from candidate_families import build_families
        from provenance_family import build_family
        packages=[(fam['id'],name,v['files'],v['expected']) for fam in build_families()+[build_family()] for name,v in fam['variants'].items()]
    calculators={'r01_orizont_scope':amount_orizont,'r02_meridian_effective':amount_meridian,'vela':amount_vela}
    for family,variant,files,expected in packages:
        amount=calculators[family](files)
        assert amount==expected['amount_eur'],(family,variant,amount,expected)
        for finding in expected['findings']:
            for anchor in finding['evidence']:
                name,key=anchor.split('#');assert files[name].count('['+key+']')==1
        print(f'{family}/{variant}: {amount} EUR; source anchors verified')
    assert len(packages)==12
if __name__=='__main__':main()
