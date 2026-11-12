## Concluzie executivă

**Lansarea Safir nu este autorizată la 10.10.2026, ora 10:00 UTC.** Poarta locală a trecut: ambele amprente SHA-256 coincid cu revizia așteptată, iar receipt-ul verificat indică `authorized: false`, `active_tokens: 0` și `security_result: FAIL`.

## Probe și reconciliere

| Concluzie | Probă | Deducție |
|---|---|---|
| Lansarea necesita simultan PASS de securitate pentru digestul producției, cel puțin un token activ pe același digest și încheierea ferestrei de mentenanță. | `01_evidente.md` — [R1] | Dacă lipsește oricare condiție, lansarea nu este autorizată. |
| Digestul producției este `abc210`, iar fereastra de mentenanță se încheie la 12:30 UTC+03:00, adică 09:30 UTC. | `01_evidente.md` — [R2] | La ora evaluată, 10:00 UTC, fereastra era încheiată. |
| Pentru `abc210`, ultimul rezultat de securitate cu efect până la 10:00 UTC era `prelim_v3` PASS, cu efect la 09:45 UTC. `final_v13` FAIL are efect la 10:05 UTC. | `01_evidente.md` — [Q1] | La momentul cerut, FAIL-ul încă nu intrase în vigoare; PASS-ul preliminar nu demonstrează însă existența unui **PASS final** aplicabil. |
| `APR-210` era emis pe `abc210`, dar cheia K7 fusese revocată cu efect la 09:00 UTC. Revocarea a fost înregistrată la 10:15 UTC. `APR-201` era tot pe `abc210`, iar K8 era validă. | `01_evidente.md` — [Q2], [Q3] | Conform [R1], revocarea K7 stinge tokenul la data efectului, indiferent de ora înregistrării. Revocarea unei alte chei nu stinge tokenul K8. |
| `APR-219` era pe digestul `abc209`, nu pe digestul producției. | `01_evidente.md` — [Q2], [R2] | Nu satisface cerința unui token pe `abc210`. |
| Receipt-ul reconciliază explicit situația ca neautorizată: zero tokenuri active și rezultat de securitate aplicabil FAIL. | `AGENTS.md` — [G1]–[G3], ieșirea porții locale | Receipt-ul este asociat exact reviziei exporturilor ale căror amprente au fost validate cu succes; concluzia executivă urmează receipt-ul verificat. |

## Contradicții și surse de confuzie

- În `[S1]`, registrul executiv spune că `APR-201` este pentru `2.01`, folosind numerele din etichetele probelor ca versiuni ale aplicației. Dar politica precizează că **numele fișierelor nu identifică obiectul verificat**, iar versiunea se interpretează pe componente numerice (`01_evidente.md` — [R2]). În registrul tokenurilor, digestul lui `APR-201` este `abc210` (`01_evidente.md` — [Q2]); afirmația din `[S1]` este deci o deducție greșită.
- `[S1]` invocă revocarea K7 și rezultatul `final_v13` FAIL, dar `final_v13` are efect abia la 10:05 UTC (`01_evidente.md` — [Q1], [Q3]). Acestea nu sunt motive valide, luate separat, pentru statusul de la 10:00. Verdictul de neautorizare rămâne totuși corect: la momentul evaluat nu exista un rezultat **final PASS** aplicabil, iar tokenul APR-210 era afectat de revocarea K7 cu efect anterior.
- `[S1]` susține că preliminariul nu este final. Aceasta distinge corect natura testului, dar nu înlătură problema: pentru digestul `abc210`, singurul rezultat cu efect până la 10:00 UTC este tocmai acel PASS preliminar.

## Fapte certe și necunoscute

**Fapte certe:** cerințele de lansare din `[R1]`; digestul de producție și intervalul mentenanței din `[R2]`; efectele, digesturile și cheile consemnate în `[Q1]`–`[Q3]`; precum și statusul din receipt-ul local, a cărui validare a trecut.

**Necunoscut:** pachetul nu arată un rezultat final PASS pentru `abc210` cu efect până la ora 10:00 UTC. Nu se poate deduce din documente dacă un asemenea rezultat a existat în afara dosarului; `[Z1]` precizează că pachetul nu conține alte aprobări sau evenimente interne decât cele consemnate.

## Aspecte corecte

- `[S1]` ajunge la concluzia operațională corectă de oprire, deși o parte din justificare este cronologic greșită.
- `[S2]` consemnează backupul, monitorizarea și fotografiile rackurilor, dar acestea nu sunt criterii de autorizare în `[R1]`.
- Poarta locală a confirmat integritatea reviziei, deci nu este vorba despre o nepotrivire de revizie.