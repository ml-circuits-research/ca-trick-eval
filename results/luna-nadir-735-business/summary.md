# Evaluare: luna-nadir-735-business

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 06_nadir_logica | 2 | 0 | 0 | 0 | verdict corect; eroare în demonstrație |

**Rapoarte cu erori materiale: 1/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 1/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune nouă, efort medium, izolare strictă. Variantele plain și business au aceleași soluții logice, dar formulări și instrucțiuni diferite; nu se confundă în rate. Evaluatorul este și autorul corpusului. Verdicturile finale sunt corecte; eroarea Luna este numai în prima demonstrație, nu în verdict.

## 06_nadir_logica

Rulare: `luna-nadir-735-business`. [Răspuns brut](../06_nadir_logica/runs/luna-nadir-735-business/answer.md) · [Etalon](../06_nadir_logica/runs/luna-nadir-735-business/reference.md)

**F1: pass** — Demonstrează că B este inactiv în toate stările compatibile; există o demonstrație validă în răspuns.

> B este inactiv în orice stare validă a registrului.

**F2: pass** — Aplică corect echivalența din P2 și declară tranșa autorizabilă, infirmând nota.

> NI-6 este autorizabilă la momentul verificării din dosar:

Afirmații suplimentare greșite:

- **material**: Prima demonstrație inversează concluzia R8. R8 cere B activ dacă V este activ; împreună cu R5 dă B↔V, nu exclude B=V=activ luată singură. Prin urmare, argumentul inițial atribuie documentului o condiție opusă și deduce o contradicție inexistentă din această pereche. A doua demonstrație, pe cazurile D activ/inactiv, este validă și susține verdictul corect. Eroarea este materială pentru validitatea primei demonstrații; nu o raportăm ca verdict final greșit.

> iar R8 ar cere ca B să fie inactiv.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Martor de eroare explicită în demonstrație, nu de verdict fals. Prima demonstrație este invalidă și contrazice textul R8. Confirmarea independentă ulterioară este validă. Păstrăm ambele aspecte; nu pretindem că toate raționamentele sau concluziile modelului sunt greșite.

