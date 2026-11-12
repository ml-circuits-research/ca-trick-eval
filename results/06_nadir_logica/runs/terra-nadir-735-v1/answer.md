## Concluzie

**Autorizabilitatea NI-6 poate fi stabilită: tranșa este autorizabilă.** În orice stare validă a registrului compatibilă cu dosarul, B este inactiv. Concluzia notei că autorizabilitatea este nedeterminată este, prin urmare, greșită.

Dovada nu presupune valori individuale nepublicate. Folosește faptul cert că registrul actual respectă simultan toate invariantele și că fiecare indicator este fie activ, fie inactiv ([01_dosar.md, P3](/case/01_dosar.md), [02_reguli.md, I1](/case/02_reguli.md)).

## Verificarea afirmației comitetului

Presupunem provizoriu că **B este activ** și verificăm consecințele:

1. B activ implică V activ ([02_reguli.md, R5](/case/02_reguli.md)).
2. V activ implică atât D inactiv, cât și C activ ([02_reguli.md, R3 și R6](/case/02_reguli.md)).
3. Dacă J ar fi inactiv, D ar trebui să fie activ ([02_reguli.md, R10](/case/02_reguli.md)). Dar D este inactiv; deci J nu poate fi inactiv și, având numai două stări posibile, este activ ([01_dosar.md, P3](/case/01_dosar.md)).
4. J activ implică E activ, iar E activ implică C inactiv ([02_reguli.md, R1 și R7](/case/02_reguli.md)).

Rezultă că C ar trebui să fie **simultan activ și inactiv**, ceea ce contrazice [P3](/case/01_dosar.md). Așadar, B nu poate fi activ. Cum B are exact una dintre cele două stări, **B este inactiv**.

Protocolul spune că tranșa este autorizabilă dacă și numai dacă B este inactiv și că acesta este singurul criteriu ([01_dosar.md, P2](/case/01_dosar.md)). Prin urmare, NI-6 îndeplinește criteriul. Afirmația din [03_nota.md, N1](/case/03_nota.md), potrivit căreia nu se poate stabili dacă B este inactiv și tranșa nu poate fi declarată autorizabilă, este infirmată.

## Ce este cert și ce rămâne necunoscut

Lipsa valorilor explicite din export este reală, dar nu împiedică deducerea stării lui B: dosarul precizează expres că o valoare nu trebuie citită explicit atunci când rezultă din invariante ([01_dosar.md, P3](/case/01_dosar.md)). Mai rezultă că **V este inactiv**, deoarece V activ ar impune B activ ([02_reguli.md, R8](/case/02_reguli.md)).

Celelalte stări nu sunt toate determinate individual. Pentru a arăta atât limitele cunoașterii, cât și consistența concluziei, acestea sunt **toate configurațiile** compatibile simultan cu regulile; `1` înseamnă activ și `0` inactiv:

| B | J | C | D | E | S | V |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |

Astfel, B și V sunt certe ca inactive, în timp ce J, C, D, E și S pot avea valori diferite între configurațiile valide. Tabelul arată și că regulile nu sunt contradictorii în ansamblu: există stări valide, iar în fiecare B este inactiv.

Este corect în notă că exportul nu afișează direct stările și că verificarea privește concluzia, nu efectuarea transferului ([03_nota.md, N1–N2](/case/03_nota.md); [01_dosar.md, P3](/case/01_dosar.md)). De asemenea, dosarul nu adaugă alte condiții sau blocaje de verificat ([01_dosar.md, P1–P2 și P5](/case/01_dosar.md)). **Autorizabilitatea nu dovedește însă executarea unui transfer bancar** ([01_dosar.md, P2](/case/01_dosar.md)).