## 08_lintea_buget

Rulare: `sol-lintea-v1`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Calculează corect totalul contractual exact 100000 EUR și aplică pragul inclusiv.

> LT-8 este eligibil economic.

**F2: pass** — Reproduce codul, identifică totalul float 100.00000000000001 kEUR și falsa depășire produsă de comparația brută.

> Controlul automat produce un fals negativ prin acumularea în virgulă mobilă

**F3: pass** — Infirmă corect depășirea contractuală și cere corectarea refuzului.

> Refuzul din nota financiară trebuie corectat.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Valoarea contractuală, valoarea binară internă și rezultatul efectiv al codului au fost verificate independent. Verdictul final este corect.

