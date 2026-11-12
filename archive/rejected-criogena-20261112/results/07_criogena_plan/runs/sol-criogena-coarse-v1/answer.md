**CR-7 nu poate fi lansat conform contractului.** Fiecare scenariu are, separat, o combinație care produce PASS, dar nu există un plan executabil care să garanteze PASS în toate cele trei scenarii, respectând alegerile și informațiile disponibile la orele stabilite.

Am citit integral cele trei fișiere din `/case`. Dosarul nu conține subdirectoare sau PDF-uri. Analiza folosește exclusiv documentele din dosar; nu am modificat fișierele.

## 1. Criteriul contractual

Contractul cere un singur plan care funcționează în fiecare scenariu, fără compensarea eșecului într-un scenariu prin succesul în altul (`01_contract.md`, [C1]).

Planul trebuie să respecte următoarea ordine:

| Ora | Informații și alegeri disponibile | Consecință |
|---|---|---|
| 08:00 | Se contractează exact un transportator, irevocabil. | Transportatorul trebuie ales înainte de alertă. |
| 10:00 | Se primește numai alerta A1 sau A2. | A1 nu permite distingerea S1 de S2. |
| 11:00 | Se alege P sau A, în funcție de transportator și alertă. | Pentru același transportator și aceeași alertă trebuie stabilită aceeași alegere. |
| 12:00 | Devine cunoscut scenariul efectiv. | Informația sosește după alegerea ambalajului. |

**Probe:** `01_contract.md`, [C2]–[C3]; `02_scenarii.md`, [S1]–[S2].

Prin urmare, trebuie ales la 08:00 un transportator și stabilită o regulă executabilă pentru ambalaj: o alegere pentru A1 și una pentru A2.

## 2. Problemele materiale ale recomandării

### 2.1. Exemplele din notă nu alcătuiesc un plan contractual

Nota folosește Aurora/P pentru S1 și S3, dar Boreal/A pentru S2 (`03_nota.md`, [N1]). Aceste combinații sunt într-adevăr PASS în registru (`02_scenarii.md`, [S1]).

Totuși, transportatorul trebuie contractat irevocabil la 08:00; nu pot fi rezervate ambele firme și nu se poate schimba firma ulterior (`01_contract.md`, [C2]).

**Deducție:** cele trei exemple demonstrează posibilități separate, nu o livrare realizabilă printr-un singur contract.

### 2.2. Alegerea exclusivă a Aurorei nu rezolvă problema: S1 și S2 sunt indistincte la momentul deciziei

Pentru Aurora:

- S1 cere P: P este PASS, A este FAIL.
- S2 cere A: P este FAIL, A este PASS.
- Ambele scenarii transmit alerta A1.

**Probe:** `02_scenarii.md`, [S1]. Identificatorul scenariului și evenimentul nu sunt comunicate înainte de 12:00 (`02_scenarii.md`, [S2]); ambalajul se alege la 11:00 (`01_contract.md`, [C3]).

**Deducție:** după A1, Aurora nu poate selecta un ambalaj care să garanteze conformitatea. P pierde S2, iar A pierde S1. O instrucțiune precum „P în S1, A în S2” ar necesita informație indisponibilă la 11:00.

Aceasta este o problemă distinctă de alternarea transportatorilor din notă: chiar folosind numai Aurora, toate scenariile nu pot fi acoperite cu informațiile permise.

### 2.3. Alegerea Boreal rezolvă ambiguitatea A1, dar face S3 imposibil

La Boreal, ambalajul A produce PASS atât în S1, cât și în S2. În S3, ambele ambalaje produc FAIL (`02_scenarii.md`, [S1]).

**Deducție:** Boreal permite o decizie sigură după A1, însă nicio decizie după A2 nu salvează S3. Cum S3 se poate produce și trebuie acoperit, Boreal nu poate susține lansarea (`01_contract.md`, [C1]).

### 2.4. „Acoperire de 100%” confundă existența unor soluții separate cu existența unui plan comun

Afirmația „fiecare scenariu are o combinație PASS” este corectă. Concluzia „poate fi lansat cu un plan conform contractului” nu rezultă din ea (`03_nota.md`, [N1]).

**Deducție:** nota demonstrează că pentru fiecare scenariu există o combinație potrivită, dar contractul cere să existe un plan executabil potrivit pentru toate scenariile (`01_contract.md`, [C1]–[C3]). Demonstrația de mai jos arată că un asemenea plan nu există.

În plus, „100%” nu poate fi interpretat drept probabilitate de succes: dosarul nu oferă probabilități (`01_contract.md`, [C1]).

## 3. Demonstrație completă: ce se poate obține

Pentru fiecare transportator există patru reguli posibile de ambalare: câte o alegere P/A pentru fiecare dintre cele două alerte. Tabelul enumeră toate cele **opt planuri** permise de această structură.

| Ambalaj după A1 | Ambalaj după A2 | Scenarii cu PASS — Aurora | Scenarii cu PASS — Boreal |
|---|---|---|---|
| P | P | S1, S3 | Niciunul |
| P | A | S1 | Niciunul |
| A | P | S2, S3 | S1, S2 |
| A | A | S2 | S1, S2 |

**Probe și calcul:** regulile de decizie provin din `01_contract.md`, [C2]–[C3]; rezultatele sunt obținute direct din `02_scenarii.md`, [S1]–[S2].

Niciun plan nu obține PASS în toate cele trei scenarii. Maximumul este **două scenarii din trei**, realizabil astfel:

- Aurora, P după A1 și P după A2: PASS în S1 și S3;
- Aurora, A după A1 și P după A2: PASS în S2 și S3;
- Boreal, A după A1 și oricare ambalaj după A2: PASS în S1 și S2.

Acesta este un număr de scenarii acoperite, **nu o probabilitate de succes de 2/3**. Niciunul dintre aceste planuri nu satisface [C1].

Aceeași imposibilitate se vede din ambalajele care garantează PASS pentru toate scenariile compatibile cu alerta:

| Transportator | A1: trebuie acoperite S1 și S2 | A2: trebuie acoperit S3 |
|---|---|---|
| Aurora | Niciun ambalaj comun | P |
| Boreal | A | Niciun ambalaj |

## 4. Aspecte corecte și limitele informației

Sunt corecte verificările individuale din [N1]: Aurora/P trece S1 și S3, iar Boreal/A trece S2. Registrul este declarat complet și validat, astfel că rezultatele sale pot fi folosite fără ipoteze tehnice suplimentare (`01_contract.md`, [C4]).

Scenariul efectiv rămâne necunoscut până la 12:00, iar probabilitățile nu sunt precizate. Aceste necunoscute împiedică estimarea unei probabilități de succes, dar **nu împiedică demonstrarea imposibilității garanției contractuale**.

Nu există în dosar alte semnale, teste, rezerve sau opțiuni (`01_contract.md`, [C3]). Nota nu modifică bugetul ori calendarul și nu poate schimba contractul (`03_nota.md`, [N2]); asemenea soluții nu pot fi presupuse în evaluare.

## Concluzie

**Recomandarea de lansare trebuie respinsă în condițiile actuale.** Aurora este singurul transportator capabil să treacă S3, dar nu poate distinge la timp între S1 și S2, care cer ambalaje opuse. Boreal poate acoperi simultan S1 și S2, dar eșuează inevitabil în S3.

Dosarul demonstrează posibilitatea unor livrări conforme în scenarii individuale și acoperirea a cel mult două scenarii printr-un plan executabil. Nu demonstrează — și, prin tabelul complet, exclude — planul cerut pentru autorizarea lansării.