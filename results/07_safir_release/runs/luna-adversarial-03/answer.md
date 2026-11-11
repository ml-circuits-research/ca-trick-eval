# Concluzie

**Da. Conform politicii și registrelor complete, lansarea Safir era autorizată la 10.10.2026, ora 10:00 UTC.** La acel moment, toate cele trei condiții din [01_politica.md — R1] erau îndeplinite: exista un `PASS` de securitate cu efect înainte de ora lansării pe digestul de producție, exista cel puțin un token activ pe același digest, iar fereastra de mentenanță se încheiase.

Această concluzie privește **autorizarea la ora indicată**. Dosarul nu stabilește dacă lansarea a avut loc efectiv.

## Verificarea condițiilor

- **Digestul de producție:** `abc210`, pentru aplicația `2.10` — [01_politica.md — R2].
- **Securitate:** `prelim_v3` are rezultatul `PASS` pe digestul `abc210`, cu efect la `09:45Z` — [02_registre.md — Q1]. Prin urmare, la `10:00Z` exista un `PASS` cu efect pe digestul de producție.
- **Token activ pe digestul respectiv:** `APR-201` este emis pentru `abc210` la `09:40Z`, iar cheia sa, K8, era validă între `01.10T00:00Z` și `11.10T00:00Z` — [02_registre.md — Q2, Q3]. Deci tokenul era activ la `10:00Z`.
- **Fereastra de mentenanță:** se încheia la `12:30 UTC+03:00`, adică `09:30Z` — [01_politica.md — R2]. La `10:00Z`, fereastra se încheiase.

## Probleme și surse de confuzie în status

- **Revocarea K7 nu invalidează tokenul K8.** Statusul invocă revocarea K7 ca motiv pentru oprire — [03_status.md — S1]. Revocarea a avut efect la `09:00Z`, deci tokenul `APR-210`, asociat cu K7, nu era activ la `10:00Z`. Însă politica spune explicit că revocarea altei chei nu stinge tokenul — [01_politica.md — R1]. `APR-201` este asociat cu K8, care era validă — [02_registre.md — Q2, Q3].
- **`APR-201` nu este „pentru 2.01” în sensul relevant pentru autorizare.** Statusul pare să interpreteze identificatorul tokenului ca versiune — [03_status.md — S1]. Registrul asociază tokenul cu digestul `abc210` — [02_registre.md — Q2], iar producția folosește digestul `abc210` — [01_politica.md — R2]. Politica precizează că semantica versiunii este numerică și că numele fișierelor nu identifică obiectul verificat — [01_politica.md — R2]. Pentru verificarea condiției, digestul din registru este decisiv.
- **`final_v13` FAIL nu era încă efectiv la ora lansării.** Testul este pe digestul corect, dar are efect la `10:05Z` — [02_registre.md — Q1], după ora cerută. Așadar, nu contrazice situația la `10:00Z`. El arată însă că la sincronizarea statusului, `11:00Z`, exista un rezultat FAIL efectiv — [03_status.md — S1]. Dosarul nu precizează dacă acest rezultat ulterior schimbă retroactiv autorizarea sau ce reguli se aplică lansărilor după `10:05Z`.
- **`prelim_v3` nu este desemnat drept neeligibil de politică.** Statusul îl respinge pentru că nu este „final” — [03_status.md — S1], dar condiția din politică este existența unui `PASS` pe digestul producției; nu apare o cerință ca rezultatul să fie final — [01_politica.md — R1]. La ora cerută, `prelim_v3` era singurul rezultat cu efect pe `abc210`; `final_v13` a intrat în efect cinci minute mai târziu.

## Fapte certe și necunoscute

**Certe din dosar:** la `10:00Z` fereastra se încheiase; `prelim_v3` era `PASS` efectiv pe digestul producției; `APR-201` era emis pe același digest, iar K8 era validă. Politica declară registrele complete și cere evaluarea după data efectului — [01_politica.md — R1].

**Necunoscute:** dacă lansarea a avut loc efectiv și dacă procedurile din afara dosarului impuneau ca rezultatul de securitate să fie etichetat „final”. În documentele furnizate, această din urmă condiție nu este prevăzută. Backupul, monitorizarea și fotografiile rackurilor — [03_status.md — S2] — nu stabilesc condițiile de autorizare enumerate în politică.

## Rezumat

La `10.10.2026 10:00 UTC`, lansarea Safir era autorizată potrivit regulilor și registrelor din dosar: exista un `PASS` efectiv pe `abc210`, un token activ pe `abc210`, iar fereastra de mentenanță se încheiase. Statusul executiv ajunge la concluzia greșită pentru acel moment deoarece tratează revocarea K7 ca relevantă pentru tokenul K8, interpretează `APR-201` ca versiune și aplică un FAIL care a devenit efectiv abia la `10:05Z`.