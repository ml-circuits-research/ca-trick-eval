# Referință: Iris — registrul cu două ceasuri

Întrebarea de evaluare: Pentru IR-071 și IR-017, la 12.06.2026 ora 12:00 UTC, stabilește statutul și totalul angajamentelor fără TVA. Verifică sinteza de control.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Ambele comenzi sunt active; totalul este 56.000 EUR.

Mecanisme: T01, T02, T03, T05, T07.

Probe: 01_contracte.md#C1, 01_contracte.md#C2, 02_registru.md#E1, 02_registru.md#E2.

Demonstrație: IR-071: X09:00 apoi A11:00, ambele sig2. Ultimul efect valabil este A. IR-017: X cu sig1 nu produce efect. Evenimentul B nu atinge O. 48.000+8.000=56.000.

## F2: Sinteza de 8.000 EUR ordonează greșit importurile și atribuie e12 obiectului greșit.

Mecanisme: T06, T10, T16.

Probe: 03_control.md#S1, 03_control.md#S2, 01_contracte.md#C3.

Demonstrație: e12 este O, nu B; effective_at precede imported_at ca regulă de stare. Copierea S1 în extras nu validează rezultatul.

## Controale corecte

- IR-017 este activă; sinteza o clasifică corect.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
