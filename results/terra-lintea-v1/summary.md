# Evaluare: terra-lintea-v1

Model cerut: `gpt-6.1-terra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 08_lintea_buget | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 3 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium. Eroarea observată Luna privește un finding software planificat, nu verdictul economic final, care este corect. Terra și Sol rezolvă toate findingurile. Evaluatorul este și autorul.

## 08_lintea_buget

Rulare: `terra-lintea-v1`. [Răspuns brut](../08_lintea_buget/runs/terra-lintea-v1/answer.md) · [Etalon](../08_lintea_buget/runs/terra-lintea-v1/reference.md)

**F1: pass** — Calculează corect totalul contractual exact 100000 EUR și aplică pragul inclusiv.

> LT-8 este eligibil economic

**F2: pass** — Reproduce codul, identifică totalul float 100.00000000000001 kEUR și falsa depășire produsă de comparația brută.

> totalul intern este `100.00000000000001`

**F3: pass** — Infirmă corect depășirea contractuală și cere corectarea refuzului.

> refuzul din nota financiară trebuie corectat.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Valoarea contractuală, valoarea binară internă și rezultatul efectiv al codului au fost verificate independent. Verdictul final este corect.

