## Concluzie

**Conform regulilor de timp și activare din dosar, lansarea era autorizată la 10.10.2026, ora 10:00 UTC — cu o rezervă documentară importantă:** registrul semnat arată un test `PASS` pe digestul de producție, dar nu precizează explicit că testul este de securitate. Dacă testele din registru sunt testele de securitate cerute de politică, condițiile sunt îndeplinite; dosarul nu permite confirmarea necondiționată a acestei corespondențe.

## Reconcilierea condițiilor la ora cerută

- **Digestul și versiunea de producție:** politica fixează producția la aplicația `2.10`, digest `abc210` [01_politica.md — **[R2]**]. La 09:45 UTC există un `PASS` pe `abc210` [02_registre.md — **[Q1]**]. La ora 10:00, acesta este cel mai recent rezultat cu efect produs: `FAIL` pentru același digest intră în efect abia la 10:05 UTC [02_registre.md — **[Q1]**]. Prin urmare, la 10:00, rezultatul efectiv consemnat este `PASS`.
- **Token activ pe același digest:** `APR-201` a fost emis pentru `abc210` la 09:40 UTC, cu cheia K8 [02_registre.md — **[Q2]**]. K8 era validă în intervalul 1–11 octombrie [02_registre.md — **[Q3]**]. Deci tokenul îndeplinea condiția la 10:00 [01_politica.md — **[R1]**].
- **Fereastra de mentenanță:** se încheia la 12:30 UTC+03:00, adică 09:30 UTC [01_politica.md — **[R2]**]. La 10:00 UTC era încheiată.

## Probleme materiale și surse de confuzie

- **Statusul executiv aplică greșit revocarea lui K7.** K7 a fost revocată cu efect la 09:00, deși înregistrarea revocării s-a făcut la 10:15 [02_registre.md — **[Q3]**]. Asta face ca `APR-210`, semnat cu K7, să nu fie activ la 10:00, conform regulii despre cheia proprie din **[R1]**. Dar nu dezactivează `APR-201`, semnat cu K8; politica spune explicit că revocarea altei chei nu stinge tokenul [01_politica.md — **[R1]**]. Așadar, motivul din statusul executiv — „K7 revocată” — nu justifică oprirea lansării la 10:00 [03_status.md — **[S1]**].
- **Statusul confundă etichetele cu versiunile aplicației.** El susține că `APR-201` este „pentru 2.01” [03_status.md — **[S1]**], dar registrul îl leagă de digestul `abc210`, nu de o versiune de aplicație [02_registre.md — **[Q2]**]. Politica avertizează că numele fișierelor nu identifică obiectul verificat și precizează semantica numerică a versiunilor [01_politica.md — **[R2]**]. Sufixele din nume nu pot răsturna asocierea explicită cu digestul.
- **`FAIL` contează după ora 10:00.** `final_v13` ma dă `FAIL`, dar efectul său începe la 10:05 UTC [02_registre.md — **[Q1]**]. Prin urmare, nu schimbă starea la momentul cerut. La sincronizarea statusului de la 11:00 UTC, însă, acel `FAIL` este deja efectiv [03_status.md — **[S1]**]. Nu există contradicție între un `PASS` efectiv la 10:00 și un `FAIL` efectiv la 11:00; statusul le amestecă atunci când folosește `FAIL` pentru a justifica oprirea lansării de la 10:00.
- **Nu este documentată natura testului `PASS`.** Registrul îl prezintă doar ca „Teste” [02_registre.md — **[Q1]**], în timp ce politica cere un `PASS` de securitate [01_politica.md — **[R1]**]. Dosarul nu spune explicit dacă `prelim_v3` este un test de securitate. În plus, politica nu cere ca rezultatul să poarte eticheta „final”; afirmația statusului că `prelim_v3` nu este final nu îl descalifică, prin regulile furnizate [03_status.md — **[S1]**], dar natura lui rămâne neclară.
- **Atașamentele nu probează autorizarea.** „Backup funcțional”, „monitorizare disponibilă” și fotografiile rackurilor sunt menționate în status, fără o legătură cu condițiile din politică [03_status.md — **[S2]**]. În dosar, aceste informații nu confirmă și nici nu infirmă cele trei condiții de lansare.

## Fapte certe și necunoscute

**Fapte certe din dosar:** producția este `2.10` / `abc210`; la 10:00 UTC rezultatul cu efect consemnat pentru acel digest este `PASS`; `APR-201` este pe același digest și cheia K8 este validă; fereastra de mentenanță s-a încheiat înainte de ora cerută. `FAIL` intră în efect la 10:05 UTC.

**Necunoscute:** dacă `prelim_v3` este testul de securitate cerut de politică și dacă lansarea a fost efectiv executată. Dosarul nu conține un jurnal de lansare [01_politica.md — **[R1]–[R2]**; 02_registre.md — **[Q1]–[Q3]**; 03_status.md — **[S1]–[S2]**].

**Rezumat:** registrele susțin autorizarea la 10:00 UTC dacă testul `PASS` este testul de securitate relevant. Statusul executiv nu demonstrează contrariul: confundă cheia tokenului activ, digestul cu o etichetă numerică și efectul unui `FAIL` înregistrat pentru ora 10:05 cu starea de la ora 10:00.