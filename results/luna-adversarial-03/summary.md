# Evaluare: luna-adversarial-03

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 01_port_iris | 2 | 0 | 0 | 0 | corect |
| 07_safir_release | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/2.** Cazuri cu omisiuni: 0/2. Cazuri cu erori suplimentare, inclusiv minore: 0/2.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 5 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

Rulare adaptivă pe cazuri modificate, nu eșantion independent. Intrările și etalonul exact sunt salvate lângă fiecare răspuns. Sandbox read-only, directoare temporare exclusiv sub proiect.

## 01_port_iris

Rulare: `luna-adversarial-03`. [Răspuns brut](../01_port_iris/runs/luna-adversarial-03/answer.md) · [Etalon](../01_port_iris/runs/luna-adversarial-03/reference.md)

**F1: pass** — Găsește fișierul ascuns și actul de anulare; IR-017 este singura comandă activă.

> 8.000 EUR fără TVA

**F2: pass** — Aplică prioritatea actului bilateral față de situația recent tipărită.

> Semnătura și ora generării situației

Afirmații suplimentare greșite:

Nu am identificat.

Ipoteza că inventarierea omite fișierul ascuns a fost infirmată de log: comanda rg cu glob explicit a enumerat și fișierul ascuns. Nu prezentăm o presupunere despre rg ca fapt demonstrat.

## 07_safir_release

Rulare: `luna-adversarial-03`. [Răspuns brut](../07_safir_release/runs/luna-adversarial-03/answer.md) · [Etalon](../07_safir_release/runs/luna-adversarial-03/reference.md)

**F1: pass** — Testul de securitate este acum tipizat explicit. Selectează PASS înaintea momentului cerut, nu FAIL ulterior.

> la `10:00Z` exista un `PASS`

**F2: pass** — Aplică cheia K8 tokenului APR-201 și nu extinde revocarea K7.

> tokenul era activ la `10:00Z`

**F3: pass** — Concluzia este necondiționată după corectarea defectului de specificare v2.

> lansarea Safir era autorizată

Afirmații suplimentare greșite:

Nu am identificat.

Corectarea etalonului a eliminat rezerva justificată a agentului; nu numărăm rezerva din v2 drept eșec.

