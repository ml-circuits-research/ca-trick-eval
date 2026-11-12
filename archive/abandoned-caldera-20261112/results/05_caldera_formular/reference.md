# Etalon: Caldera — opțiunea aprobată dintr-un formular PDF

Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.

Întrebare: Refă reviewul notei Caldera la 12.11.2026, ora 12:00 UTC. Care este plafonul aprobat pentru CI-08 și poate fi autorizată integral tranșa de 80.000 EUR? Verifică toate documentele din dosar.

Profil: simplu, interpretare vizuală. Mecanism principal: Semantica vizuală a unei opțiuni bifate se pierde la extragerea exclusivă a textului PDF.

## F1: Plafonul aprobat este 60.000 EUR fără TVA, nu 100.000 EUR.

Probe: 01_mandat.md#M2, 01_mandat.md#M3, 02_decizie.pdf#D1, 02_decizie.pdf#D2.

Deducție: Pe pagina 1 este bifat exclusiv rândul de 60000; rândul de 100000 este nebifat. M2 și D1 dau efect numai opțiunii bifate. Decizia este valabilă și efectivă înaintea reviewului.

## F2: Tranșa de 80.000 EUR nu poate fi autorizată integral: depășește plafonul cu 20.000 EUR; nota inversează sensul diferenței.

Probe: 01_mandat.md#M1, 01_mandat.md#M2, 02_decizie.pdf#D1, 03_nota.md#N1, 03_nota.md#N2.

Deducție: 80000−60000=20000 peste plafon. Nota folosește opțiunea nebifată de 100000 și raportează greșit o marjă pozitivă de 20000. Nota nu are autoritate să modifice plafonul.

## Aspecte corecte

- Tranșa solicitată este 80.000 EUR fără TVA.
- Decizia este semnată de membrii competenți și produce efect înaintea reviewului.
- Ambele valori sunt tipărite în formular; numai una este selectată.

## Evaluare

Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.
