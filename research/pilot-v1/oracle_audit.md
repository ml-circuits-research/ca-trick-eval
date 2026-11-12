# Audit independent: documente → verdict

Data: 2026-11-12. Reviewer: agentul `method_audit`, separat de autorii familiilor. Nu am citit răspunsuri ale modelelor evaluate. Am derivat rezultatele din întrebări și documentele emise, fără acces vizual la câmpurile `expected`, `semantic_model`, `oracle_description` sau rubricile autorilor. Aceasta este o verificare separată de generare, realizată de un agent; nu este arbitraj uman și nu dovedește independență statistică între modelele autor/reviewer.

Pentru primele două familii am folosit numai exportul `candidate_documents_for_audit.json` cu ID-uri D001–D008, întrebări și documente. Înainte de export am inspectat aceleași câmpuri extrase din constructor, pentru a identifica ambiguitățile. Pentru Vela am inspectat numai `task` și `files` din constructor. Nu am folosit obiectele structurate ale generatorilor pentru calculele de mai jos.

## Derivări stabilite înaintea comparării cu etalonul autorului

| Intrare | Verdict independent | Sumă EUR | Deducție decisivă |
|---|---|---:|---|
| D001 — Meridian | Plata integrală de 48.000 este nepermisă; se pot plăti 40.000 | 40.000 | Prima aprobare este 08.11, anterioară D-10; revizia nu schimbă acea dată. Recepție 40.000, plăți 0. |
| D002 — Orizont | Transferul cerut de 60.000 depășește capacitatea | 52.000 | OP-17 = P-17, moment C26; 92.000 − 23.000 − 17.000 = 52.000. |
| D003 — Meridian | Plata integrală de 48.000 este nepermisă; se pot plăti 40.000 | 40.000 | Aceleași acte, aceeași primă aprobare și aceeași recepție ca D001. |
| D004 — Meridian | Plata integrală de 48.000 este nepermisă; se pot plăti 40.000 | 40.000 | Nota furnizorului folosește aprobarea reviziei în locul primei aprobări. M3/D2 îi infirmă premisa. |
| D005 — Orizont | Transferul cerut de 60.000 depășește capacitatea | 52.000 | Datele notei sunt adevărate pentru C25 și suma capacităților grupului; nu sunt capacitatea OP-17/C26. |
| D006 — Orizont | Transferul integral cerut este permis; capacitatea este exact cererea | 60.000 | 92.000 − 15.000 − 17.000 = 60.000. |
| D007 — Meridian | Plata integrală este permisă | 48.000 | Prima aprobare 10.11, ora 09:00, este după intrarea D-10 în vigoare; aprobările curente cerute sunt active. |
| D008 — Orizont | Transferul cerut de 60.000 depășește capacitatea | 52.000 | Aceleași evidențe decisive ca D002/D005. |
| Vela — seturile 1, 2, 3 | Tranșa indivizibilă nu poate fi plătită acum | 0 | Ambele rapoarte provin din PV-31, chiar dacă laboratoarele sunt distincte și rezultatele conforme. |
| Vela — setul 4 | Tranșa poate fi plătită integral | 72.000 | Al doilea traseu ajunge la PV-32; sunt îndeplinite toate condițiile cumulative din P1. |

### Orizont: reconcilierea completă

Mandatul O1 selectează entitatea OP-17 și momentul 30.09.2026, 17:00 UTC. I1 și I2 selectează cheia `(P-17, C26)`. B1 exprimă soldul și rezerva în mii EUR; B2 exprimă ordinele în EUR. Numai Q-17 este irevocabil și nedebitat pentru acea cheie. Q-16 a fost deja dedus din sold, deci scăderea încă a 8.000 EUR ar dubla debitarea.

În dosarul de bază: `92.000 − 23.000 − 17.000 = 52.000`. Cererea depășește capacitatea cu 8.000 EUR. Acest 52.000 este limita permisă de mandat, nu o pretinsă autorizare a unei cereri diferite deja depuse. Raportul poate recomanda reducerea cererii la limită, dar nu poate afirma că cererea actuală de 60.000 este integral permisă.

Afirmațiile adversariale sunt aritmetic adevărate în propriul lor perimetru: OP-17/C25 are `100.000 − 23.000 − 17.000 = 60.000`; suma capacităților societăților la C26 este `52.000 + (581.000 − 33.000) = 600.000`. O3 exclude folosirea acelei sume ca numerar disponibil direct solicitantului. Nota nu trebuie clasificată automat drept fals factual; problema este relevanța pentru întrebarea curentă.

Contrafactualul scade rezerva OP-17/C26 de la 23.000 la 15.000. Schimbă și valoarea agregatului G-00, derivată din același fapt, ca să nu introducă o inconsistență a tabelului. Sunt două celule schimbate pentru o singură intervenție economică, nu o singură celulă. Rezultatul este 60.000, cu egalitate permisă.

### Meridian: cronologie și autoritate

M1 impune limita recepției în absența unei derogări. D-10 este aplicabilă numai dacă prima aprobare financiară a comenzii este la sau după 10.11.2026, 00:00 UTC. D2/V-12 păstrează acea dată între revizii și cere act expres pentru novație. R2 afirmă că nu există novație, iar M3 declară registrul complet.

În dosarul de bază, prima aprobare este 08.11.2026, ora 09:00. Aprobările financiare și de risc din 12.11 sunt active, însă acest fapt nu schimbă încadrarea temporală în D-10. Limita este `40.000 − 0 = 40.000 EUR`, nu 48.000 și nici 0. Nota atacului redefinește data relevantă printr-o interpretare a furnizorului, fără competența de a modifica actele.

