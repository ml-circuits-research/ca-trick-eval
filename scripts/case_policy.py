"""Business control invariants with exhaustive truth-table reference answers."""
import json
from collections import deque
from pathlib import Path
from cases import finding
NAMES={1:('B','blocaj de proces'),2:('J','validare juridică'),3:('C','validare de colateral'),4:('D','derogare procedurală'),5:('E','analiză extinsă'),6:('S','validare de securitate'),7:('V','verificare manuală')}

def state(literal):
    return NAMES[abs(literal)][0]+(' este activ' if literal>0 else ' este inactiv')

def worlds(spec):
    return [mask for mask in range(1<<spec['n']) if all(any(bool(mask&(1<<(abs(lit)-1)))==(lit>0) for lit in clause) for clause in spec['clauses'])]

def proof(spec):
    graph={i:[] for i in [*range(1,spec['n']+1),*range(-spec['n'],0)]}
    for index,(a,b) in enumerate(spec['clauses']):
        graph[-a].append((b,index+1));graph[-b].append((a,index+1))
    target=spec['target'];queue=deque([(-target,[])]);seen={-target}
    while queue:
        at,path=queue.popleft()
        if at==target:return path
        for to,index in graph[at]:
            if to not in seen:seen.add(to);queue.append((to,path+[(at,to,index)]))
    raise ValueError('No contradiction certificate')

def build():
    root=Path(__file__).resolve().parent
    configuration=json.loads((root/'active_policy.json').read_text())
    seed=configuration['seed'];style=configuration.get('style','plain')
    spec=next(s for s in json.loads((root/'policy_candidates.json').read_text()) if s['seed']==seed)
    valid=worlds(spec);target=spec['target'];required=state(target)
    assert valid and all(bool(w&(1<<(abs(target)-1)))==(target>0) for w in valid)
    rules=[]
    for index,(a,b) in enumerate(spec['clauses'],1):
        premise=state(-a);conclusion=state(b)
        if style=='business':
            variant=(index-1)%5
            if variant==0: text=f'Dacă {premise}, atunci {conclusion}.'
            elif variant==1: text=f'{premise} numai dacă {conclusion}.'
            elif variant==2:
                pa,pv=premise.split(' este ');co,cv=conclusion.split(' este ')
                text=f'Pentru ca indicatorul {pa} să fie {pv}, este necesar ca indicatorul {co} să fie {cv}.'
            elif variant==3: text=f'Este exclusă combinația: {premise} și {state(-b)}.'
            else: text=f'În orice stare validă, {state(a)} sau {state(b)}; cel puțin una dintre cele două afirmații este adevărată.'
        else: text=f'Dacă {premise}, atunci {conclusion}.'
        rules.append(f'[R{index}] '+text)
    docs={
'01_dosar.md':f'''# Nadir Invest — controlul unei tranșe de investiții

[P1] La 12.11.2026, ora 12:00 UTC, se verifică autorizarea tranșei NI-6 de 50.000 EUR. Nu există alte tranșe, aprobări necesare, plăți sau condiții financiare în acest dosar sintetic.
[P2] Protocolul stabilește că tranșa este autorizabilă dacă și numai dacă {required}. Acesta este singurul criteriu. „Autorizabilă” descrie îndeplinirea condiției, nu afirmă că un transfer bancar a fost executat.
[P3] Indicatorii sunt binari: activ sau inactiv. Valorile individuale au fost eliminate din exportul pentru comitet. Responsabilul de date confirmă că registrul actual satisface simultan toate relațiile din 02_reguli.md.
[P4] Dicționarul indicatorilor:
| cod | indicator |
|---|---|
'''+''.join(f'| {code} | {name} |\n' for code,name in NAMES.values())+'''
[P5] Se aplică exclusiv regulile interne ale acestui dosar. Nu se presupun aprobări, cerințe sau evenimente externe.
''',
'02_reguli.md':'''# Invariantele registrului Nadir

[I1] Relațiile de integritate ale registrului la data de referință:

'''+ '\n\n'.join(rules)+'\n',
'03_nota.md':f'''# Notă pentru comitet — tranșa NI-6

[N1] Exportul nu afișează direct stările individuale ale indicatorilor. Nota susține: „Nu se poate stabili din dosar dacă {required}; autorizabilitatea tranșei rămâne nedeterminată. NI-6 nu poate fi declarată autorizabilă pe baza acestui pachet.”
[N2] Nota nu invocă alte blocaje sau condiții în afara protocolului. Se cere verificarea concluziei, nu efectuarea transferului.
'''}
    certificate=proof(spec)
    steps='; '.join(f'{state(a)} → {state(b)} prin R{rule}' for a,b,rule in certificate)
    statement=f'Presupunem că {state(-target)}. {steps}. Rezultă {state(target)}, contradicție cu presupunerea. Deci {required} în orice stare compatibilă. Verificare independentă: toate cele {len(valid)} stări compatibile dintre {1<<spec["n"]} au aceeași valoare a indicatorului decisiv.'
    refs=[f'02_reguli.md#R{i}' for i in sorted({r for _,_,r in certificate})]
    return dict(status='retained_luna_proof_error' if seed==735 and style=='business' else 'candidate',id='06_nadir_logica',variant=f'seed-{seed}-{style}',seed=seed,title='Nadir — concluzie certă din informații indirecte',profile='scurt, raționament deductiv',
        primary_mechanism='Incertitudinea asupra valorilor individuale este confundată cu imposibilitatea unei concluzii certe implicate de toate stările compatibile.',
        task='Verifică nota pentru comitetul Nadir și stabilește dacă tranșa NI-6 de 50.000 EUR este autorizabilă la momentul cerut. Prezintă findingurile materiale și probele lor.',documents=docs,
        findings=[
            finding('F1',f'Starea decisivă este certă: {required}, deși valoarea nu este afișată explicit.',['01_dosar.md#P3','02_reguli.md#I1',*refs],statement,['T07','T09','T17','T24']),
            finding('F2','Tranșa este autorizabilă conform singurului criteriu; nota greșește când o declară nedeterminată.',['01_dosar.md#P1','01_dosar.md#P2','01_dosar.md#P5','03_nota.md#N1','03_nota.md#N2',*refs],f'F1 demonstrează {required}; P2 este o echivalență, deci autorizabilitatea rezultă. Nu deducem o plată deja executată.',['T07','T09','T24'])],
        correct=['Lipsesc valorile explicite individuale; faptul este real, dar nu exclude deducția.','Regulile sunt consistente: există stări compatibile, nu deducem o concluzie din contradicția întregului dosar.','Nu se afirmă că transferul bancar a fost efectuat.'])
