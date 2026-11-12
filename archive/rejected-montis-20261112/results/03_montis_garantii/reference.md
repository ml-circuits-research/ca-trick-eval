# Etalon: Montis — alocarea simultană a garanțiilor

Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.

Întrebare: Refă reviewul notei Montis. Poate fi aprobat pachetul în forma actuală? Care este expunerea minimă neacoperită și ce schimbă fiecare dintre cele două oferte de garanții? Demonstrează concluziile din dosar.

Profil: simplu, mecanism nou. Mecanism principal: Fezabilitatea globală confundată cu verificări locale și cu egalitatea totalurilor; aceeași capacitate nu poate fi reutilizată.

## F1: Pachetul actual nu poate fi aprobat: N, E și V cer 120, dar singurele garanții eligibile pentru ele au împreună 100.

Probe: 01_politica.md#P1, 01_politica.md#P2, 02_registru.md#C1, 02_registru.md#G1, 03_nota.md#N1.

Deducție: Subtotalul N+E+V este 40+40+40=120. Numai GA+GB pot acoperi acest subtotal: 50+50=100. Fiecare credit poate fi acoperit luat separat, iar totalurile sunt egale, dar ambele verificări sunt insuficiente pentru acoperire simultană.

## F2: Acoperirea maximă actuală este 180, iar expunerea minimă neacoperită este 20 milioane EUR.

Probe: 01_politica.md#P2, 02_registru.md#C1, 02_registru.md#G1.

Deducție: Limita superioară este 100 pentru N/E/V plus 80 pentru S = 180. Se atinge prin GA→N 40 și E 10; GB→E 10 și V 40; GC→S 80. Rămân E 20 neacoperit și GC 20 fără utilizare eligibilă. Existența acestei alocări și limita superioară demonstrează optimul.

## F3: Garanția suplimentară de 20 exclusiv pentru S nu reduce deficitul și nu permite aprobarea.

Probe: 01_politica.md#P2, 02_registru.md#G1, 03_nota.md#N2.

Deducție: N/E/V rămân limitate la GA+GB=100 pentru cerere 120. S este deja acoperibil integral; o capacitate suplimentară numai pentru S nu ajută subtotalul deficitar. Expunerea minimă rămâne 20.

## F4: Garanția suplimentară de 20 exclusiv pentru N permite acoperirea integrală; ofertele nu sunt echivalente.

Probe: 01_politica.md#P1, 01_politica.md#P2, 02_registru.md#G1, 03_nota.md#N3.

Deducție: Alocare fezabilă completă: garanția nouă→N 20; GA→N 20 și E 30; GB→E 10 și V 40; GC→S 80. Fiecare credit este acoperit, fiecare destinație este permisă și fiecare capacitate este respectată. Deficitul devine 0, spre deosebire de oferta pentru S.

## Aspecte corecte

- Totalurile 200=200 și controalele individuale ale notei sunt aritmetic corecte.
- Garanțiile existente sunt valide și nu au alte sarcini.
- Împărțirea unei garanții între destinații eligibile este permisă; nu este permisă depășirea capacității sale.

## Evaluare

Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.