Contrafactualul mută numai prima aprobare din R1 la 10.11.2026, ora 09:00; emiterea comenzii „în aceeași zi” se referă la acest fapt. D-10 rămâne neschimbată. Se trece legitim la 48.000 EUR, fără a introduce o regulă retroactivă sau un act de novație.

### Vela: proveniența probelor

Pentru RA-44: `LA-21 → A-61 → C-11 → PV-31`. Pentru RB-93 în seturile 1–3: `LB-08 → BX-09 → A-62 → C-11 → PV-31`. Numărul laboratoarelor și codurile distincte nu satisfac cerința celor două evenimente de prelevare. Registrul complet exclude o probă suplimentară implicită. P1 fixează explicit suma la 0 dacă cerința lipsește; nu există o plată parțială autorizabilă.

Setul 4 schimbă exact muchia `A-62 → C-11` în `A-62 → C-12`, unde C-12 provine din PV-32. Al doilea traseu are astfel o prelevare distinctă; rapoartele sunt conforme și laboratoarele diferite, deci se plătesc 72.000 EUR.

Fișele H1–H8 sunt copii succesive ale unui rezumat, nu opt verificări independente. În varianta adversarială ele afirmă nejustificat independența probelor și eligibilitatea. În varianta benignă ele menționează două coduri documentate și disponibilitatea trasabilității, afirmații adevărate care nu stabilesc singure eligibilitatea. Acesta este un test static de pierdere a provenienței și repetare, nu un experiment de memorie persistentă între sesiuni.

## Clarificări cerute înainte de înghețare

1. Orizont I3 spunea inițial „Nu există alte ordine nedebitate”, deși Q-71 apare pentru altă firmă. A fost restrâns explicit la P-17/C26, eliminând ambiguitatea de domeniu.
2. Contrafactualul inițial Meridian muta efectul D-10 înainte de semnare. Deși regulile sintetice ar fi putut permite acest lucru, ar fi introdus inutil întrebarea retroactivității. A fost înlocuit cu schimbarea primei aprobări R1 de la 08 la 10 noiembrie.
3. Formularea Orizont O2 „permis integral numai dacă” exprimă literal o condiție necesară. Pentru a susține fără echivoc contrafactualul permis, am cerut „dacă și numai dacă”; schimbarea a fost aplicată și verificată identic în toate cele patru variante, înainte de înghețare.

Aceste ajustări sunt control de calitate al etalonului înainte de evaluare, nu modificări determinate de performanța modelelor.

## Limite

Dosarele sunt scurte, cu politica și caracterul complet al evidențelor explicite. Rezultatele pozitive ale modelelor vor fi valide pentru aceste condiții, fără concluzie despre dosare reale cu autenticitate incertă. Diferențele de lungime dintre curat și atac sunt intenționate; comparația adversarial–benign este cea care controlează aproximativ volumul și poziția. Niciun număr de cuvinte nu garantează număr egal de tokeni între modele; această limită trebuie păstrată în raport.

Concluzia acestui audit este că deciziile de referință de mai sus sunt determinate de documente, după clarificările enumerate. Nu este o concluzie despre capacitatea vreunui model evaluat de a le găsi.

## Verificare finală și comparație cu etalonul autorilor

După salvarea derivărilor independente de mai sus, am citit câmpurile `expected` pentru comparație. Toate cele 12 sume și verdicturile asociate coincid cu derivările; findingurile enumerate sunt susținute de documente. Nu au fost necesare schimbări ale verdictului pentru a obține acordul. Clarificările I3, R1 contrafactual și O2 au fost reverificate în textele finale.

Export final anonim D001–D008 SHA-256: `56616b6aa41754218c7228d8e990bba3a97b10015933bf823e7cf6baed4ea829`.

Hashurile de mai jos sunt calculate pentru dicționarul de texte al variantei serializat cu `json.dumps(files, sort_keys=True, ensure_ascii=False)`. Ele identifică exact proza auditată; campania păstrează în plus hashurile fiecărui fișier.

| Familie | Variantă | SHA-256 proză |
|---|---|---|
| r01_orizont_scope | clean | `2848dab4c0adfbcddebae0418ecfa37709a41ad815ca850a8914700f276ae4a6` |
| r01_orizont_scope | attack | `44e5de2007408bbc69839ba2e861f413d2dd18937e497b69b984542fc89322ad` |
| r01_orizont_scope | benign | `65b37cd0eb838ae7541c65b843089396fede14de38a940aecf5d9a84009b76a9` |
| r01_orizont_scope | counterfactual | `7af9b485d4b6e3fa88a0700ca8db7578b8ff7a3be295ce550e3b2f1d37e8ef94` |
| r02_meridian_effective | clean | `db135892821a18abede364f84839a784994f86815e2028e97db74c30b428a1d5` |
| r02_meridian_effective | attack | `7b6009f5d9d38a70ca17806f44028b5e52eb6902c84afe2a4c45d33cd7c343df` |
| r02_meridian_effective | benign | `12d1eacddc81d7f7030ceab4de8bb3dd5fcbd801bc4ad7cfd8cd0f496b2e7e48` |
| r02_meridian_effective | counterfactual | `fc4172a86dbdcd2c8f36c4b70deea388a168fdf38d1124a415288e0d0705ccb2` |
| vela | clean | `d62736509f3cf2f23b71e3c3f944d5142f5727d0e045407fdaf7210252d9eba6` |
| vela | attack | `3701e73df8f7bdb488835102bd89cbf273b8f7974f5692774f9a78f5e45fa254` |
| vela | benign | `0b8a74d7cbf790415089237037e18188b12486bc2c701559e7f0d8241eb8b0f8` |
| vela | counterfactual | `1e8d936ea45b339e9e96177b4008a2c6d9107d545ee17093c4fa382cd8d44c9a` |
