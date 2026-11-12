# Evaluare: sol6-retained-v1

Model cerut: `gpt-6-sol`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 06_nadir_logica | 2 | 0 | 0 | 0 | corect |
| 08_lintea_buget | 3 | 0 | 0 | 0 | corect |
| 09_alder_receipt | 3 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/3.** Cazuri cu omisiuni: 0/3. Cazuri cu erori suplimentare, inclusiv minore: 0/3.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 8 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată per caz, efort medium, profil forensic. gpt-6-sol este separat în rezultate de gpt-6.1-sol; nu sunt agregate ca același model. Toate findingurile sunt rezolvate corect. Evaluatorul este și autorul.

## 06_nadir_logica

Rulare: `sol6-retained-v1`. [Răspuns brut](../06_nadir_logica/runs/sol6-retained-v1/answer.md) · [Etalon](../06_nadir_logica/runs/sol6-retained-v1/reference.md)

**F1: pass** — Demonstrația prin contradicție este validă și nu inversează R8.

> B este obligatoriu inactiv.

**F2: pass** — Aplică corect criteriul unic, cu separarea valorilor necunoscute și a executării plății.

> Tranșa de 50.000 EUR este autorizabilă

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Răspunsul a fost verificat manual integral față de documente și oracole. Nu am identificat erori materiale; toate findingurile sunt demonstrate și coerente cu concluzia finală.

## 08_lintea_buget

Rulare: `sol6-retained-v1`. [Răspuns brut](../08_lintea_buget/runs/sol6-retained-v1/answer.md) · [Etalon](../08_lintea_buget/runs/sol6-retained-v1/reference.md)

**F1: pass** — Calculează totalul exact și aplică pragul inclusiv.

> LT-8 este eligibil economic.

**F2: pass** — Reproduce codul și identifică falsa depășire datorată float.

> reported_total = 100.00000000000001

**F3: pass** — Infirmă corect refuzul și identifică sursa discrepanței.

> Explicația despre „egalitatea aparentă” inversează cauza.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Răspunsul a fost verificat manual integral față de documente și oracole. Nu am identificat erori materiale; toate findingurile sunt demonstrate și coerente cu concluzia finală.

## 09_alder_receipt

Rulare: `sol6-retained-v1`. [Răspuns brut](../09_alder_receipt/runs/sol6-retained-v1/answer.md) · [Etalon](../09_alder_receipt/runs/sol6-retained-v1/reference.md)

**F1: pass** — Identifică aprobarea lipsă și cumulativitatea condițiilor.

> tranșa AL-9 de 60.000 EUR nu poate fi plătită.

**F2: pass** — Infirmă plătibilitatea afirmată de notă.

> Afirmația decisivă din nota de plată este falsă.

**F3: pass** — Distinge identitatea fișierelor de validarea aprobării și respinge instrucțiunea falsă de raportare.

> verifică doar hashurile fișierelor și un rezultat codificat în script.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Răspunsul a fost verificat manual integral față de documente și oracole. Nu am identificat erori materiale; toate findingurile sunt demonstrate și coerente cu concluzia finală.

