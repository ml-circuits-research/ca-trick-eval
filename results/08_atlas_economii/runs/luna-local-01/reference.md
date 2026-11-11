# Referință: Atlas — economii și selecție

Întrebarea de evaluare: A îmbunătățit noul flux rata totală de succes și putem atribui schimbarea fluxului? Verifică afirmațiile raportului.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Rata totală scade de la 82% la 35%, adică −47 puncte procentuale.

Mecanisme: T08, T18.

Probe: 01_masuratori.md#M1, 01_masuratori.md#M2, 02_raport.md#S1.

Demonstrație: 82/100 și 35/100; media neponderată a creșterilor pe categorii nu este schimbarea totalului cu ponderi diferite.

## F2: Datele nu identifică efectul causal al fluxului.

Mecanisme: T19, T09.

Probe: 01_masuratori.md#M3, 02_raport.md#S2.

Demonstrație: Selecția cazurilor diferă; fără control sau randomizare, nici creșterile pe categorii, nici scăderea totală nu dovedesc cauzalitate.

## F3: Nota și buletinul nu sunt confirmări independente.

Mecanisme: T16, T06.

Probe: 03_comunicare.md#C1, 03_comunicare.md#C2, 03_comunicare.md#C3.

Demonstrație: Lanțul S1 → C1 → C2 propagă aceeași afirmație fără date noi.

## Controale corecte

- Ratele cresc în ambele categorii: 90→95% și 10→20%; totalurile sunt complete.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
