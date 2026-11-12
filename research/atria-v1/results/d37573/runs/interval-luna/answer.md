# Raport pentru beneficiarul proiectului Atria

## Concluzie

Documentele **nu susțin eliberarea tranșei AT-72**. La închiderea ferestrei lucrărilor, suma autorizabilă este **0 EUR**.

Contractul prevede că tranșa de 90.000 EUR se autorizează integral numai dacă există acoperire în fiecare moment al ferestrei. Dacă apare orice întrerupere, suma autorizabilă este zero; plata proporțională cu orele acoperite nu este permisă (contract, P1–P2).

## Verificarea acoperirii

Fereastra contractuală este **[03.11.2026 00:00, 06.11.2026 00:00) UTC** (P1, P3). Certificatele acoperă:

| Interval UTC | Certificat(e) |
|---|---|
| 03.11.2026 00:00–04.11.2026 00:00 | A |
| 03.11.2026 18:00–05.11.2026 00:00 | B |
| 05.11.2026 06:00–06.11.2026 00:00 | C |

Perioadele provin din registrul certificatelor (R1). Suprapunerea dintre A și B asigură continuitate până la **05.11.2026 00:00**, dar există apoi o **întrerupere de șase ore**, între 00:00 și 06:00, înainte de începerea certificatului C. Prin urmare, acoperirea nu este continuă pe întreaga fereastră.

## Probleme materiale și efect

- **Lipsă de acoperire:** 05.11.2026 00:00–06:00 UTC. Aceasta împiedică îndeplinirea condiției contractuale de acoperire în fiecare moment (P2, R1).
- **Tranșă indivizibilă:** deși acoperirea există în restul ferestrei, contractul exclude plata proporțională; întreruperea conduce la 0 EUR autorizabili (P2).
- Registrul este declarat complet și validat, iar perioadele definitive; nu sunt indicate prelungiri sau alte acte care să acopere întreruperea (R2). Dosarul confirmă că analiza perioadelor este completă (N1).

Începutul inclus și finalul exclus nu schimbă concluzia: intervalele care se ating la aceeași oră asigură continuitate, dar între certificatele B și C există un interval neacoperit (P3).