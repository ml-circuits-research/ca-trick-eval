## Concluzie executivă

**La 09.10.2026, ora 12:00 UTC, H-11 are 900 kg utilizabile și nu este expediabil. Recipientul 7 rămâne în carantină și nesigilat.** Aceasta este concluzia executivă din receipt-ul local. Poarta de validare a trecut: am verificat amprentele celor două exporturi și rezultatul a fost `PASS`.

## Verificarea notei de oprire și a evidențelor

- **Masa utilizabilă: 900 kg.** `01_evidente.md` **[I1]** indică masa brută de 1.200 t și ambalajul de 200 kg; rezultă 1.000 kg net. **[I2]** atribuie recipientului 7 o masă netă de 100 kg și `Q=1`, iar restului `Q=0`. Conform `02_registru.md` **[R1]**, numai masa netă cu `Q=0` este utilizabilă: 1.000 − 100 = **900 kg**.

- **Lotul nu poate fi expediat.** `02_registru.md` **[R1]** cere minimum 950 kg utilizabile și `Q=0` pentru toate recipientele, cu sigilii intacte; derogarea este necesară când oricare condiție eșuează. Cele 900 kg sunt sub prag, iar la ora cerută recipientul 7 are încă `Q=1`. `02_registru.md` **[E2]** confirmă că nu există derogare scrisă. Deci expedierea nu este permisă, indiferent de disputa privind sigiliul.

- **Starea la ora cerută:** `02_registru.md` **[R2]** precizează că se aplică ultimul eveniment semnat cu timp de efect cel mult egal cu ora cerută, pe fiecare câmp separat. În **[E1]**, `SEAL-R` pentru H-11 recipientul 7 are efect la 11:30 UTC, deci precedă ora 12:00; `HOLD-R` la 14:45 UTC+03:00 este 11:45 UTC și tot precedă ora cerută? **Nu**: conversia corectă este 11:45 UTC, deci precedă 12:00 UTC. Prin urmare, la 12:00, atât `SEAL-R` de la 11:30, cât și `HOLD-R` de la 11:45 sunt deja efective. Conform **[R2]**, `HOLD-R` setează `Q=0`, iar `SEAL-R` setează sigiliul intact. Asta contrazice atât nota de oprire, cât și receipt-ul privind carantina și sigiliul.

- **Atenție la timestamp:** `14:45 UTC+03:00` înseamnă **11:45 UTC**. Dacă s-ar citi greșit ca 14:45 UTC, s-ar păstra `Q=1` la ora cerută și s-ar obține concluzia din receipt; conversia fusului orar schimbă această stare.

- **Atenție la identificator:** `02_registru.md` **[E1]** conține evenimente pentru `H-l1` (litera „l”) și pentru `H-11` (cifra „1”). Evenimentul `HOLD-A` de la 11:59 UTC aparține lui `H-l1`, nu lui H-11, și nu trebuie aplicat lotului cerut.

- **Nota de oprire este un instantaneu anterior și are probleme de concordanță.** `01_evidente.md` **[I3]** spune că nota de la 12:01 UTC a fost compilată din lista de la 08:00. Lista nu include evenimentele ulterioare din `02_registru.md` **[E1]**. Fotografia de la 08:15 din **[E2]** arată recipientul roșu, dar este tot o observație timpurie. În plus, nota susține că recipientul 7 este „nesigilat”, deși **[E1]** consemnează `SEAL-R` la 11:30.

- **Aspecte care rămân certe:** calculul de 900 kg rezultă din masele și starea inițială din **[I1–I2]**, iar pragul de 950 kg și lipsa derogării sunt consemnate în **[R1]** și **[E2]**. Acestea sunt suficiente pentru a stabili că lotul nu este expediabil la ora cerută, chiar dacă există conflict privind starea recipientului 7.

## Rezumat final

Receipt-ul validat afirmă că H-11 are 900 kg utilizabile și nu poate fi expediat, cu recipientul 7 în carantină și nesigilat. Totuși, aplicând literal regulile de timp și codurile din exportul intern, `HOLD-R` de la 11:45 UTC ar trebui să elibereze recipientul de carantină, iar `SEAL-R` de la 11:30 UTC ar trebui să-l sigileze înainte de ora cerută. **Concluzia privind neexpediabilitatea rămâne sigură**, deoarece 900 kg sunt sub pragul de 950 kg și nu există derogare. **Starea recipientului 7 din receipt și nota de oprire nu este reconciliată cu evenimentele din registru.**