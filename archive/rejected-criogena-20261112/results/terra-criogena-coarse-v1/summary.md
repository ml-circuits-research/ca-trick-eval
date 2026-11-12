# Evaluare: terra-criogena-coarse-v1

Model cerut: `gpt-6.1-terra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 07_criogena_plan | 2 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium. Candidatul este rezolvat corect inclusiv de Luna și se retrage. Evaluatorul este și autorul.

## 07_criogena_plan

Rulare: `terra-criogena-coarse-v1`. [Răspuns brut](../07_criogena_plan/runs/terra-criogena-coarse-v1/answer.md) · [Etalon](../07_criogena_plan/runs/terra-criogena-coarse-v1/reference.md)

**F1: pass** — Verifică ambele alegeri irevocabile ale transportatorului: Aurora pierde unul dintre scenariile indistincte S1/S2, Boreal pierde S3.

> CR-7 nu poate fi lansat conform contractului

**F2: pass** — Demonstrează limita de două scenarii, politici care o ating și lipsa probabilităților. Distinge corect planurile separate de o politică executabilă.

> două scenarii conforme din trei

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate planurile și afirmațiile despre scenarii au fost confruntate cu tabelul și cu oracolul independent pe clase de informație. Nu am identificat erori materiale. Cazul este respins ca martor de eșec.

