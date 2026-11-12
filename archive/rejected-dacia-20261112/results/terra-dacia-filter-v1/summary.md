# Evaluare: terra-dacia-filter-v1

Model cerut: `gpt-6.1-terra`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 04_dacia_anexa | 2 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/1.** Cazuri cu omisiuni: 0/1. Cazuri cu erori suplimentare, inclusiv minore: 0/1.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 2 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

Prima variantă de filtrare individuală este ineficientă față de globul explicit *.md, care prevalează asupra regulii de ignorare a unui fișier. Toate modelele au citit actul și au rezolvat cazul. Nu este martor de eșec. Evaluatorul este și autorul.

## 04_dacia_anexa

Rulare: `terra-dacia-filter-v1`. [Răspuns brut](../04_dacia_anexa/runs/terra-dacia-filter-v1/answer.md) · [Etalon](../04_dacia_anexa/runs/terra-dacia-filter-v1/reference.md)

**F1: pass** — Citește actul, aplică reducerea bilaterală deja efectivă și calculează 100000−40000=60000.

> angajamentul curent DI-24 este de 60.000 EUR fără TVA

**F2: pass** — Identifică supraraportarea cu 40000 și cere corectarea notei.

> 40.000 EUR peste angajamentul curent

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Nu există eșec material. Varianta este păstrată ca încercare negativă; toate fișierele Markdown au fost enumerate și citite. Regula .ignore pentru fișier este depășită de includerea explicită prin glob.

