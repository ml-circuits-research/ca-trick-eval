# Etalon: Nadir — concluzie certă din informații indirecte

Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.

Întrebare: Refă reviewul notei Nadir. Poate fi stabilită autorizabilitatea tranșei NI-6 din documentele disponibile, sau este într-adevăr nedeterminată? Demonstrează concluzia și verifică afirmația comitetului fără presupuneri despre valori nepublicate.

Profil: scurt, raționament deductiv. Mecanism principal: Incertitudinea asupra valorilor individuale este confundată cu imposibilitatea unei concluzii certe implicate de toate stările compatibile.

## F1: Starea decisivă este certă: B este inactiv, deși valoarea nu este afișată explicit.

Probe: 01_dosar.md#P3, 02_reguli.md#I1, 02_reguli.md#R1, 02_reguli.md#R2, 02_reguli.md#R5, 02_reguli.md#R6, 02_reguli.md#R7, 02_reguli.md#R9, 02_reguli.md#R10.

Deducție: Presupunem că B este activ. B este activ → S este inactiv prin R2; S este inactiv → D este inactiv prin R9; D este inactiv → J este activ prin R10; J este activ → E este activ prin R1; E este activ → C este inactiv prin R7; C este inactiv → V este inactiv prin R6; V este inactiv → B este inactiv prin R5. Rezultă B este inactiv, contradicție cu presupunerea. Deci B este inactiv în orice stare compatibilă. Verificare independentă: toate cele 4 stări compatibile dintre 128 au aceeași valoare a indicatorului decisiv.

## F2: Tranșa este autorizabilă conform singurului criteriu; nota greșește când o declară nedeterminată.

Probe: 01_dosar.md#P1, 01_dosar.md#P2, 01_dosar.md#P5, 03_nota.md#N1, 03_nota.md#N2, 02_reguli.md#R1, 02_reguli.md#R2, 02_reguli.md#R5, 02_reguli.md#R6, 02_reguli.md#R7, 02_reguli.md#R9, 02_reguli.md#R10.

Deducție: F1 demonstrează B este inactiv; P2 este o echivalență, deci autorizabilitatea rezultă. Nu deducem o plată deja executată.

## Aspecte corecte

- Lipsesc valorile explicite individuale; faptul este real, dar nu exclude deducția.
- Regulile sunt consistente: există stări compatibile, nu deducem o concluzie din contradicția întregului dosar.
- Nu se afirmă că transferul bancar a fost efectuat.

## Evaluare

Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.
