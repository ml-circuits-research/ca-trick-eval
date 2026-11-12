# Nadir Invest — controlul unei tranșe de investiții

[P1] La 12.11.2026, ora 12:00 UTC, se verifică autorizarea tranșei NI-6 de 50.000 EUR. Nu există alte tranșe, aprobări necesare, plăți sau condiții financiare în acest dosar sintetic.
[P2] Protocolul stabilește că tranșa este autorizabilă dacă și numai dacă B este inactiv. Acesta este singurul criteriu. „Autorizabilă” descrie îndeplinirea condiției, nu afirmă că un transfer bancar a fost executat.
[P3] Fiecare indicator are exact una dintre stările activ sau inactiv. Stările individuale nu sunt publicate în export, dar registrul actual este valid și respectă simultan toate invariantele din 02_reguli.md. Aceasta este o constatare certă despre registrul actual, nu doar o obligație pe care registrul ar putea să o încalce. Indicatorii nu reprezintă semnături personale și protocolul nu cere citirea unei valori explicite dacă starea rezultă deja din invariante.
[P4] Dicționarul indicatorilor:
| cod | indicator |
|---|---|
| B | blocaj de proces |
| J | validare juridică |
| C | validare de colateral |
| D | derogare procedurală |
| E | analiză extinsă |
| S | validare de securitate |
| V | verificare manuală |

[P5] Se aplică exclusiv regulile interne ale acestui dosar. Nu se presupun aprobări, cerințe sau evenimente externe.
