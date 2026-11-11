# Referință: Platforma Alfa

Întrebarea de evaluare: Stabilește dacă furnizorul facturant este eligibil pentru achiziția din sediul Cluj și dacă poate fi plătit.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Certificatul nu acoperă emitentul, activitatea și sediul cerute.

Mecanisme: T03, T13.

Probe: 01_achizitie.md#A1, 02_certificat.md#C1, 02_certificat.md#C2, 03_politica.md#R1.

Demonstrație: 400100 ≠ 400101; Iași ≠ Cluj; mentenanță ≠ vânzare servere. Afilierea și numele de afișare nu transferă certificarea.

## F2: Plata nu este eligibilă chiar dacă recepția și aprobarea financiară există.

Mecanisme: T07, T10.

Probe: 01_achizitie.md#A3, 03_politica.md#R2, 03_politica.md#R3.

Demonstrație: Conjuncția include eligibilitatea, care lipsește; sinteza comercială generalizează nejustificat de la grup.

## Controale corecte

- Recepția, aprobarea financiară și aritmetica facturii sunt confirmate.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
