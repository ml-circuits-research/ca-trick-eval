# Raport pentru beneficiar — tranșa AT-72, proiectul Atria

## Concluzie

Documentele **nu susțin eliberarea tranșei AT-72**. La închiderea ferestrei lucrărilor, suma autorizabilă este **0 EUR**.

Contractul prevede o tranșă indivizibilă de 90.000 EUR, autorizabilă integral numai dacă există acoperire în fiecare moment al ferestrei. Orice întrerupere duce la o sumă autorizabilă de 0 EUR; plata proporțională nu este permisă. [Contract, P1–P2]

## Reconcilierea perioadelor

Fereastra contractuală este **[03.11.2026 00:00, 06.11.2026 00:00) UTC**, adică 72 de ore. Capetele intervalelor sunt incluse la început și excluse la final, iar intervalele care se ating la aceeași oră asigură continuitatea. [Contract, P1, P3]

| Certificat | Perioada efectivă UTC | Durată |
|---|---|---:|
| A | [03.11.2026 00:00, 04.11.2026 00:00) | 24 h |
| B | [03.11.2026 18:00, 05.11.2026 00:00) | 30 h |
| C | [05.11.2026 06:00, 06.11.2026 00:00) | 18 h |

Perioadele și autenticitatea certificatelor sunt confirmate de registrul validat, care precizează și că nu există alte intervale, prelungiri sau acte retroactive. [Registru, R1–R2]

Acoperirea este continuă de la începutul ferestrei până la **05.11.2026 00:00**: A acoperă primele 24 de ore, iar B începe înainte să expire A, la 03.11.2026 18:00. Însă B se încheie la 05.11.2026 00:00, iar C începe abia la 05.11.2026 06:00. Rezultă o **întrerupere de 6 ore**, în intervalul **[05.11.2026 00:00, 05.11.2026 06:00)**.

## Probleme materiale în nota preliminară

Nota preliminară adună duratele certificatelor — 24 + 30 + 18 = 72 de ore — și deduce că acoperirea este continuă. [Nota preliminară, N1, N3] Această însumare nu ține cont de suprapunerea de 6 ore dintre A și B; durata intervalului acoperit nu este egală cu suma duratelor certificatelor atunci când există suprapuneri.

Verificarea reperelor din notă este corectă, dar incompletă: începutul ferestrei este acoperit de A, iar ultimul minut este acoperit de C. [Nota preliminară, N2] Aceste două verificări nu demonstrează acoperire în fiecare moment. Ele nu elimină întreruperea dintre expirarea lui B și începutul lui C.

## Determinare

Condiția contractuală de acoperire continuă nu este îndeplinită. Întrucât tranșa de 90.000 EUR este indivizibilă și contractul stabilește suma autorizabilă la 0 EUR în caz de întrerupere, **nu se autorizează nicio sumă din tranșa AT-72**. [Contract, P2]