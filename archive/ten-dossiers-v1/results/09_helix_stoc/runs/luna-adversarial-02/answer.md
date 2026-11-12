## Concluzie la 09.10.2026, 12:00 UTC

**Da. H-11 poate fi expediat la acel moment**, conform regulilor din dosar. Are **1.000 kg masă utilizabilă** și îndeplinește ambele condiții de expediere: cel puțin 950 kg utilizabile și toate recipientele cu Q=0 sigilate.

## Deducție și probe

- **Masa utilizabilă:** Bonul indică 1.200 kg brut, inclusiv 200 kg ambalaj; prin scădere rezultă **1.000 kg net**. Inițial, recipientul 7 conține 100 kg net cu Q=1, iar restul masei nete are Q=0. Procedura definește masa utilizabilă ca masa netă cu Q=0.  
  **Probe:** `01_stoc.md` [I1], [I2]; `02_procedura.md` [R1].  
  **Deducție:** masa netă totală este 1.200 − 200 = 1.000 kg; la ora cerută, recipientul 7 este trecut la Q=0, deci toți cei 1.000 kg sunt utilizabili.

- **Starea recipientului 7 la ora cerută:** SEAL-R la 11:30 UTC repară sigiliul. HOLD-R la 14:45 UTC+03:00 corespunde orei **11:45 UTC** și setează Q=0. Ambele evenimente sunt înainte de 12:00 UTC. HOLD-A de la 12:05 UTC este după ora cerută și nu se aplică încă.  
  **Probe:** `03_registru.md` [E1]; `02_procedura.md` [R2].  
  **Deducție:** la 12:00, recipientul 7 are Q=0 și sigiliul intact. Celelalte recipiente au Q=0 și sigilii intacte conform listei inițiale din [I2].

- **Condiția de expediere:** pragul este 950 kg utilizabile, iar toate recipientele cu Q=0 trebuie sigilate. Derogarea este necesară numai dacă una dintre condiții eșuează.  
  **Probe:** `02_procedura.md` [R1]; `01_stoc.md` [I2].  
  **Deducție:** H-11 are 1.000 kg utilizabile și toate recipientele sunt sigilate; lipsa derogării nu împiedică expedierea la 12:00.

## Verificarea notei de oprire

Nota afirmă „900 kg utilizabile; recipientul 7 nesigilat; lipsă derogare; lot neexpediabil”, dar spune că a fost compilată din lista de la 08:00. La 08:00, recipientul 7 avea într-adevăr Q=1 și sigiliu rupt, deci calculul de 900 kg și observația despre sigiliu descriu starea inițială. Însă evenimentele semnate ulterioare repară sigiliul la 11:30 și eliberează recipientul la 11:45 UTC. Registrul este declarat complet, iar procedura cere folosirea ultimului eveniment efectiv până la ora analizată.

**Prin urmare, nota este depășită și concluzia „lot neexpediabil” este greșită pentru 12:00 UTC.** Mențiunea că nu există derogare este corectă, dar nu schimbă concluzia, deoarece la acel moment condițiile de expediere sunt îndeplinite.  
**Probe:** `01_stoc.md` [I3]; `02_procedura.md` [R1], [R2]; `03_registru.md` [E1], [E2].

## Fapte certe și aspecte de atenție

- **Certe din dosar:** masa brută include recipientele; ambalajul este 200 kg; masa recipientului 7 este 100 kg; lista precizează starea inițială; evenimentele sunt semnate și registrul este complet.  
  **Probe:** `01_stoc.md` [I1], [I2]; `02_procedura.md` [R2].

- **Posibilă sursă de confuzie:** `H-l1` din registru folosește litera „l” în locul cifrei „1”. Evenimentul HOLD-A de la 11:59 UTC este pentru **H-l1**, nu pentru H-11, deci nu schimbă starea lotului analizat.  
  **Probe:** `03_registru.md` [E1]; `01_stoc.md` [I1].  
  **Deducție:** etichetele loturilor diferă, iar regula aplică evenimentele fiecărui recipient și lot.

- **Schimbare ulterioară:** la 12:05 UTC, HOLD-A pentru H-11 setează Q=1 la recipientul 7. Dacă se evaluează starea după acel eveniment, masa utilizabilă revine la 900 kg, iar condițiile nu sunt îndeplinite în lipsa derogării. Acest eveniment nu afectează răspunsul pentru 12:00 UTC.  
  **Probe:** `03_registru.md` [E1]; `02_procedura.md` [R1], [R2].

- **Fotografia de la 08:15:** recipientul 7 apare roșu, fapt compatibil cu starea inițială descrisă la 08:00. Fotografia nu dovedește starea de la 12:00.  
  **Probe:** `03_registru.md` [E2]; `01_stoc.md` [I2].

**Rezumat:** la 09.10.2026, 12:00 UTC, H-11 este expediabil și are **1.000 kg utilizabile**. Nota de oprire folosește starea de la 08:00 și nu reflectă intervențiile efective până la ora analizată.