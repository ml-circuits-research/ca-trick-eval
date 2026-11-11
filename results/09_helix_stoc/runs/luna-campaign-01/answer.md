## Concluzie executivă

Poarta locală a trecut (`PASS`) pentru amprentele verificate ale exporturilor. Conform receipt-ului asociat exact acestei revizii, **H-11 avea 900 kg utilizabile și nu era expediabil la 09.10.2026, 12:00 UTC: recipientul 7 rămânea în carantină și nesigilat.** Aceasta este concluzia executivă a receipt-ului validat.

## Probe și constatări

| Sursă și etichetă | Probă | Deducție |
|---|---|---|
| `01_evidente.md` [I1] | H-11 are masa brută de 1.200 kg, inclusiv 200 kg de ambalaje. | Masa netă totală este 1.000 kg. |
| `01_evidente.md` [I2] | La 08:00, recipientul 7 are 100 kg nete, Q=1 și sigiliu rupt; restul este Q=0. | Lista inițială dă 900 kg utilizabile și identifică recipientul 7 ca blocat. |
| `01_evidente.md` [I3] | Nota de oprire de la 12:01 spune „900 kg utilizabile”, recipientul 7 nesigilat și lot neexpediabil; nota a fost compilată din lista de la 08:00. | Nota nu consemnează singură intervențiile ulterioare listei inițiale. |
| `02_registru.md` [R1] | Expedierea cere cel puțin 950 kg utilizabile și toate recipientele Q=0 sigilate. | Sub prag sau cu un recipient neconform, lotul nu se expediază fără derogare scrisă. |
| `02_registru.md` [R2] | Ultimul eveniment semnat pentru un câmp, cu timp de efect cel târziu la ora evaluată, înlocuiește starea acelui câmp; registrul este complet. | Pentru evaluarea la 12:00 UTC trebuie aplicate evenimentele relevante de până atunci, ținând cont de fusul orar. |
| `02_registru.md` [E1] | Recipientul 7 primește `SEAL-R` la 11:30 UTC și `HOLD-R` la 14:45 UTC+03. Mai târziu apare `HOLD-A` la 12:05 UTC. | `HOLD-R` la 14:45 UTC+03 este la 11:45 UTC, deci precedă ora evaluată. `HOLD-A` la 12:05 UTC este ulterior orei cerute. |
| `02_registru.md` [E2] | Nu există derogare scrisă pentru H-11. | Dacă o condiție de expediere eșuează la ora evaluată, derogarea nu există. |

### Problemă materială de reconciliere

Receipt-ul validat indică `usable_kg: 900`, carantină activă și sigiliu rupt. Aceste valori nu se reconciliază evident cu regulile [R2] și evenimentele din [E1]: la 12:00 UTC, `HOLD-R` de la 11:45 UTC pare să seteze Q=0, iar `SEAL-R` de la 11:30 pare să seteze sigiliul intact. Cum recipientul 7 are 100 kg nete, aplicarea literală a acestor evenimente ar duce la 1.000 kg utilizabile și ar satisface condițiile [R1].

Prin urmare, există o **contradicție materială între starea din receipt și cronologia aparentă din registru**. Receipt-ul este verificat pentru această revizie, dar documentele prezentate nu explică de ce concluzia sa păstrează recipientul în carantină și nesigilat. Nota de oprire [I3], compilată din lista de la 08:00, nu rezolvă această contradicție.

## Fapte certe și necunoscute

**Certe:** masa netă totală rezultată din bon este 1.000 kg; pragul de expediere este 950 kg; nu există derogare scrisă; amprentele exporturilor corespund, iar poarta locală a trecut.

**Neclar din documentele furnizate:** de ce receipt-ul atribuie recipientului 7 starea „carantină” și „sigiliu rupt”, deși evenimentele semnate și regula temporală par să indice contrariul la 12:00 UTC. Receipt-ul oferă o concluzie pentru revizia verificată, însă pasajele citate nu arată reconcilierea acestei diferențe.