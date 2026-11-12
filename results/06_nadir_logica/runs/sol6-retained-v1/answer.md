# Review independent — tranșa NI-6

**Tranșa de 50.000 EUR este autorizabilă la 12.11.2026, ora 12:00 UTC.** Nota pentru comitet ajunge la concluzia opusă deoarece tratează lipsa valorilor afișate ca pe o imposibilitate de a deduce valoarea lui B.

| Finding material | Probe și deducție |
|---|---|
| **B este obligatoriu inactiv.** | [02_reguli.md](/case/02_reguli.md) [R5] spune că, dacă B ar fi activ, V ar trebui să fie activ. [R6] ar face atunci C activ. Totodată, [R3] ar face D inactiv; [R10] ar impune J activ; [R1] ar impune E activ; iar [R7] ar face C inactiv. Rezultă contradicția „C activ și C inactiv”. Cum indicatorii sunt binari și toate regulile sunt satisfăcute simultan, B este inactiv: [01_dosar.md](/case/01_dosar.md) [P3]. |
| **Concluzia notei despre autorizabilitate este eronată.** | [03_nota.md](/case/03_nota.md) [N1] afirmă că starea lui B și autorizabilitatea rămân nedeterminate. Deducția de mai sus stabilește B inactiv; [01_dosar.md](/case/01_dosar.md) [P2] prevede că aceasta este condiția necesară și suficientă, iar [P1] fixează momentul și suma. |
| **Lipsa valorilor individuale este o sursă de confuzie, nu un blocaj.** | Este corect că exportul nu le afișează direct: [01_dosar.md](/case/01_dosar.md) [P3], [03_nota.md](/case/03_nota.md) [N1]. Confirmarea că registrul respectă simultan regulile [P3] permite însă stabilirea lui B prin deducție. |
| **Nu se poate deduce că plata a fost făcută.** | [01_dosar.md](/case/01_dosar.md) [P2] distinge expres „autorizabilă” de executarea unui transfer; [03_nota.md](/case/03_nota.md) [N2] cere verificarea concluziei, nu efectuarea transferului. |

**Ce rămâne necunoscut:** valorile individuale ale lui J, C, D, E și S nu sunt toate determinate. Regulile admit patru stări coerente; în toate, **B și V sunt inactive**. V este inactiv deoarece [02_reguli.md](/case/02_reguli.md) [R8] cere ca B să fie activ pentru ca V să fie activ. Celelalte stări posibile nu schimbă verdictul.

**Aspecte corecte ale notei:** descrie fidel absența valorilor directe din export și nu introduce condiții suplimentare ([N1]–[N2]). Eroarea materială este concluzia că NI-6 nu poate fi declarată autorizabilă. Din regulile și faptele dosarului, poate fi declarată autorizabilă la momentul cerut.