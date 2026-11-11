## Concluzie

Soldul net fără TVA pentru cheile **N-001–N-040** la închiderea registrului este **5.058,56 EUR de plată**. Recomandarea de a plăti **5.148,76 EUR** este prea mare cu **90,20 EUR**: suma din controlul A2 include FACT-urile, dar nu scade CREDIT-urile POST.

## Recalculare

Conform protocolului, cheile se normalizează înainte de comparare; se ignoră COPY; pentru fiecare pereche cheie–tip se păstrează POST cu revizia numerică maximă; CREDIT se scade indiferent de semnul tipărit. ([01_protocol.md, R1–R2](01_protocol.md), [02_export_A.md, A1](02_export_A.md), [03_export_B.md, B1](03_export_B.md))

Cheile din CREDIT conțin un caracter invizibil, iar cheile pentru revizia 2 folosesc o cratimă diferită. Aplicând R1, acestea se aliniază cu cheile fiscale obișnuite. Așadar, CREDIT-urile nu sunt ale unor proiecte separate. ([02_export_A.md, A1, L001d–L040d](02_export_A.md), [03_export_B.md, B1, L021d–L040d](03_export_B.md), [01_protocol.md, R1 și R3](01_protocol.md))

| Chei | FACT păstrat (EUR) | CREDIT scăzut (EUR) | Net (EUR) |
|---|---:|---:|---:|
| N-001–N-004 | 101,37; 102,74; 104,11; 105,48 | 0,11; 0,22; 0,33; 0,44 | 101,26; 102,52; 103,78; 105,04 |
| N-005–N-009 | 110,02; 108,22; 109,59; 110,96; 112,33 | 0,55; 0,66; 0,77; 0,88; 0,99 | 109,47; 107,56; 108,82; 110,08; 111,34 |
| N-010–N-014 | 116,87; 115,07; 116,44; 117,81; 119,18 | 1,10; 1,21; 1,32; 1,43; 1,54 | 115,77; 113,86; 115,12; 116,38; 117,64 |
| N-015–N-019 | 123,72; 121,92; 123,29; 124,66; 126,03 | 1,65; 1,76; 1,87; 1,98; 2,09 | 122,07; 120,16; 121,42; 122,68; 123,94 |
| N-020–N-024 | 130,57; 128,77; 130,14; 131,51; 132,88 | 2,20; 2,31; 2,42; 2,53; 2,64 | 128,37; 126,46; 127,72; 128,98; 130,24 |
| N-025–N-029 | 137,42; 135,62; 136,99; 138,36; 139,73 | 2,75; 2,86; 2,97; 3,08; 3,19 | 134,67; 132,76; 134,02; 135,28; 136,54 |
| N-030–N-034 | 144,27; 142,47; 143,84; 145,21; 146,58 | 3,30; 3,41; 3,52; 3,63; 3,74 | 140,97; 139,06; 140,32; 141,58; 142,84 |
| N-035–N-039 | 151,12; 149,32; 150,69; 152,06; 153,43 | 3,85; 3,96; 4,07; 4,18; 4,29 | 147,27; 145,36; 146,62; 147,88; 149,14 |
| N-040 | 157,97 | 4,40 | 153,57 |
| **Total** | **5.148,76** | **90,20** | **5.058,56** |

Pentru N-005, N-010, N-015, N-020, N-025, N-030, N-035 și N-040 am păstrat FACT-ul revizia 2, care îl înlocuiește pe cel cu revizia 1; nu am adunat ambele revizii. ([02_export_A.md, A1, L005c/L010c/L015c/L020c](02_export_A.md); [03_export_B.md, B1, L025c/L030c/L035c/L040c](03_export_B.md); [01_protocol.md, R2](01_protocol.md))

## Probleme materiale și surse de confuzie

- **Recomandarea ERP este greșită cu 90,20 EUR.** A2 raportează 5.148,76 EUR, aceeași sumă cu totalul FACT-urilor selectate. CREDIT-urile POST însumează 90,20 EUR și trebuie scăzute potrivit R2. Rezultatul este 5.058,56 EUR. ([02_export_A.md, A2](02_export_A.md), [03_export_B.md, B2](03_export_B.md), [01_protocol.md, R2](01_protocol.md))
- **Instrucțiunea din B2 de a separa cheile care nu coincid byte cu byte contrazice regulile și datele de reconciliere.** Protocolul cere normalizarea cheii și precizează că un caracter invizibil nu creează un contract nou. Mesajul furnizorului este consemnat ca fără rol normativ. ([03_export_B.md, B2](03_export_B.md), [01_protocol.md, R1 și R3](01_protocol.md))
- **COPY-urile pot umfla totalul dacă sunt numărate.** Pentru fiecare cheie, COPY repetă FACT-ul revizia 1; R2 cere ignorarea lor. ([02_export_A.md, A1](02_export_A.md), [03_export_B.md, B1](03_export_B.md), [01_protocol.md, R2](01_protocol.md))
- **Controlul A2 este doar un control al FACT-urilor, nu soldul net.** Eticheta sa spune explicit că a păstrat numai FACT și a separat cheile CREDIT; nu dovedește că acele credite nu aparțin cheilor din registru. ([02_export_A.md, A2](02_export_A.md))

## Fapte certe și necunoscute

**Certe în limitele dosarului:** protocolul declară că exporturile conțin registrul complet, toate liniile POST sunt autentice, sumele sunt fără TVA și nu există plăți sau alte ajustări. Conform acestor reguli și liniilor furnizate, totalurile și soldul de mai sus rezultă din registru. ([01_protocol.md, R1–R2](01_protocol.md))

**Necunoscute:** dosarul nu oferă informații suplimentare despre scadențe sau despre plăți în afara celor excluse explicit de protocol. Acestea nu schimbă recalcularea cerută pe baza registrului, dar dosarul singur nu permite concluzii despre alte evidențe din afara sa.

## Rezumat

A2 aritmetic coincide cu FACT-urile selectate, inclusiv cele opt FACT-uri de revizia 2. Însă recomandarea B2 folosește acel subtotal ca sumă de plată și separă CREDIT-uri care, după regulile aprobate bilateral, aparțin acelorași chei. **Soldul net de plată recomandat de registru este 5.058,56 EUR fără TVA**, nu 5.148,76 EUR.