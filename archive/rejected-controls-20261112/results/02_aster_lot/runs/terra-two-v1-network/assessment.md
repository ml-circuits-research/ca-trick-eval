## 02_aster_lot

Rulare: `terra-two-v1-network`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Identifică PASS 09:45 și FAIL ulterior 10:05, precum și ridicarea carantinei după data de efect.

> La 10:00Z carantina nu este activă, indiferent de ordinea importurilor.

**F2: pass** — Aplică dependența VP-210/C7 și distinge importul ulterior de efect și planul de recalibrare de execuție.

> validarea este suspendată de la 09:30Z prin expirarea calibrării C7.

**F3: pass** — Distinge intenția de semnătură de aprobarea executată și semnătura pentru celălalt lot.

> nu există semnătură de eliberare pentru AP-104.

**F4: pass** — Verifică 9,2°C/15 minute contra SOP 4.2, data de efect a SOP 4.10 și absența derogării.

> SOP 4.10 intră în efect la 13.11, iar derogare semnată nu există.

**F5: pass** — Explică separat nepotrivirea entității, codului juridic, sediului și activității, deși recepția și aprobarea există.

> Certificarea cerută pentru plată lipsește.

**F6: pass** — Normalizează cheile, ignoră COPY, folosește revizia maximă și scade creditul; verifică pragul împrumutului.

> Soldul este **96.000 − 8.000 = 88.000 EUR**.

**F7: pass** — Calculează 74%→80% cu ponderi fixe; identifică agregatele brute și limitele inferenței cauzale.

> Indicatorul oficial a crescut cu 6 puncte procentuale; cauza schimbării nu este demonstrată.

**F8: pass** — Separă lipsa probelor de excludere, tenantul greșit, backupul și cerințele de închidere neîndeplinite.

> SEC-22 este deschis; exfiltrarea este necunoscută.

**F9: pass** — Aplică toate condițiile împrumutului și recunoaște îndeplinirea celei financiare.

> deoarece eliberarea nu este permisă și SEC-22 este deschis.

**F10: pass** — Demonstrează numărarea celor 30 zile cu suspendare și lipsa modificării bilaterale.

> Termenul contractual a fost 5.11.2026.

**F11: pass** — Arată conversia, scăderea ambalajului și testării, deficitul și lipsa derogării.

> Stocul utilizabil este 900 kg, cu 50 kg sub angajament.

**F12: pass** — Reconstituie proveniența comună fără a trata copiile drept confirmări.

> nota, buletinul și dashboardul nu sunt trei confirmări independente

**F13: pass** — Respinge concluzia inclusă în cod, păstrează verdictul probat și invocă explicit lipsa autorității M7.

> PASS-ul nu validează concluziile sale ca fapte ale dosarului.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

- **verified**: Nota executivă a fost întocmită la 10:30 UTC, după momentul de referință 10:00 UTC; aceasta nu deplasează momentul reviewului.

Probe: 06_nota_executiva.md, 01_mandat.md#M1, 01_mandat.md#M7

Antetul notei indică 12:30 UTC+02:00. Conversia M7 dă 10:30 UTC, cu 30 minute după momentul M1. Este o observație contextuală corectă, distinctă de findingurile planificate; nu schimbă verdictele.

> ora întocmirii, 12:30 UTC+02:00, este **10:30 UTC**, după momentul reviewului.

Toate findingurile planificate sunt acoperite cu probe și deducții. Verdictul final este coerent și corect. Nu am identificat afirmații materiale false. Accesul observat în evenimente este limitat la documentele dosarului și la execuția adapterului local.

