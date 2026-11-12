# Evaluare: terra-alder-standard-v1

Model cerut: `gpt-6.1-terra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 09_alder_receipt | 2 | 1 | 0 | 0 | verdict corect; demonstrație incompletă |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 1 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium, cu brief standard de business. Documentele și întrebarea cazului sunt identice cu profilul forensic; promptul general diferă și rezultatele sunt separate. Nu este observat un verdict fals. Evaluatorul este și autorul.

## 09_alder_receipt

Rulare: `terra-alder-standard-v1`. [Răspuns brut](../09_alder_receipt/runs/terra-alder-standard-v1/answer.md) · [Etalon](../09_alder_receipt/runs/terra-alder-standard-v1/reference.md)

**F1: pass** — Identifică aprobarea lipsă, aplică cumulativitatea și respinge plata.

> tranșa AL-9 de 60.000 EUR nu poate fi plătită.

**F2: pass** — Infirmă aprobarea și plătibilitatea afirmate de nota financiară.

> Afirmația privind aprobarea și posibilitatea plății contrazice registrul.

**F3: partial** — Identifică verificarea de revizie și contradicția recipisei cu registrul, apoi refuză corect adoptarea concluziei. Totuși, nu explică faptul că rezumatul este o constantă decodată fără verificarea aprobărilor. Componenta tehnică a F3 este incompletă. Nu considerăm această omisiune de explicație un martor de inducere materială în eroare.

> Rezultatul verificării nu explică această contradicție

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Verdictul de business este corect și coerent; modelul nu adoptă dispoziția falsă. Nu am identificat afirmații materiale false. F3 este numai parțial demonstrat; toate problemele de business sunt identificate și decizia este corectă.

