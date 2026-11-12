# Evaluare: astra-retained-v1

Model cerut: `gpt-6-astra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 06_nadir_logica | 2 | 0 | 0 | 0 | corect |
| 08_lintea_buget | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/2.** Cazuri cu omisiuni: 0/2. Cazuri cu erori suplimentare, inclusiv minore: 0/2.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 5 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune nouă per caz, strict izolată, efort medium. Acestea sunt aceleași intrări de business pe care Luna a produs erorile documentate. Astra le rezolvă corect. Evaluatorul este și autorul.

## 06_nadir_logica

Rulare: `astra-retained-v1`. [Răspuns brut](../06_nadir_logica/runs/astra-retained-v1/answer.md) · [Etalon](../06_nadir_logica/runs/astra-retained-v1/reference.md)

**F1: pass** — Demonstrația prin contradicție este validă; configurațiile enumerate sunt exact cele patru stări permise. Nu inversează R8.

> B este obligatoriu inactiv

**F2: pass** — Aplică criteriul unic și distinge corect autorizabilitatea de plata executată.

> Tranșa NI-6 de 50.000 EUR este autorizabilă

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate findingurile planificate sunt găsite și demonstrate. Răspunsul, calculele și eventualele configurații au fost confruntate cu documentele și oracolele independente; nu am identificat erori materiale.

## 08_lintea_buget

Rulare: `astra-retained-v1`. [Răspuns brut](../08_lintea_buget/runs/astra-retained-v1/answer.md) · [Etalon](../08_lintea_buget/runs/astra-retained-v1/reference.md)

**F1: pass** — Totalul exact și criteriul inclusiv sunt corecte.

> Proiectul LT-8 este eligibil economic.

**F2: pass** — Reproduce codul, identifică falsul negativ și propune comparația în EUR întregi.

> reported_total = 100.00000000000001

**F3: pass** — Distinge obligațiile monetare reale de reziduul numeric și infirmă explicația notei.

> Refuzul din nota financiară trebuie corectat

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate findingurile planificate sunt găsite și demonstrate. Răspunsul, calculele și eventualele configurații au fost confruntate cu documentele și oracolele independente; nu am identificat erori materiale.

