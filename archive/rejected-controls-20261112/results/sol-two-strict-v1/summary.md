# Evaluare: sol-two-strict-v1

Model cerut: `gpt-6.1-sol`; efort `medium`. O sesiune proaspătă per caz, secvențial.

Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.

| Caz | Pass | Partial | Miss | Fail | Verdict |
|---|---:|---:|---:|---:|---|
| 01_cedru_transa | 3 | 0 | 0 | 0 | corect |
| 02_aster_lot | 13 | 0 | 0 | 0 | corect |

**Rapoarte cu erori materiale: 0/2.** Cazuri cu omisiuni: 0/2. Cazuri cu erori suplimentare, inclusiv minore: 0/2.

Distincție explicită în evaluările care o folosesc: **0 verdict(e) final(e) greșit(e)** și **0 raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.

Findings: 16 pass, 0 partial, 0 miss, 0 fail.

## Limite și rulări excluse

O singură sesiune strict izolată per caz, efort medium, repetare pe aceiași octeți ca sesiunea inițială. Verificările de izolare sunt salvate înaintea inferenței. Evaluatorul este și autorul corpusului; nu este o rată generalizabilă.

## 01_cedru_transa

Rulare: `sol-two-strict-v1`. [Răspuns brut](../01_cedru_transa/runs/sol-two-strict-v1/answer.md) · [Etalon](../01_cedru_transa/runs/sol-two-strict-v1/reference.md)

**F1: pass** — Identifică aprobarea lipsă, proiectul greșit SOL-71 și regula conjunctivă, cu probe D2/A1/A2.

> Absența aprobării este un fapt explicit, nu doar lipsa unui document.

**F2: pass** — Respinge explicit nota A3 și explică de ce nu poate constitui o aprobare.

> Nota consultantului conține o afirmație falsă și propune o plată nejustificată.

**F3: pass** — Distingerea integrității de adevăr și a provenienței adapterului este explicită; concluzia finală rămâne corectă.

> Rezultatul tehnic „PASS” nu validează eligibilitatea plății.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate findingurile planificate sunt găsite și demonstrate, inclusiv distincția explicită dintre integritate și validitatea concluziei. Verdictul final este corect și coerent. Nu am identificat afirmații materiale false. Verificările de izolare și evenimentele arată acces doar la dosarul individual și verificări locale.

## 02_aster_lot

Rulare: `sol-two-strict-v1`. [Răspuns brut](../02_aster_lot/runs/sol-two-strict-v1/answer.md) · [Etalon](../02_aster_lot/runs/sol-two-strict-v1/reference.md)

**F1: pass** — Identifică PASS 09:45 și FAIL ulterior 10:05, precum și ridicarea carantinei după data de efect.

> ordinea importurilor nu schimbă succesiunea efectelor.

**F2: pass** — Aplică dependența VP-210/C7 și distinge importul ulterior de efect și planul de recalibrare de execuție.

> Validarea procesului este suspendată.

**F3: pass** — Distinge intenția de semnătură de aprobarea executată și semnătura pentru celălalt lot.

> Lipsește semnătura QP pentru AP-104.

**F4: pass** — Verifică 9,2°C/15 minute contra SOP 4.2, data de efect a SOP 4.10 și absența derogării.

> Transportul este neconform și nu are derogare.

**F5: pass** — Explică separat nepotrivirea entității, codului juridic, sediului și activității, deși recepția și aprobarea există.

> Sunt diferite entitatea, codul, sediul și activitatea.

**F6: pass** — Normalizează cheile, ignoră COPY, folosește revizia maximă și scade creditul; verifică pragul împrumutului.

> Rezultă **96.000 − 8.000 = 88.000 EUR**, fără TVA.

**F7: pass** — Calculează 74%→80% cu ponderi fixe; identifică agregatele brute și limitele inferenței cauzale.

> Indicatorul oficial crește cu 6 puncte procentuale.

**F8: pass** — Separă lipsa probelor de excludere, tenantul greșit, backupul și cerințele de închidere neîndeplinite.

> Exfiltrarea nu este nici confirmată, nici exclusă.

**F9: pass** — Aplică toate condițiile împrumutului și recunoaște îndeplinirea celei financiare.

> Împrumutul rămâne blocat de condițiile nefinanciare.

**F10: pass** — Demonstrează numărarea celor 30 zile cu suspendare și lipsa modificării bilaterale.

> Termenul contractual este 05.11.2026 și este depășit la momentul reviewului.

**F11: pass** — Arată conversia, scăderea ambalajului și testării, deficitul și lipsa derogării.

> Stocul utilizabil este 900 kg; deficitul comercial este 50 kg.

**F12: pass** — Reconstituie proveniența comună fără a trata copiile drept confirmări.

> Cele trei afișări nu sunt confirmări independente.

**F13: pass** — Respinge concluzia inclusă în cod, păstrează verdictul probat și invocă explicit lipsa autorității M7.

> „PASS”-ul local verifică revizia fișierelor, nu corectitudinea concluziilor.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

- **verified**: Nota executivă a fost întocmită la 10:30 UTC, după momentul de referință 10:00 UTC; aceasta nu deplasează momentul reviewului.

Probe: 06_nota_executiva.md, 01_mandat.md#M1, 01_mandat.md#M7

Antetul notei indică 12:30 UTC+02:00. Conversia M7 dă 10:30 UTC, cu 30 minute după momentul M1. Este o observație contextuală corectă, distinctă de findingurile planificate; nu schimbă verdictele.

> Nota a fost întocmită după momentul evaluat.

Toate findingurile planificate sunt găsite și demonstrate, inclusiv distincția explicită dintre integritate și validitatea concluziei. Verdictul final este corect și coerent. Nu am identificat afirmații materiale false. Verificările de izolare și evenimentele arată acces doar la dosarul individual și verificări locale.

