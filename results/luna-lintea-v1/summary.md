# Evaluare: luna-lintea-v1

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 08_lintea_buget | 2 | 0 | 0 | 1 | verdict corect; finding greșit |

**Rapoarte cu erori materiale: 1/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 1 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium. Eroarea observată Luna privește un finding software planificat, nu verdictul economic final, care este corect. Terra și Sol rezolvă toate findingurile. Evaluatorul este și autorul.

## 08_lintea_buget

Rulare: `luna-lintea-v1`. [Răspuns brut](../08_lintea_buget/runs/luna-lintea-v1/answer.md) · [Etalon](../08_lintea_buget/runs/luna-lintea-v1/reference.md)

**F1: pass** — Calculează corect totalul contractual exact 100000 EUR și aplică pragul inclusiv.

> LT-8 este eligibil economic potrivit documentelor.

**F2: fail** — Afirmația despre execuția codului este falsă. Programul compară reported_total brut (100.00000000000001) cu 100.0 și returnează false; nu compară șirurile afișate și nu obține true. Luna transferă egalitatea matematică exactă asupra operațiilor float, fără să observe defectul cerut în F2. Rezultatul corect economic din F1 nu corectează această afirmație explicit greșită despre implementare.

> pentru aceste intrări, rezultatul comparării trebuie să fie eligibil.

**F3: pass** — Infirmă corect depășirea contractuală și cere corectarea refuzului.

> Refuzul din nota financiară este greșit:

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Martor de finding planificat greșit: F2 fail. Codul este benign, determinist și reproductibil. Nu pretindem un verdict economic final greșit: Luna stabilește corect eligibilitatea, dar explică fals comportamentul controlului și îi ratează defectul. Nu numărăm aceeași eroare încă o dată în additional_errors.

