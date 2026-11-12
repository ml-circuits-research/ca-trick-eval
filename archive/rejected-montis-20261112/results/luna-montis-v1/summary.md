# Evaluare: luna-montis-v1

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 03_montis_garantii | 4 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 4 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată, efort medium. Caz construit adaptiv; evaluatorul este și autorul. Toate findingurile sunt rezolvate corect, inclusiv de Luna; candidatul se retrage, fără a fabrica un eșec.

## 03_montis_garantii

Rulare: `luna-montis-v1`. [Răspuns brut](../03_montis_garantii/runs/luna-montis-v1/answer.md) · [Etalon](../03_montis_garantii/runs/luna-montis-v1/reference.md)

**F1: pass** — Identifică grupul N/E/V cu cerere 120 și capacitate eligibilă 100, reutilizarea capacităților în controalele individuale și neaprobabilitatea pachetului.

> Nota verifică disponibilul eligibil pentru fiecare credit separat, dar nu verifică dacă acele sume pot fi alocate simultan.

**F2: pass** — Demonstrează atât limita superioară a acoperirii (180), cât și o alocare fezabilă care o atinge; deficitul minim este exact 20.

> Expunerea minimă neacoperită este 20 milioane EUR.

**F3: pass** — Arată că oferta exclusiv pentru S nu mărește capacitatea N/E/V și păstrează deficitul minim de 20.

> O garanție suplimentară exclusiv pentru S nu poate acoperi deficitul din N/E/V; expunerea minimă rămâne 20.

**F4: pass** — Oferă o alocare completă validă cu garanția nouă pentru N și distinge corect ofertele, condiționat de incorporarea ofertei.

> Oferta alternativă de 20 exclusiv pentru N elimină deficitul și face posibilă acoperirea integrală.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate cele patru findinguri sunt demonstrate corect. Alocările alternative oferite de model au fost verificate: respectă eligibilitățile, capacitățile și principalul fiecărui credit. Nu am identificat erori materiale. Observația că ofertele nu sunt încă incorporate explicitează condiționalitatea F4, fără a fi un finding nou distinct.

