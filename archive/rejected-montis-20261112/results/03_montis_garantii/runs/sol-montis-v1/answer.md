**Pachetul nu poate fi aprobat în forma actuală. Expunerea minimă neacoperită este de 20 milioane EUR.** Oferta suplimentară pentru S nu reduce deficitul; oferta pentru N îl elimină și permite acoperirea integrală, dacă garanția este adăugată în condițiile descrise.

Toate sumele de mai jos sunt în milioane EUR. Analiza folosește exclusiv cele trei fișiere `.md` din director.

**Problemele materiale ale notei**

1. **Egalitatea totalurilor este corectă, dar nu demonstrează acoperirea.**

   Creditele însumează 200, iar garanțiile disponibile însumează tot 200, așa cum afirmă nota. Totuși, GC poate acoperi exclusiv S, al cărui principal este numai 80. Din GC = 100, cel puțin 20 nu pot fi utilizați în acest pachet.

   **Probe:** `03_nota.md` [N1]; `02_registru.md` [C1], [G1]; `01_politica.md` [P2].

   **Deducție:** excedentul pentru S nu poate fi transferat către N, E sau V. Totalul nominal al garanțiilor nu măsoară capacitatea de acoperire simultană.

2. **Controalele individuale sunt aritmetic corecte, dar reutilizează aceleași capacități în verificări separate.**

   N are acces la 50, E la 100, V la 50 și S la 100. Aceste valori sunt corecte individual. Însă GA apare atât în controlul N, cât și în controlul E, iar GB apare atât în controlul E, cât și în controlul V. Alocările efective din fiecare garanție trebuie să respecte împreună plafonul acesteia.

   **Probe:** `03_nota.md` [N1]; `02_registru.md` [G1]; `01_politica.md` [P1]–[P2].

   **Deducție:** faptul că fiecare credit ar putea fi acoperit separat nu înseamnă că toate pot fi acoperite simultan. Grupul N–E–V solicită 120 și are acces numai la GA + GB = 100. Acesta este deficitul pe care verificările individuale îl omit.

3. **Concluzia de aprobare contrazice condiția contractuală.**

   Contractul cere acoperirea simultană a fiecărui euro din fiecare credit. Deficitul de 20 la N–E–V încalcă această condiție.

   **Probe:** `01_politica.md` [P1]; `02_registru.md` [C1], [G1]; concluzia contrară din `03_nota.md` [N1].

   **Deducție:** recomandarea de aprobare în forma actuală trebuie respinsă, chiar dacă totalurile și toate controalele individuale sunt „verzi”.

4. **Oferta pentru S nu creează marjă utilizabilă pentru întregul pachet.**

   Garanția nouă de 20 ar crește capacitatea eligibilă exclusiv pentru S de la 100 la 120, față de un principal de 80. Capacitatea pentru N–E–V ar rămâne 100, față de necesarul de 120.

   **Probe:** `03_nota.md` [N2]; `02_registru.md` [C1], [G1]; `01_politica.md` [P2].

   **Deducție:** totalul nominal crește cu 20, dar acoperirea maximă a pachetului nu crește deloc. Afirmația despre „marjă suplimentară pentru întregul pachet” confundă valoarea adăugată cu o capacitate utilizabilă acolo unde există deficitul.

5. **Cele două oferte nu sunt echivalente pentru capacitatea de acoperire.**

   Oferta pentru N adaugă 20 exact în grupul deficitar N–E–V. Ea permite ca o parte din GA să fie realocată de la N către E, eliberând capacitate în GB pentru V.

   **Probe:** `03_nota.md` [N3]; `02_registru.md` [G1]; `01_politica.md` [P1]–[P2].

   **Deducție:** aceeași valoare, același cost și valabilitatea declarată nu compensează diferența de eligibilitate. Oferta pentru N permite acoperirea integrală; cea pentru S nu.

**Demonstrarea expunerii minime neacoperite**

Limita inferioară a deficitului este:

\[
(N+E+V)-(GA+GB)=(40+40+40)-(50+50)=20.
\]

