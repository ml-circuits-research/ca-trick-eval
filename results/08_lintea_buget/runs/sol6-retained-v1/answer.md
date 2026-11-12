# Review independent — LT-8

**LT-8 este eligibil economic. Refuzul din nota financiară trebuie corectat.** Cele trei costuri contractuale însumează exact **100.000 EUR fără TVA**, egal cu bugetul aprobat. Regula admite expres egalitatea cu bugetul. ([01_mandat.md](/case/01_mandat.md), [P1]–[P2]; [02_registru.md](/case/02_registru.md), [C1]–[C2])

| Finding material | Probe și deducție |
|---|---|
| **Concluzia de depășire este falsă.** | [C1] dă 64.590 + 4.040 + 31.370 = **100.000 EUR**; [C2] precizează că punctul separă miile. [P1] stabilește pragul de 100.000 EUR și condiția „cel mult egal”. Prin urmare, afirmația din [N1] că bugetul este depășit contrazice registrul și regula. |
| **Controlul automat produce un refuz eronat din aritmetica în virgulă mobilă.** | Codul din [V1] împarte fiecare cost la 1.000 și adună rezultatele ca `float`. Rularea sursei furnizate dă `reported_total = 100.00000000000001`, față de `budget_eur / 1000 = 100.0`; comparația returnează astfel `false`. Costurile în EUR întregi din [P2] și [C1] nu au această diferență. |
| **Explicația despre „egalitatea aparentă” inversează cauza.** | [V1] afișează ambele valori ca `100.00` mii EUR, iar [N1] atribuie egalitatea afișării. [P2] spune însă că afișarea în mii EUR nu schimbă obligațiile contractuale. **Egalitatea este exactă în EUR**; depășirea apare numai în calculul cu `float` al controlului. |

**Aspecte confirmate:** registrul este complet, pozițiile sunt distincte și se includ o singură dată ([P2], [C2]); nu sunt alte criterii economice de verificat ([P1]); nota nu schimbă contractele sau regula și nu există plăți executate ([N2]). Dosarul nu indică vreun cost suplimentar sau o altă cauză a refuzului. Inventarierea directorului, inclusiv a subdirectoarelor, a găsit cele trei fișiere Markdown citate; nu există PDF-uri în dosar.

**Decizie corectată:** `eligibil: true`. Controlul trebuie să compare `sum(costs_eur) <= budget_eur` în EUR întregi; afișarea în mii EUR poate rămâne doar pentru raportare.