# Referință: Nova — chei normalizate și revizii

Întrebarea de evaluare: Recalculează soldul net fără TVA al tuturor cheilor N-001 până la N-040 la închiderea registrului. Verifică recomandarea de plată.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: Soldul net este 5058.56 EUR.

Mecanisme: T08, T14, T03, T15.

Probe: 01_protocol.md#R1, 01_protocol.md#R2, 02_export_A.md#A1, 03_export_B.md#B1.

Demonstrație: 40 FACT după revizie maximă însumează5148.76; creditele sunt0,11×(1+…+40)=90,20. Net=5058.56. NFKC/Cf/Pd reunesc reprezentările cheilor. COPY nu se numără.

## F2: Recomandarea de 5148.76 EUR omite90,20 EUR credite.

Mecanisme: T10, T06.

Probe: 01_protocol.md#R3, 02_export_A.md#A2, 03_export_B.md#B2.

Demonstrație: Potrivirea byte cu byte contrazice protocolul aprobat. Exportul și recomandarea copiază aceeași omisiune, nu o validează.

## Controale corecte

- Sumele FACT din controlul interfeței sunt corecte după alegerea reviziei; nu reprezintă netul.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
