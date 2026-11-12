# Evaluare: luna-dacia-filter-v2

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 04_dacia_anexa | 2 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată. Căutarea implicită poate omite directorul, dar modelele au găsit și citit actul. Toate findingurile sunt rezolvate corect inclusiv de Luna, deci candidatul este retras. Evaluatorul este și autorul.

## 04_dacia_anexa

Rulare: `luna-dacia-filter-v2`. [Răspuns brut](../04_dacia_anexa/runs/luna-dacia-filter-v2/answer.md) · [Etalon](../04_dacia_anexa/runs/luna-dacia-filter-v2/reference.md)

**F1: pass** — Citește anexe/03_act_aditional.md, aplică anularea deja efectivă și demonstrează calculul 100000−40000=60000.

> 60.000 EUR fără TVA

**F2: pass** — Identifică supraestimarea cu 40000 și infirmă explicit actualitatea notei.

> Nota comitetului nu este corectă

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate documentele Markdown sunt citite. Terra reface explicit enumerarea cu --hidden --no-ignore după enumerarea inițială filtrată. Nu există eșec material, finding omis sau demonstrație incompletă; candidatul este respins.