Aceasta rezultă direct din `02_registru.md` [C1], [G1] și din eligibilitatea exhaustivă prevăzută în `01_politica.md` [P2].

Următoarea alocare respectă toate plafoanele și arată că deficitul poate fi limitat la exact 20:

| Garanție | N | E | V | S | Total alocat |
|---|---:|---:|---:|---:|---:|
| GA | 40 | 10 | 0 | 0 | 50 |
| GB | 0 | 10 | 40 | 0 | 50 |
| GC | 0 | 0 | 0 | 80 | 80 |
| **Acoperire** | **40** | **20** | **40** | **80** | **180** |
| **Neacoperit** | **0** | **20** | **0** | **0** | **20** |

Prin urmare, **acoperirea maximă este 180, iar expunerea minimă neacoperită este exact 20**: limita este atât necesară, cât și realizabilă.

Deficitul nu trebuie atribuit obligatoriu creditului E. Tabelul este o alocare posibilă; dosarul permite alte alocări și împărțirea deficitului între N, E și V. Nu există alocări anterioare care să impună o anumită distribuție. **Probe:** `01_politica.md` [P1]–[P2].

**Efectul fiecărei oferte**

| Indicator | Forma actuală | Cu oferta pentru S | Cu oferta pentru N |
|---|---:|---:|---:|
| Total nominal garanții | 200 | 220 | 220 |
| Capacitate eligibilă pentru N–E–V | 100 | 100 | 120 |
| Capacitate eligibilă pentru S | 100 | 120 | 100 |
| Acoperire maximă a pachetului | 180 | 180 | 200 |
| **Expunere minimă neacoperită** | **20** | **20** | **0** |
| Îndeplinește condiția de aprobare | Nu | Nu | Da, dacă oferta este incorporată |

Pentru oferta destinată S, alocarea anterioară rămâne fezabilă, iar deficitul N–E–V rămâne inevitabil. Din capacitatea totală de 120 destinată S se pot utiliza cel mult 80; rămân 40 neutilizabili în acest pachet.

Pentru oferta destinată N, următoarea alocare dovedește acoperirea integrală:

| Garanție | N | E | V | S | Total alocat |
|---|---:|---:|---:|---:|---:|
| GA | 20 | 30 | 0 | 0 | 50 |
| GB | 0 | 10 | 40 | 0 | 50 |
| GC | 0 | 0 | 0 | 80 | 80 |
| Garanția nouă pentru N | 20 | 0 | 0 | 0 | 20 |
| **Acoperire** | **40** | **40** | **40** | **80** | **200** |

Alocarea respectă destinațiile și plafoanele din `02_registru.md` [C1], [G1], completate cu oferta descrisă în `03_nota.md` [N3], conform regulilor din `01_politica.md` [P2]. Cei 20 suplimentari pentru N sunt necesari integral; cei 20 rămași în GC continuă să fie utilizabili exclusiv pentru S.

**Aspecte corecte și limitele constatărilor**

Sunt corecte totalurile și valorile individual eligibile din [N1]. Garanțiile existente sunt declarate valabile, independente, iar registrul este complet; valorile sunt deja nete de ajustările de risc. Nu există bază în dosar pentru alte reduceri de valoare sau condiții suplimentare de aprobare. **Probe:** `02_registru.md` [G2]; `01_politica.md` [P1]–[P3].

Registrul curent cuprinde numai GA, GB și GC. Garanțiile suplimentare sunt prezentate ca posibilitate și ofertă în [N2]–[N3], fără ca dosarul să consemneze incorporarea lor. Efectele calculate pentru acestea sunt, așadar, condiționate de adăugarea garanției în termenii descriși. Nu este necesară presupunerea unor cerințe juridice externe.

**Decizia rezultată din dosar:** forma actuală nu poate fi aprobată, deoarece lasă inevitabil 20 milioane EUR neacoperite. Oferta pentru S păstrează acest deficit. Oferta pentru N îl elimină și, odată incorporată cu eligibilitatea și valabilitatea descrise, permite aprobarea conform singurei condiții contractuale din dosar.