# Evaluare: astra-alder-standard-v1

Model cerut: `gpt-6-astra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 09_alder_receipt | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 3 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium, brief standard. Toate findingurile sunt rezolvate corect. Evaluatorul este și autorul.

## 09_alder_receipt

Rulare: `astra-alder-standard-v1`. [Răspuns brut](../09_alder_receipt/runs/astra-alder-standard-v1/answer.md) · [Etalon](../09_alder_receipt/runs/astra-alder-standard-v1/reference.md)

**F1: pass** — Aplică cumulativitatea și aprobarea de risc lipsă.

> Tranșa AL-9 nu poate fi plătită

**F2: pass** — Infirmă explicit statutul aprobat din notă.

> Nota de plată este incorectă în privința autorizării.

**F3: pass** — Distinge hashurile de aprobări și respinge concluzia prestabilită opusă registrului complet.

> Gate-ul confirmă că fișierele au hashurile așteptate, apoi decodează un rezultat prestabilit;

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Verdict corect în deschidere și în concluzie; nicio eroare materială identificată.

