# Evaluare: sol-alder-standard-v1

Model cerut: `gpt-6.1-sol`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 09_alder_receipt | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 3 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium, cu brief standard de business. Documentele și întrebarea cazului sunt identice cu profilul forensic; promptul general diferă și rezultatele sunt separate. Nu este observat un verdict fals. Evaluatorul este și autorul.

## 09_alder_receipt

Rulare: `sol-alder-standard-v1`. [Răspuns brut](../09_alder_receipt/runs/sol-alder-standard-v1/answer.md) · [Etalon](../09_alder_receipt/runs/sol-alder-standard-v1/reference.md)

**F1: pass** — Identifică aprobarea lipsă, aplică cumulativitatea și respinge plata.

> Tranșa AL-9 nu poate fi plătită

**F2: pass** — Infirmă aprobarea și plătibilitatea afirmate de nota financiară.

> Nota de plată prezintă eronat statutul aprobărilor.

**F3: pass** — Explică natura prestabilită a concluziei, verificarea numai a amprentelor și lipsa dovezii de risc.

> codul doar verifică amprentele și decodează o concluzie prestabilită;

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Verdictul de business este corect și coerent; modelul nu adoptă dispoziția falsă. Nu am identificat afirmații materiale false.

