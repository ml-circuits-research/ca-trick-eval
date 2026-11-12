#!/usr/bin/env python3
"""Generate active blind-review dossiers; preserve runs and archives."""
import json
from pathlib import Path
from cases import build
ROOT=Path(__file__).resolve().parents[1]

def main():
    cases=build()
    manifest=[]
    for c in cases:
        folder=ROOT/'eval'/c['id']; folder.mkdir(parents=True,exist_ok=True)
        for name,body in c['documents'].items():
            (folder/name).parent.mkdir(parents=True,exist_ok=True)
            (folder/name).write_bytes(body if isinstance(body,bytes) else body.encode('utf-8'))
        manifest.append({k:v for k,v in c.items() if k!='documents'}|{'files':list(c['documents'])})
        out=ROOT/'results'/c['id']; out.mkdir(parents=True,exist_ok=True)
        lines=[f'# Etalon: {c["title"]}','','Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.','',f'Întrebare: {c["task"]}','','Profil: '+c['profile']+'. Mecanism principal: '+c['primary_mechanism'],'']
        for f in c['findings']:
            lines += [f'## {f["id"]}: {f["claim"]}','','Probe: '+', '.join(f['evidence'])+'.','','Deducție: '+f['proof'],'']
        lines += ['## Aspecte corecte','']+['- '+x for x in c['correct']]
        lines += ['','## Evaluare','','Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.','']
        (out/'reference.md').write_text('\n'.join(lines))
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Generated {len(cases)} dossiers, {sum(len(c["documents"]) for c in cases)} files, {sum(len(c["findings"]) for c in cases)} findings.')
if __name__=='__main__': main()
