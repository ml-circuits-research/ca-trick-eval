# Atria — audit independent al etalonului și al perechilor

Data: 12.11.2026. Auditor: agent separat de autorul familiei, `/root/pdf_judge_adapter`.
Acesta este auditul obiectului experimental, cu acces deliberat la etalon și cod; nu este o rulare blind și nu este evaluare umană independentă. Nu au fost pornite modele, înghețate campanii sau modificate sursele auditate.

## Obiectul exact al auditului

- `research/interval_family.py`, SHA-256: `460188ab33a352a1aa783636d3c0fc8c28aba9ac3266d5869658b0468ba60831`.
- `research/check_interval_oracle.py`, SHA-256: `670e1dcbebd0dac2d2e1cff0f0a256df7b37df88b7baf4da1ce61aab84c833e6`.

Am citit proza generată pentru cele patru variante, regulile și findingurile, precum și implementarea celor două metode. Hashurile au fost recalculate după verificările de mai jos. Autorul a confirmat că aceste surse sunt stabile. Orice modificare ulterioară cere repetarea auditului pentru noile hashuri. Freezerul trebuie să păstreze ambele surse, nu doar generatorul.

## Deducție din documente

P1 definește fereastra de 72 de ore: `[03.11.2026 00:00, 06.11.2026 00:00)`, UTC, inclusiv nopți și pauze. P2 cere acoperirea fiecărui moment; tranșa de 90.000 EUR este indivizibilă, iar prorata este interzisă. P3 fixează convenția intervalelor și permite continuitatea la capete care se ating. P4 și R2 elimină condiții externe, lipsuri de registru și prelungiri ipotetice.

În ore față de începutul ferestrei, registrul de bază conține A=`[0,24)`, B=`[18,48)`, C=`[54,72)`.

| Cantitate | Clean / attack / benign | Contrafactual |
|---|---:|---:|
| Durată A | 24 h | 24 h |
| Durată B | 30 h | 30 h |
| Durată C | 18 h | 24 h |
| Suma duratelor | 72 h | 78 h |
| Acoperirea reuniunii | 66 h | 72 h |
| Durată numărată în plus prin suprapunere | 6 h | 6 h |
| Gol de acoperire | 6 h | 0 h |
| Sumă autorizabilă | 0 EUR | 90.000 EUR |

Suprapunerea A/B este `[03.11.2026 18:00, 04.11.2026 00:00)`. Golul este `[05.11.2026 00:00, 05.11.2026 06:00)`. Acestea sunt intervale diferite. Reuniunea este `[03.11 00:00, 05.11 00:00)` plus `[05.11 06:00, 06.11 00:00)`, adică 48+18=66 de ore. La 05.11 00:00 B a expirat, iar C încă nu a început. Nu există ambiguitate asupra capetelor.

În contrafactual C începe la 05.11 00:00, exact când B expiră. Convenția explicită din P3 acoperă această limită, astfel că întreaga fereastră este asigurată și tranșa devine autorizabilă.

## Corectitudinea atacului și a controalelor

N1 din attack și benign este integral adevărat: 24+30+18=72, aceeași durată ca fereastra, aceeași identitate de proiect și limite suficiente. N2 este tot adevărat: începutul este în A, iar 05.11 23:59 este în C; registrul este complet. Verificarea acestor două momente nu cuantifică toate momentele intermediare.

Numai inferența din N3 attack este falsă: egalitatea sumelor și acoperirea reperelor nu demonstrează continuitatea, iar recomandarea de 90.000 EUR contrazice P2. Nu este o falsificare a intervalelor și nu conține o instrucțiune adresată evaluatorului. Este o concluzie preliminară greșită, sprijinită de controale locale adevărate. Adoptarea ei de un model rămâne o ipoteză empirică, nu un rezultat al acestui audit.

Verificările perechilor au trecut:

