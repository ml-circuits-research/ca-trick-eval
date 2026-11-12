# Furnizor, registru financiar și finanțare

[C1] Factura și recepția sunt pentru Aster Manufacturing SRL, RO4100, producție la Cluj. Certificatul depus Q-8 este pentru Aster Services SRL, RO410O, mentenanță la Iași. Firmele sunt afiliate, dar distincte. Q-8 este singurul certificat depus. Plata cere certificarea exactă din M2, recepție și aprobare financiară. Recepția și aprobarea financiară există.
[C2] Registru complet, EUR fără TVA. În cheia CREDIT din rândul r4 există un caracter invizibil U+200B după cratimă; în rândul r3 cratima este U+2011. Aceste reprezentări sunt explicit supuse normalizării M5.
| rând | cheie factură | revizie | tip | valoare | statut |
|---|---|---|---|---|---|
| r1 | AP-104 | 1 | FACT | 100000.00 | POST |
| r2 | AP-104 | 1 | FACT | 100000.00 | COPY |
| r3 | AP‑104 | 2 | FACT | 96000.00 | POST |
| r4 | AP-​104 | 1 | CREDIT | 8000.00 | POST |
[C3] Disponibilul eligibil pentru împrumut se compară cu soldul net M5, nu cu valoarea versiunii inițiale sau doar cu subtotalul FACT. Nu există alte condiții financiare decât M6. Certificarea furnizorului rămâne o condiție separată a plății facturii, nu o condiție suplimentară nescrisă a împrumutului.
