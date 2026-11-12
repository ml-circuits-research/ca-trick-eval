## Concluzie la 12.06.2026, 12:00 UTC

**Comanda activă este IR-017, în valoare de 8.000 EUR fără TVA. Totalul angajamentelor active este 8.000 EUR fără TVA.** Raportul publicat și rezumatul de comunicare indică 56.000 EUR și ambele comenzi active; aceste afirmații nu corespund actelor comerciale relevante din dosar.

## Probe și deducții

- **Valori și chei:** `01_contracte.md`, pasajele **[C1]** și **[C4]**: IR-071 este de 48.000 EUR și se leagă de DG-710 → MAP-142; IR-017 este de 8.000 EUR și se leagă de DG-170 → MAP-124. Ambele au fost emise active la 03.06.  
  **Deducție:** pentru a afla starea fiecărei comenzi trebuie urmărite aceste chei prin indexuri.

- **Rezolvarea referințelor:** `02_jurnal.md`, pasajele **[J1]** și **[J2]**: MAP-142 → PK-908 → REF-61; MAP-124 → PK-890 → REF-16.  
  **Deducție:** actele de pe REF-61 se aplică IR-071, iar cele de pe REF-16 se aplică IR-017. Codurile se compară integral, conform [J1].

- **Regula de stare:** `01_contracte.md`, pasajele **[C2]–[C3]**: contează ultimul eveniment comercial cu efect până la ora raportului; un eveniment comercial trebuie să fie din familia COM și să aibă două semnături; codul 20 înseamnă anulare integrală, iar familia ACC nu are efect comercial. Registrele sunt declarate complete, iar actele autentice; raportul nu modifică actele.

- **Actele relevante:** `03_raport_si_acte.md`, pasajul **[A1]**:
  - REF-61 are un eveniment **COM, cod 20**, cu efect la 11.06, 09:00 UTC și două semnături.
  - REF-61 are apoi un eveniment **ACC, cod 10**, cu efect la 12.06, 11:00 UTC; acesta nu schimbă starea comercială.
  - REF-16 are un eveniment **ACC, cod 20**, cu efect la 12.06, 11:30 UTC; nici acesta nu schimbă starea comercială.
  - REF-19 are un eveniment **COM, cod 20**, dar referința nu este asociată comenzilor IR-071 sau IR-017 în indexurile din dosar.

  **Deducție:** IR-071 este anulată integral înainte de ora de referință și nu există o reactivare comercială ulterioară pe REF-61. IR-017 rămâne activă: [J3] precizează că REF-16 nu are evenimente comerciale ulterioare emiterii inițiale, iar evenimentul ACC din [A1] nu produce efect comercial.

- **Raportul publicat:** `03_raport_si_acte.md`, pasajul **[S1]**: raportul din 11:59 UTC declară active ambele comenzi și totalul de 56.000 EUR fără TVA.  
  **Deducție:** IR-071 nu era activă la acel moment, deci totalul este supraevaluat cu 48.000 EUR. Valoarea corectă era 8.000 EUR fără TVA.

- **Rezumatul de comunicare:** `03_raport_si_acte.md`, pasajul **[S2]**: la 12:00 UTC este comunicat din nou totalul de 56.000 EUR, preluat din celula de total a raportului [S1].  
  **Deducție:** rezumatul repetă eroarea raportului; ora ulterioară a comunicării nu schimbă efectul actelor.

## Probleme materiale și surse de confuzie

1. **Raportul folosește starea greșită pentru IR-071.** [S1] o prezintă activă, deși [A1] consemnează anularea comercială integrală pe REF-61, identificată prin [C4], [J1] și [J2].
2. **Totalul este greșit:** raportul însumează 48.000 + 8.000 = 56.000 EUR, dar trebuie inclusă doar IR-017: **8.000 EUR fără TVA**.
3. **Evenimentele ACC pot induce în eroare.** [A1] conține evenimente ACC cu coduri 10 și 20, dar [C2] le exclude explicit din starea comercială. Ele nu reactivează IR-071 și nu anulează IR-017.
4. **Referința REF-19 nu aparține comenzilor analizate.** Actul comercial de anulare de pe REF-19 nu poate fi atribuit unei comenzi Iris doar pe baza prezenței sale în borderou; traseul cheilor din [C4], [J1] și [J2] duce la REF-61 și REF-16.
5. **Observațiile administrative nu sunt acte comerciale.** [C3] precizează că rândurile OBS nu au acest efect. Datele neobișnuite din unele rânduri OBS nu schimbă calculul, iar dosarul nu oferă temei să le tratăm ca anulări sau activări.
6. **[S2] propagă, nu verifică, cifra din raport.** Faptul că rezumatul preia totalul din [S1] explică repetarea valorii, dar nu o confirmă independent.

## Fapte certe și necunoscute

**Fapte certe potrivit dosarului:** regulile de interpretare sunt stabilite în [C2]–[C3], registrele sunt declarate complete, iar actele autentice. Pe baza traseelor și actelor, la ora cerută IR-071 este anulată, IR-017 este activă, iar angajamentul activ este de **8.000 EUR fără TVA**. [C1] mai precizează că nu există costuri de anulare, prestații, plăți sau alte comenzi de inclus.

**Necunoscut din dosar:** nu este furnizată o altă verificare independentă a registrelor ori o metodă de validare în afara declarațiilor din [C2]–[C3]. Concluzia de mai sus se bazează, așadar, pe autenticitatea și caracterul complet afirmate în dosar.

## Rezumat final

La **12.06.2026, 12:00 UTC**, singura comandă Iris activă din dosar este **IR-017 — 8.000 EUR fără TVA**. **Raportul publicat este incorect:** marchează IR-071 activă și raportează un angajament de 56.000 EUR, deși actul comercial de anulare cu efect la 11.06 o anulase deja. Rezumatul de la 12:00 repetă cifra eronată.