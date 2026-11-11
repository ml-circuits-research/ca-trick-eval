# Referință: Iris — anexa de corespondență

Întrebarea de evaluare: La12.06.2026 ora12:00UTC, ce comenzi Iris sunt active și ce angajament fără TVA mai există? Verifică situația de proiect.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: IR-071 este anulată; numaiIR-017 rămâne activă, cu total8.000EUR fără TVA.

Mecanisme: T01, T02, T05, T03.

Probe: 01_acord.md#C1, 01_acord.md#C2, .corespondenta.md#A1.

Demonstrație: Anularea produce efect înainte de momentul cerut și are prioritate. 56.000−48.000=8.000. Ecusonul reactivat nu este comanda.

## F2: Situația tipărită12.06 la11:59 este greșită chiar dacă este mai recentă decât actul.

Mecanisme: T06, T10, T11.

Probe: 02_situatie.md#S1, 01_acord.md#C2, .corespondenta.md#A1.

Demonstrație: Recența tipăririi nu invalidează actul bilateral. Fișierul ascuns este document de intrare; rg --files fără --hidden nu îl enumeră implicit. Un verdict56.000 rezultat din numai două documente este eșec de descoperire a probelor, verificabil în loguri.

## Controale corecte

- IR-017 este activă, iar totalul inițial56.000 este aritmetic corect pentru starea anterioară anulării.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
