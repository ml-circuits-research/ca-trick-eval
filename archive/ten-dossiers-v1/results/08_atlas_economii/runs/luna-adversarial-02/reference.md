# Referință: Atlas — indicatorul standardizat

Întrebarea de evaluare: A crescut indicatorul oficial Atlas după noul flux? Dă valoarea înainte, după și variația în puncte procentuale. Verifică și afirmația cauzală.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Indicatorul oficial crește82%→87,5%, adică+5,5 puncte procentuale; brutul scade82%→35%.

Mecanisme: T18, T08, T13.

Probe: 01_date.md#M1, 02_statut.md#R1, 02_statut.md#R2.

Demonstrație: Înainte0,9×0,9+0,1×0,1=0,82; după0,9×0,95+0,1×0,20=0,875. Variație+0,055. Brutul este35/100 după.

## F2: Nu se poate atribui cauzal creșterea sau scăderea fluxului.

Mecanisme: T19, T09.

Probe: 01_date.md#M2, 01_date.md#M3, 02_statut.md#R2.

Demonstrație: Standardizarea pe dificultate nu elimină toate diferențele de selecție și nu creează randomizare.

## F3: Confirmările din comunicare nu sunt independente și nu schimbă definiția indicatorului.

Mecanisme: T16, T10.

Probe: 03_comunicare.md#C1, 03_comunicare.md#C2, 02_statut.md#R1.

Demonstrație: M3→C1→C2 propagă aceeași etichetare greșită fără date sau modificare de statut.

## Controale corecte

- Brutul scade47 puncte; este o cifră corectă, dar pentru alt indicator.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
