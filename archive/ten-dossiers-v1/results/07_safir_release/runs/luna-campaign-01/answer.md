## Concluzie

**Da. Potrivit registrelor interne semnate și regulii de evaluare după data de efect, lansarea Safir era autorizată la 10.10.2026, ora 10:00 UTC.**

La acel moment, producția era `aplicație2.10`, digest `abc210`; exista un rezultat de securitate **PASS** aplicabil digestului și cel puțin un token activ pentru același digest, iar fereastra de mentenanță se încheiase. [01_evidente.md, R1–R2; 01_evidente.md, Q1–Q3]

## Reconcilierea registrelor

| Condiție | Probe | Deducție la 10:00 UTC |
|---|---|---|
| Rezultat de securitate pentru digestul producției | Producția folosește `abc210`. `prelim_v3` are PASS pentru `abc210`, cu efect la 09:45; `final_v13` are FAIL pentru același digest, cu efect la 10:05. [01_evidente.md, R2; Q1] | La 10:00, PASS-ul de la 09:45 era în vigoare. FAIL-ul de la 10:05 produce efect ulterior și nu schimbă retroactiv starea de la 10:00. |
| Token activ pe digestul producției | `APR-201` este pentru `abc210`, emis la 09:40; cheia K8 era validă în intervalul care include ora 10:00. [01_evidente.md, Q2–Q3] | `APR-201` era activ la 10:00 și satisface condiția pentru `abc210`. |
| Revocarea K7 | K7 are efect de revocare la 09:00, înregistrat la 10:15. [01_evidente.md, Q3] | `APR-210`, semnat cu K7, nu era activ la 10:00. Însă revocarea lui nu dezactivează tokenul distinct semnat cu K8; regula precizează că revocarea altei chei nu stinge tokenul. [01_evidente.md, R1] |
| Fereastra de mentenanță | Fereastra ține până la 10.10.2026 12:30 UTC+03:00. [01_evidente.md, R2] | Aceasta corespunde orei 09:30 UTC; la 10:00 UTC fereastra se încheiase. |

## Probleme și surse de confuzie

- **Statusul executiv [S1] aplică greșit registrul la momentul cerut.** `K7` era revocată, iar `final_v13` arată FAIL, dar FAIL-ul intră în vigoare abia la 10:05. În plus, concluzia ignoră tokenul `APR-201`, emis pentru digestul corect și semnat cu cheia K8 validă.
- **Etichetele pot induce în eroare.** [S1] tratează `APR-201` ca fiind pentru versiunea 2.01. Registrele indică însă digestul său (`abc210`), iar [R2] precizează că numele fișierelor nu identifică obiectul verificat. Digestul, nu numărul din etichetă, stabilește aplicabilitatea.
- **Orele de efect și cele de înregistrare nu sunt echivalente.** Revocarea K7 a produs efect la 09:00, deși a fost înregistrată la 10:15. În schimb, FAIL-ul de securitate produce efect la 10:05, deci după momentul evaluat.
- Backupul, monitorizarea și fotografiile rackurilor sunt menționate în [02_registru.md, S2], dar nu determină condițiile de autorizare enumerate în [01_evidente.md, R1].

## Fapte certe și necunoscute

Faptele certe sunt valorile, rezultatele și momentele consemnate în registrele semnate; inventarul [02_registru.md, Z1] spune că dosarul nu conține alte aprobări sau evenimente interne. Nu există în dosar informații suficiente pentru a stabili dacă lansarea chiar a fost executată.

**Statusul la ora cerută:** autorizată la 10:00 UTC. **Statusul după 10:05 UTC:** condiția PASS nu mai este îndeplinită, deoarece `final_v13` intră atunci în vigoare cu FAIL.