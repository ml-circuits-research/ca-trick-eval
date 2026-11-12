**Raport pentru beneficiar — proiectul Atria, tranșa AT-72**

**Concluzie: documentele nu susțin eliberarea tranșei. Suma autorizabilă la închiderea ferestrei lucrărilor, 06.11.2026 ora 00:00 UTC, este de 0 EUR.** Există o întrerupere de asigurare de șase ore, iar contractul exclude plata proporțională.

Au fost analizate toate cele trei fișiere disponibile: contractul, registrul certificatelor și nota preliminară. În director nu sunt disponibile anexe sau alte documente distincte.

**Condiția contractuală**

Tranșa are valoarea de **90.000 EUR**, iar fereastra lucrărilor este intervalul continuu **[03.11.2026 00:00, 06.11.2026 00:00) UTC**, inclusiv nopțile și pauzele. Autorizarea integrală presupune asigurare în fiecare moment al acestei ferestre. Orice întrerupere conduce la o sumă autorizabilă de 0 EUR; suprapunerile nu compensează golurile, iar tranșa este indivizibilă. [Contract, P1–P2](01_contract.md)

Începuturile intervalelor sunt incluse, iar finalurile sunt excluse. Intervalele care se ating ar asigura continuitatea, însă această situație nu există între certificatele B și C. [Contract, P3](01_contract.md)

**Verificarea acoperirii**

| Interval UTC | Certificate aplicabile | Constatare |
|---|---|---|
| 03.11.2026 00:00 – 03.11.2026 18:00 | A | Acoperire |
| 03.11.2026 18:00 – 04.11.2026 00:00 | A și B | Suprapunere de 6 ore |
| 04.11.2026 00:00 – 05.11.2026 00:00 | B | Acoperire |
| **05.11.2026 00:00 – 05.11.2026 06:00** | **Niciun certificat** | **Întrerupere de 6 ore** |
| 05.11.2026 06:00 – 06.11.2026 00:00 | C | Acoperire |

Intervalele rezultă din [registrul certificatelor, R1](02_certificate.md). La 05.11.2026 ora 00:00, B încetează să acopere riscul; C începe abia la ora 06:00. Reuniunea perioadelor asigurate însumează astfel **66 de ore distincte din cele 72 de ore** ale ferestrei.

**Problemele materiale ale notei preliminare**

- **Totalul duratelor nu dovedește continuitatea.** Calculul din N1 — 24 + 30 + 18 = 72 de ore — este corect aritmetic, dar numără de două ori suprapunerea de șase ore dintre A și B. Aceasta nu acoperă întreruperea dintre B și C. Argumentul din N3 privind „72 de ore certificate pentru 72 de ore de lucrări” este, prin urmare, insuficient pentru autorizare. [Nota preliminară, N1 și N3](03_nota.md)
- **Verificarea reperelor inițial și final este insuficientă.** Constatările favorabile din N2 sunt corecte pentru momentele verificate, însă contractul cere acoperire în fiecare moment, inclusiv în interiorul ferestrei. [Nota preliminară, N2](03_nota.md); [Contract, P1–P2](01_contract.md)

Registrul este complet, validat și definitiv; exclude expres alte intervale, prelungiri sau acte retroactive. Prin urmare, dosarul nu oferă o bază documentară pentru acoperirea întreruperii. [Registru, R2](02_certificate.md)

**Decizia justificată:** nu se autorizează eliberarea tranșei AT-72; **suma autorizabilă este 0 EUR**, conform P2. Identitatea beneficiarului, proiectul, riscul, limitele suficiente și îndeplinirea celorlalte condiții sunt confirmate contractual, dar nu înlătură lipsa continuității asigurării. [Contract, P4](01_contract.md)