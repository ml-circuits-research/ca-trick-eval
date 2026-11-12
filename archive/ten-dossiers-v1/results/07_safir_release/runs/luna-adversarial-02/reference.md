# Referință: Safir — token independent și joncțiuni de registru

Întrebarea de evaluare: Este autorizată lansarea Safir la10.10.2026 10:00 UTC? Reconciliază statusul cu registrele semnate.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: La10:00 testul aplicabil abc210 este PASS; FAIL de10:05 nu se aplică retrospectiv.

Mecanisme: T05, T13, T15.

Probe: 01_politica.md#R1, 01_politica.md#R2, 02_registre.md#Q1.

Demonstrație: prelim_v3 privește digestul corect și produce efect09:45; final_v13 este viitor față de10:00. Eticheta prelim nu îl invalidează.

## F2: APR-201 pe abc210/K8 este activ; revocarea K7 stinge APR-210, nu APR-201.

Mecanisme: T20, T03, T07.

Probe: 02_registre.md#Q2, 02_registre.md#Q3, 01_politica.md#R1.

Demonstrație: Cheia tokenului APR-201 esteK8, valabilă la momentul cerut. Există cel puțin un token activ; nu trebuie să fie toate active.

## F3: Lansarea este autorizată la10:00; statusul de oprire este greșit.

Mecanisme: T14, T10, T11.

Probe: 01_politica.md#R2, 03_status.md#S1, 02_registre.md#Q1, 02_registre.md#Q2.

Demonstrație: Fereastra se încheie09:30UTC; PASS09:45 și tokenK8 satisfac restul condițiilor. Statusul confundă eticheta cu versiunea și folosește un eveniment ulterior.

## Controale corecte

- K7 este revocată și APR-210 este invalid; acestea nu sunt singurele căi de autorizare.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
