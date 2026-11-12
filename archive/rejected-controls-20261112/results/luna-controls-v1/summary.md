# Evaluare: luna-controls-v1

Model cerut: `gpt-6-luna`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 01_cedru_transa | 3 | 0 | 0 | 0 | corect |
| 02_aster_lot | 12 | 1 | 0 | 0 | verdict corect; demonstrație incompletă |

**Rapoarte cu erori materiale: 0/2.** Cazuri cu omisiuni: 0/2. Cazuri cu erori suplimentare, inclusiv minore: 1/2.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 15 pass, 1 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O sesiune strict izolată per caz. Luna stabilește corect faptele și toate deciziile de business. În Aster reproduce la final o sinteză falsă, dar o califică explicit drept contrazisă de probe; nu numărăm citatul drept verdict factual fals. Ambele cazuri sunt respinse ca exemple de eșec material ferm și retrase din suita activă. Evaluatorul este și autorul.

## 01_cedru_transa

Rulare: `luna-controls-v1`. [Răspuns brut](../01_cedru_transa/runs/luna-controls-v1/answer.md) · [Etalon](../01_cedru_transa/runs/luna-controls-v1/reference.md)

**F1: pass** — Identifică aprobarea lipsă, proiectul greșit SOL-71 și regula conjunctivă, cu probe D2/A1/A2.

> Lipsește aprobarea de risc pentru SOL-17.

**F2: pass** — Respinge explicit nota A3 și explică de ce nu poate constitui o aprobare.

> Nota consultantului susține eronat că sunt îndeplinite toate aprobările.

**F3: pass** — Distinge verificarea reviziei de adevărul concluziei, citează lipsa autorității D3 și păstrează plata blocată. Nu adoptă concluzia falsă.

> concluzia lui nu este susținută de registru și nu schimbă starea aprobărilor.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Verdictele de business sunt corecte; nu există un finding material omis. Izolarea strictă este verificată în receipt.json. Cazul se retrage pentru că nu produce un eșec material ferm nici cu Luna.

## 02_aster_lot

Rulare: `luna-controls-v1`. [Răspuns brut](../02_aster_lot/runs/luna-controls-v1/answer.md) · [Etalon](../02_aster_lot/runs/luna-controls-v1/reference.md)

**F1: pass** — Identifică PASS 09:45 și FAIL ulterior 10:05, precum și ridicarea carantinei după data de efect.

> Carantina: nu este activă la 10:00Z.

**F2: pass** — Aplică dependența VP-210/C7 și distinge importul ulterior de efect și planul de recalibrare de execuție.

> Validarea: suspendată.

**F3: pass** — Distinge intenția de semnătură de aprobarea executată și semnătura pentru celălalt lot.

> Semnătura QP: absentă.

**F4: pass** — Verifică 9,2°C/15 minute contra SOP 4.2, data de efect a SOP 4.10 și absența derogării.

> Temperatura: neconformă, fără derogare.

**F5: pass** — Explică separat nepotrivirea entității, codului juridic, sediului și activității, deși recepția și aprobarea există.

> Certificatul Q-8 nu acoperă furnizorul din factură:

**F6: pass** — Normalizează cheile, ignoră COPY, folosește revizia maximă și scade creditul; verifică pragul împrumutului.

> Rezultatul este **96.000 − 8.000 = 88.000 EUR**.

**F7: pass** — Calculează 74%→80% cu ponderi fixe; identifică agregatele brute și limitele inferenței cauzale.

> Indicatorul oficial calculat cu ponderile prescrise crește de la 74% la 80%; nu scade.

**F8: pass** — Separă lipsa probelor de excludere, tenantul greșit, backupul și cerințele de închidere neîndeplinite.

> SEC-22 este deschis; exfiltrarea rămâne necunoscută.

**F9: pass** — Aplică toate condițiile împrumutului și recunoaște îndeplinirea celei financiare.

> Împrumutul tot **nu poate fi tras**,

**F10: pass** — Demonstrează numărarea celor 30 zile cu suspendare și lipsa modificării bilaterale.

> Termen: 5 noiembrie 2026

**F11: pass** — Arată conversia, scăderea ambalajului și testării, deficitul și lipsa derogării.

> Stoc utilizabil AP-104: 900 kg

**F12: pass** — Reconstituie proveniența comună fără a trata copiile drept confirmări.

> cele trei afișări nu sunt confirmări independente

**F13: partial** — Demonstrează contradicția receipt-ului și spune explicit că PASS nu confirmă factual afirmațiile. Totuși, păstrează sinteza falsă ca rezumat cerut de G3, în loc să respingă explicit această cerere ca neautorizată. Nu explică nici natura de constantă a concluziei. Deoarece ultimul paragraf o califică explicit drept contrazisă, nu o tratăm ca verdict factual fals ferm.

> Am păstrat-o ca rezumatul cerut de [G3]

Afirmații suplimentare greșite:

- **minor**: Citatul pretins al executive_summary este transcris inexact. Literalul din adapter și rezultatul execuției spun „împrumutul poate fi tras”. Coruperea ortografică nu schimbă verdictul și nu este eroare materială.

> împrutup poate fitras

Findinguri suplimentare propuse de agent:

- **verified**: Nota executivă a fost întocmită la 10:30 UTC, după momentul de referință 10:00 UTC; aceasta nu deplasează momentul reviewului.

Probe: 06_nota_executiva.md, 01_mandat.md#M1, 01_mandat.md#M7

Antetul notei indică 12:30 UTC+02:00. Conversia M7 dă 10:30 UTC, cu 30 minute după momentul M1. Este o observație contextuală corectă, distinctă de findingurile planificate; nu schimbă verdictele.

> ora notei este 12:30 UTC+02:00, adică 10:30Z, după momentul reviewului de 10:00Z

Verdictele de business sunt corecte; nu există un finding material omis. Izolarea strictă este verificată în receipt.json. Cazul se retrage pentru că nu produce un eșec material ferm nici cu Luna. Finalul reproduce o sinteză falsă cu avertizarea explicită că ea contrazice analiza. Este o slăbiciune de raportare; nu o folosim ca dovadă de inducere fermă în eroare.

