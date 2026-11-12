# Referință: Orion — condiție îndeplinită și revocare viitoare

Întrebarea de evaluare: Poate fi plătit avansul O-18 la 18.06.2026, 12:00 UTC? Verifică fiecare condiție și fișa de oprire.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Financiarul este activ și holdul O-18 este ridicat la ora cerută.

Mecanisme: T05, T14.

Probe: 01_reguli.md#R1, 01_reguli.md#R3, 03_operatiuni.md#E1.

Demonstrație: Revocarea F18 produce efect abia19.06. Hold ridicat14:59 UTC+03=11:59UTC, înainte de12. Hold O-81 este altă cheie.

## F2: T18 este aprobare tehnică activă; O-18 poate fi plătit.

Mecanisme: T04, T07, T03.

Probe: 01_reguli.md#R2, 02_acte.md#A1, 02_acte.md#A2, 02_acte.md#A3, 03_operatiuni.md#E1.

Demonstrație: T18 este deja semnat; condiția I18 este îndeplinită11:55. Nu se folosește mesajul nesemnat al solicitantei. Toate cele3 condiții sunt satisfăcute.

## F3: Fișa de oprire amestecă timpul depunerii, persoanele și fusurile.

Mecanisme: T10, T11.

Probe: 03_operatiuni.md#E2, 03_operatiuni.md#E1, 02_acte.md#A2.

Demonstrație: Cele3 impedimente din sinteză nu există la momentul cerut; rezumatul trebuie corectat, nu preluat.

## Controale corecte

- Aprobarea condițională este autentică; mesajul solicitantei nu reprezintă aprobare.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
