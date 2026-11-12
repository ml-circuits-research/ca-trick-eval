# Evaluare: sol-nadir-735-v1

Model cerut: `gpt-6.1-sol`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 06_nadir_logica | 2 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune nouă, efort medium, izolare strictă. Variantele plain și business au aceleași soluții logice, dar formulări și instrucțiuni diferite; nu se confundă în rate. Evaluatorul este și autorul corpusului. Verdicturile finale sunt corecte; eroarea Luna este numai în prima demonstrație, nu în verdict.

## 06_nadir_logica

Rulare: `sol-nadir-735-v1`. [Răspuns brut](../06_nadir_logica/runs/sol-nadir-735-v1/answer.md) · [Etalon](../06_nadir_logica/runs/sol-nadir-735-v1/reference.md)

**F1: pass** — Demonstrează că B este inactiv în toate stările compatibile; există o demonstrație validă în răspuns.

> B este obligatoriu inactiv

**F2: pass** — Aplică corect echivalența din P2 și declară tranșa autorizabilă, infirmând nota.

> NI-6 este autorizabilă din documentele disponibile.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Demonstrația și configurațiile prezentate au fost confruntate cu regulile și oracolul exhaustiv. Nu există finding planificat omis. Pentru Terra și Sol nu am identificat erori materiale.

