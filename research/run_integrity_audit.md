# Audit al integrității execuției — pilot-v1

Data: 2026-11-12. Audit read-only realizat de agentul `method_audit`. Nu am modificat runnerul, pachetul înghețat sau sursele acestuia. Nu am citit `answer.md` și am exclus mesajele de tip `agent_message` din inspecția transcriptelor. Identitățile modelelor sunt vizibile în receipts; acest audit verifică integritatea execuției, nu corectitudinea semantică a răspunsurilor.

## Înghețare și alocare

Freeze SHA-256: `c171a39fe8b5e5fd621fd5fe73f21926e1fa8ba5634b278492dff3dca6aee146`.

- Toate cele 73 de fișiere înghețate corespund hashurilor; cele trei surse runtime active corespund copiilor înghețate.
- Pachetul are 12 dosare neutru identificate, patru fișiere de documente fiecare. Inventarul din `eval/` coincide exact cu inventarul înghețat; referințele, rubricile, manifestul și rapoartele de audit sunt în afara intrărilor.
- Alocarea primară este de 24 de sesiuni: 12 pentru `gpt-6.1-terra`, 12 pentru `gpt-6.1-sol`. Ambele au profil `standard`, efort `medium` și timeout 600 secunde.
- `verify_allocation` refuză un run nealocat, alt model, alt profil, alt efort, alt timeout sau alt set de dosare. `run_eval.py --suite` refuză modul de izolare `context`.
- `research/test_campaign_guards.py` a trecut: modificarea probelor, modificarea runtime-ului, introducerea unui fișier suplimentar și modificarea alocării sunt respinse.

## Verificări pe sesiuni

Pentru fiecare receipt finalizat inclus în checkpoint am verificat independent:

1. `started.json` și `receipt.json` indică același dosar, model, timp de început și hash de freeze; începutul este după momentul înghețării.
2. Hashul promptului efectiv salvat coincide cu receipt-ul și cu hashul preînregistrat pentru acel dosar.
3. Inventarul și hashurile fiecărui snapshot coincid cu `eval/` înghețat și cu `input_sha256`; sunt exact patru documente. Nici etalonul, nici răspunsurile sau judecățile altor sesiuni nu apar în snapshot.
4. Receipt-ul indică `inputs_unchanged=true`, `freeze_unchanged=true` și preflight strict trecut. Comanda începe cu `bwrap`, conține `--clearenv`, montează cazul la `/case` read-only și livrează răspunsul la `/output/answer.md`.
5. Toate verificările de mediu, ascundere a proiectului/configurației/tmp, izolare prin `/proc/self/root` și imposibilitate de scriere a cazului sunt prezente și trecute.
6. ID-urile `thread.started` sunt distincte. Sesiunile nu sunt continuări ale aceleiași conversații.
7. Pentru expunere, am inspectat exclusiv comenzile și rezultatele `command_execution`. Am normalizat numai prefixele de numerotare produse de `nl -ba` și am verificat prezența tuturor liniilor ne-goale din fiecare document în rezultatele toolurilor. Acesta este un control al disponibilității textului la interfața observabilă, nu o dovadă despre atenția internă a modelului.

Audit final al lotului primar la `2026-11-12T12:57:31.227996+00:00`: **24/24 receipts finalizate, 24 sesiuni distincte, toate cu status `completed`, 96/96 documente expuse integral în tool results**, fără erori JSON sau comenzi eșuate. Am inspectat toate comenzile: numai enumerări și citiri locale ale dosarului, fără acces la rețea, alte dosare sau rezultate de evaluare. Ordinea celor 12 sesiuni din fiecare lot coincide cu ordinea preînregistrată. Cele 24 directoare private de lucru/runtime/livrare au fost șterse după încheiere.

| Dosar | Run | Snapshot/hashuri | Expunere documente | Status tehnic |
|---|---|---|---|---|
| d2897 | pilot-sol | conforme | 4/4 | completed |
| d2897 | pilot-terra | conforme | 4/4 | completed |
| d3881 | pilot-sol | conforme | 4/4 | completed |
| d3881 | pilot-terra | conforme | 4/4 | completed |
| d4366 | pilot-sol | conforme | 4/4 | completed |
| d4366 | pilot-terra | conforme | 4/4 | completed |
| d4452 | pilot-sol | conforme | 4/4 | completed |
| d4452 | pilot-terra | conforme | 4/4 | completed |
| d4989 | pilot-sol | conforme | 4/4 | completed |
| d4989 | pilot-terra | conforme | 4/4 | completed |
| d5092 | pilot-sol | conforme | 4/4 | completed |
| d5092 | pilot-terra | conforme | 4/4 | completed |
| d6801 | pilot-sol | conforme | 4/4 | completed |
| d6801 | pilot-terra | conforme | 4/4 | completed |
| d7266 | pilot-sol | conforme | 4/4 | completed |
| d7266 | pilot-terra | conforme | 4/4 | completed |
| d8133 | pilot-sol | conforme | 4/4 | completed |
| d8133 | pilot-terra | conforme | 4/4 | completed |
| d8770 | pilot-sol | conforme | 4/4 | completed |
| d8770 | pilot-terra | conforme | 4/4 | completed |
| d9278 | pilot-sol | conforme | 4/4 | completed |
| d9278 | pilot-terra | conforme | 4/4 | completed |
| d9895 | pilot-sol | conforme | 4/4 | completed |
| d9895 | pilot-terra | conforme | 4/4 | completed |

Lotul primar este complet din punct de vedere tehnic. Acest audit nu cuprinde lotul secundar Luna sau o eventuală confirmare.

## Limite și condiții procedurale

- Câmpul `secondary_if_no_primary_error` din alocarea Luna este declarativ; `verify_allocation` nu execută condiția semantică. Operatorul trebuie să documenteze terminarea și judecarea lotului primar înainte de a lansa acel lot secundar. Nu am identificat o încălcare a condiției la checkpoint.
- Hashurile din freeze și alocarea sunt verificabile, dar nu sunt ancorate într-un registru extern care ar împiedica rescrierea deliberată de către operator. `started.json` și receipts fixează hashul folosit în fiecare sesiune. Aceasta este trasabilitate în cadrul experimentului, nu notarizare externă.
- Runnerul verifică pachetul înaintea fiecărei sesiuni și verifică egalitatea hashurilor copiilor cu freeze la încheiere. O cursă de modificare exact între verificarea inițială și copiere ar fi detectată ulterior și ar invalida sesiunea. În checkpoint, toate egalitățile au trecut.
- Codul folosește `assert` pentru verificările de integritate. Comenzile de rulare ale pilotului folosesc Python normal, fără `-O`; pentru un instrument distribuit, validările critice ar trebui să folosească excepții explicite. Nu modifica runtime-ul în mijlocul pilotului.
- Izolarea filesystem și a mediului nu echivalează cu blocarea întregii rețele: CLI trebuie să contacteze backendul. Comenzile și toolurile sunt inspectate pentru surse externe; absența lor în transcript nu certifică toate componentele backendului.
- Versiunea CLI este în receipts, iar modelul este identificatorul cerut. Identitatea internă a backendului și hashul complet al toolchainului instalat nu sunt atestate independent.
- Auditul structural nu acordă scoruri de business și nu concluzionează că un model a rezistat sau a fost păcălit. Acea etapă folosește pachetele anonime și rubrica înghețată.
