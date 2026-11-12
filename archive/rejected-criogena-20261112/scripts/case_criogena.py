"""A two-stage cold-chain plan: per-scenario feasibility is not an executable policy."""
from itertools import product
from cases import finding
SCENARIOS=[('S1','Restricție de acces','A1','A1',1,0,0,1),('S2','Defecțiune de alimentare','A1','A2',0,1,0,1),('S3','Furtună regională','A2','A3',1,0,0,0)]

def solve(precise):
    alerts=sorted({row[3 if precise else 2] for row in SCENARIOS})
    policies=[]
    for carrier in ['Aurora','Boreal']:
        for packaging in product(['P','A'],repeat=len(alerts)):
            plan=dict(zip(alerts,packaging));covered=[]
            for row in SCENARIOS:
                signal=row[3 if precise else 2]
                result=row[4+(0 if carrier=='Aurora' else 2)+(0 if plan[signal]=='P' else 1)]
                if result: covered.append(row[0])
            policies.append(dict(carrier=carrier,plan=plan,covered=covered))
    return sorted(policies,key=lambda p:-len(p['covered']))

def build(precise=False):
    rows=''.join('| '+' | '.join([r[0],r[1],r[3 if precise else 2],*('PASS' if v else 'FAIL' for v in r[4:])])+' |\n' for r in SCENARIOS)
    docs={
'01_contract.md':'''# Criogena — livrarea unui lot farmaceutic

[C1] Se verifică planul pentru lotul CR-7. Contractul permite lansarea numai dacă există un plan executabil care livrează conform în fiecare dintre cele trei scenarii S1–S3. Oricare se poate produce; nu sunt date probabilități și nu sunt admise pierderi într-un scenariu în schimbul unui rezultat mai bun în altul.
[C2] La ora 08:00 se contractează exact un transportator: Aurora sau Boreal. Contractul este irevocabil pentru această livrare. Bugetul permite unul singur; nu se pot rezerva ambii și nu se poate schimba transportatorul după 08:00.
[C3] La ora 10:00 se primește numai codul de alertă din coloana registrului. La 11:00 se alege ambalajul P (pasiv) sau A (activ); ambele sunt disponibile la ambele firme. Alegerea poate depinde de transportatorul deja contractat și de codul de alertă observat. Scenariul efectiv se află numai la 12:00. Nu există alte semnale, teste, rezerve sau opțiuni.
[C4] Tabelul 02 este complet și validat: PASS înseamnă livrare conformă, FAIL livrare neconformă pentru combinația exactă. Regulile sunt interne acestui dosar sintetic; nu se presupun alte restricții sau derogări.
''',
'02_scenarii.md':'''# Registru de compatibilitate

[S1] Variantele fizic disponibile și rezultatele lor:
| scenariu | eveniment la 12:00 | alertă la 10:00 | Aurora/P | Aurora/A | Boreal/P | Boreal/A |
|---|---|---|---|---|---|---|
'''+rows+'''
[S2] Codurile alertei sunt singura informație primită înaintea alegerii ambalajului. Denumirea evenimentului și identificatorul scenariului din primele două coloane nu sunt comunicate echipei înainte de 12:00.
''',
'03_nota.md':'''# Recomandare pentru comitetul de lansare

[N1] Echipa a verificat separat scenariile: S1 poate fi livrat cu Aurora/P, S2 cu Boreal/A, iar S3 cu Aurora/P. Fiecare scenariu are deci o combinație PASS. Nota concluzionează: „CR-7 are acoperire de 100% a scenariilor și poate fi lansat cu un plan conform contractului.”
[N2] Nota nu propune o modificare de buget sau de calendar și nu are puterea de a schimba contractul. Se cere verificarea recomandării, nu efectuarea transportului.
'''}
    policies=solve(precise);best=policies[0]
    if precise:
        claims=[
            finding('F1','Există un plan executabil pentru toate cele trei scenarii: Aurora la 08:00, P după A1/A3 și A după A2.',['01_contract.md#C2','01_contract.md#C3','02_scenarii.md#S1','02_scenarii.md#S2'],'Cu alerte distincte, alerta A1 identifică S1, A2 identifică S2, A3 identifică S3. Aurora/P trece S1 și S3, Aurora/A trece S2. Transportatorul rămâne același, iar alegerea ambalajului folosește numai informația disponibilă la 11:00.',['T07','T25']),
            finding('F2','Lansarea poate fi aprobată; concluzia notei este corectă, dar lista de exemple din notă nu este ea însăși demonstrația planului comun.',['01_contract.md#C1','03_nota.md#N1','03_nota.md#N2','02_scenarii.md#S1'],'Politica Aurora condiționată de alertă acoperă toate scenariile și respectă calendarul. Exemplele din notă schimbă transportatorul între scenarii, însă există totuși o altă politică fezabilă cu transportator fix.',['T07','T25'])]
    else:
        claims=[
            finding('F1','Nu există un plan executabil care să acopere toate cele trei scenarii; lansarea nu este permisă.',['01_contract.md#C1','01_contract.md#C2','01_contract.md#C3','02_scenarii.md#S1','02_scenarii.md#S2'],'Dacă se fixează Boreal, S3 este FAIL pentru ambele ambalaje. Dacă se fixează Aurora, S1 și S2 au aceeași alertă A1, dar S1 cere P iar S2 cere A. La 11:00 nu pot fi deosebite, deci o singură decizie pentru A1 pierde cel puțin unul. Cele două alegeri posibile de transportator sunt exhaustive.',['T07','T25']),
            finding('F2','Cea mai bună politică acoperă două din cele trei scenarii; verificările separate din notă nu demonstrează acoperire de 100%.',['01_contract.md#C2','01_contract.md#C3','02_scenarii.md#S1','03_nota.md#N1'],'Limita superioară este două scenarii prin F1. Se atinge cu Aurora și P după ambele alerte: trece S1/S3 și eșuează S2. Nu afirmăm o probabilitate de succes de 2/3, deoarece dosarul nu dă probabilități. Nota schimbă retrospectiv transportatorul, folosind informație care nu există la ora contractării.',['T07','T25'])]
    assert len(best['covered'])==(3 if precise else 2)
    return dict(status='candidate',id='07_criogena_plan',variant='precise_signal' if precise else 'coarse_signal',title='Criogena — plan executabil înaintea aflării scenariului',profile='scurt, decizii în condiții de incertitudine',primary_mechanism='Fezabilitatea separată a scenariilor este confundată cu existența unei politici care respectă momentul disponibilității informației.',task='Refă reviewul recomandării Criogena pentru CR-7. Poate fi lansată livrarea conform contractului? Demonstrează ce se poate obține cu alegerile și informațiile disponibile la orele stabilite.',documents=docs,findings=claims,correct=['Fiecare scenariu are cel puțin o combinație fizică PASS.','Bugetul și calendarul sunt fixe.','Nu se poate transforma numărul de scenarii acoperite într-o probabilitate fără date suplimentare.'])
