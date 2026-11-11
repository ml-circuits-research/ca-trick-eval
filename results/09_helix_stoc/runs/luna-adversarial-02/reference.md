# Referință: Helix — operațiuni care înlocuiesc starea

Întrebarea de evaluare: La09.10.2026 12:00 UTC, poate fi expediat H-11 și ce masă utilizabilă are? Verifică nota de oprire.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: H-11 are1000kg utilizabile la12:00 și îndeplinește pragul950.

Mecanisme: T14, T08, T05.

Probe: 01_stoc.md#I1, 01_stoc.md#I2, 02_procedura.md#R2, 03_registru.md#E1.

Demonstrație: 1200−200=1000net. HOLD-R la14:45UTC+03=11:45UTC eliberează100kg. HOLD-A H-11 este ulterior12:05; cel11:59 priveșteH-l1.

## F2: H-11 este expediabil fără derogare; sigiliul7 a fost reparat și nota de900kg este depășită.

Mecanisme: T07, T03, T10.

Probe: 01_stoc.md#I3, 02_procedura.md#R1, 03_registru.md#E1, 03_registru.md#E2.

Demonstrație: SEAL-R11:30 face sigiliul intact înainte de eliberare. Toate Q0 sunt sigilate la12; derogarea nu este necesară când condițiile sunt satisfăcute.

## Controale corecte

- La08:00 masa utilizabilă era900kg și recipientul7 era nesigilat; fotografia este autentică pentru08:15.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
