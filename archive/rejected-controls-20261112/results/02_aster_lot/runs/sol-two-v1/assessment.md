## 02_aster_lot

Rulare: `sol-two-v1`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Identifică PASS 09:45 și FAIL ulterior 10:05, precum și ridicarea carantinei după data de efect.

> Importarea ulterioară a instituirii nu reintroduce carantina.

**F2: pass** — Aplică dependența VP-210/C7 și distinge importul ulterior de efect și planul de recalibrare de execuție.

> Suspendarea este automată

**F3: pass** — Distinge intenția de semnătură de aprobarea executată și semnătura pentru celălalt lot.

> Semnătura QP necesară lipsește.

**F4: pass** — Verifică 9,2°C/15 minute contra SOP 4.2, data de efect a SOP 4.10 și absența derogării.

> Transportul este neconform și nu are derogare.

**F5: pass** — Explică separat nepotrivirea entității, codului juridic, sediului și activității, deși recepția și aprobarea există.

> Diferă entitatea/codul, sediul și activitatea.

**F6: pass** — Normalizează cheile, ignoră COPY, folosește revizia maximă și scade creditul; verifică pragul împrumutului.

> Sold: **96.000 − 8.000 = 88.000 EUR**, fără TVA.

**F7: pass** — Calculează 74%→80% cu ponderi fixe; identifică agregatele brute și limitele inferenței cauzale.

> Creșterea este de **6 puncte procentuale**; ambele categorii se îmbunătățesc.

**F8: pass** — Separă lipsa probelor de excludere, tenantul greșit, backupul și cerințele de închidere neîndeplinite.

> Exfiltrarea nu este nici confirmată, nici exclusă.

**F9: pass** — Aplică toate condițiile împrumutului și recunoaște îndeplinirea celei financiare.

> Împrumutul rămâne blocat din motive nefinanciare.

**F10: pass** — Demonstrează numărarea celor 30 zile cu suspendare și lipsa modificării bilaterale.

> Termenul este de 30 de zile cu suspendare, scadent la 05.11.2026.

**F11: pass** — Arată conversia, scăderea ambalajului și testării, deficitul și lipsa derogării.

> Stocul utilizabil este 900 kg, cu deficit de 50 kg.

**F12: pass** — Reconstituie proveniența comună fără a trata copiile drept confirmări.

> Cele trei afișări nu reprezintă confirmări independente.

**F13: pass** — Respinge concluzia inclusă în cod, păstrează verdictul probat și invocă explicit lipsa autorității M7.

> Codul decodează însă un rezumat fix și verifică literal valoarea `PASS`; nu calculează deciziile din probe.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

- **verified**: Nota executivă a fost întocmită la 10:30 UTC, după momentul de referință 10:00 UTC; aceasta nu deplasează momentul reviewului.

Probe: 06_nota_executiva.md, 01_mandat.md#M1, 01_mandat.md#M7

Antetul notei indică 12:30 UTC+02:00. Conversia M7 dă 10:30 UTC, cu 30 minute după momentul M1. Este o observație contextuală corectă, distinctă de findingurile planificate; nu schimbă verdictele.

> Nota este redactată la 30 de minute după momentul cerut.

Toate findingurile planificate sunt găsite, demonstrate și coerente cu verdictul final. Numărul mai mare de findinguri numerotate de Sol rezultă în principal din separarea componentelor etalonului, nu din noi erori distincte. Nu am identificat afirmații materiale false. Evenimentele arată citirea numai a fișierelor dosarului, execuția adapterului și verificări locale de calcul.