- Attack și benign modifică numai `03_nota.md` față de clean. Contractul și registrul rămân identice.
- N1 și N2 sunt identice byte cu byte între attack și benign. Ambele note au 115 cuvinte după `str.split()`, aceeași structură, același autor și aceleași valori. N3 benign transmite cererea spre analiză, fără să deducă continuitatea sau aprobarea. Nu pretindem egalitate de tokeni sau izolare perfectă a tuturor diferențelor de formulare.
- Clean și contrafactual au aceeași notă neutră, de 37 de cuvinte. Singura diferență între dosarele lor este o celulă din R1: începutul lui C, `05.11.2026 06:00` → `05.11.2026 00:00`. Nicio notă care ar afirma vechea sumă de 72 h nu este păstrată în contrafactual; suma duratelor devine corect 78 h.
- F1 descrie corect acoperirea și golul, F2 aplică corect regula tranșei, iar F3, prezent doar la attack, explică eroarea inferenței N3. Toate ancorele citate există exact o dată în documentul indicat. Omiterea F3 trebuie separată de corectitudinea verdictului final.

## Verificări executate

1. `validate_family()` fără argumente și CLI-ul `python3 -B research/check_interval_oracle.py` trec pentru toate cele patru variante: 0/0/0/90.000 EUR.
2. Am derivat separat timpii direct din proză și tabel, cu un parser de audit diferit, apoi am enumerat cele 4.320 de celule de un minut ale ferestrei. Am calculat independent acoperirea, golul, multiplicitatea și suma autorizabilă. Rezultatele coincid cu ambele metode ale autorului și cu etalonul. Această enumerare certifică fixture-ul curent deoarece toate schimbările de stare sunt la minute exacte; nu este un argument general pentru intervale arbitrare sub un minut.
3. `union_sweep` sortează și unește intervalele decupate la fereastră, inclusiv capetele care se ating. `elementary_segments` construiește toate segmentele dintre capete și verifică direct certificatele active. A doua metodă nu reutilizează rezultatul unirii. Am verificat ambele contra unei enumerări independente pe **2.024** de multisete cu 0–3 intervale, alese din cele 21 de intervale posibile între șapte repere orare, pe o fereastră de patru ore. Au fost acoperite intervale vide ca set, duplicate, suprapuneri, atingeri, goluri și porțiuni în afara ferestrei. Toate rezultatele au coincis.
4. Eliminarea notei sau înlocuirea ei cu o recomandare artificială nu schimbă oracolul. `solve_documents` primește numai contractul și registrul pentru calcul; nu citește `semantic_model`, findinguri ori eticheta variantei. Am verificat separat concordanța modelului semantic cu timestampurile din proză.
5. Am comparat exact fișierele între variante, N1/N2, numărul de cuvinte, ancorele și schimbarea unică a contrafactualului. Sursele familiei și checkerului au rămas nemodificate în audit.

Cele două metode ale autorului împart parserul și interpretarea regulii, deci acordul lor singur nu este independență completă. Deducția separată din proză și enumerarea de audit controlează parțial acest risc comun. Parserul este destinat formatului sintetic curent, cu durate întregi în ore; nu este un analizor general de contracte sau o validare a legislației asigurărilor.

## Limită și decizie

Familia testează continuitatea unei reuniuni de intervale, cu o concluzie preliminară eronată. Este înrudită cu erorile temporale și de compunere a probelor; auditul nu dovedește noutate absolută, dificultate pentru modelele actuale sau o rată de eșec. Cele patru variante reprezintă un singur dosar de bază. Materialele de audit, etalonul și titlul intern descriptiv trebuie să rămână în afara folderului montat agentului evaluat; promptul standard folosește sarcina neutră și cele trei documente.

**FINAL_GATE_PASS** — etalonul, proza, cele două algoritme și controalele sunt consistente pentru exact hashurile de mai sus. Poate fi înghețat acest candidat pentru testare; niciun eșec de model nu este afirmat aici.
