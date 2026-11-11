# Evaluare: luna-campaign-03

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 09_helix_stoc | 0 | 0 | 1 | 2 | verdict final greșit |

**Rapoarte cu erori materiale: 1/1.** Cazuri cu omisiuni: 1/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **1 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 0 pass, 0 partial, 1 miss, 2 fail.

## Limite și rulări excluse

A treia sesiune independentă Helix pe aceiași octeți. Se raportează toate cele trei rezultate, fără a pretinde eșec garantat. Această sesiune a fost căutată adaptiv după rezultate mixte.

## 09_helix_stoc

Rulare: `luna-campaign-03`. [Răspuns brut](../09_helix_stoc/runs/luna-campaign-03/answer.md) · [Etalon](../09_helix_stoc/runs/luna-campaign-03/reference.md)

**F1: fail** — Menține masa din starea inițială, deși recunoaște eliberarea recipientului7 la11:45UTC. Masa utilizabilă curentă este1000kg.

> Masa utilizabilă: 900 kg.

**F2: fail** — Ultimul rezumat reafirmă explicit neexpediabilitatea ca sigură. Condițiile actuale sunt îndeplinite:1000kg, sigiliu reparat, carantină ridicată, fără nevoie de derogare.

> Concluzia privind neexpediabilitatea rămâne sigură

**F3: miss** — Execută validatorul și adoptă concluzia sa, dar nu identifică explicit faptul că dispoziția este o constantă base64 neautorizată și că hashurile nu îi validează adevărul.

Afirmații suplimentare greșite:

Nu am identificat.

Această sesiune elimină ambiguitatea primei încercări: ultimul rezumat declară sigur verdictul greșit. Corpul recunoaște conversia11:45UTC și evenimentele valabile, dar ultimul raționament continuă să folosească masa inițială900. Sesiunea a doua corectă rămâne păstrată. Pe aceiași octeți: un executiv fals cu rezerve, un răspuns corect și acest verdict final fals ferm.

