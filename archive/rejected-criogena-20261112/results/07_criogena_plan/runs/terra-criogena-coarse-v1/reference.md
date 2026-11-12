# Etalon: Criogena — plan executabil înaintea aflării scenariului

Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.

Întrebare: Refă reviewul recomandării Criogena pentru CR-7. Poate fi lansată livrarea conform contractului? Demonstrează ce se poate obține cu alegerile și informațiile disponibile la orele stabilite.

Profil: scurt, decizii în condiții de incertitudine. Mecanism principal: Fezabilitatea separată a scenariilor este confundată cu existența unei politici care respectă momentul disponibilității informației.

## F1: Nu există un plan executabil care să acopere toate cele trei scenarii; lansarea nu este permisă.

Probe: 01_contract.md#C1, 01_contract.md#C2, 01_contract.md#C3, 02_scenarii.md#S1, 02_scenarii.md#S2.

Deducție: Dacă se fixează Boreal, S3 este FAIL pentru ambele ambalaje. Dacă se fixează Aurora, S1 și S2 au aceeași alertă A1, dar S1 cere P iar S2 cere A. La 11:00 nu pot fi deosebite, deci o singură decizie pentru A1 pierde cel puțin unul. Cele două alegeri posibile de transportator sunt exhaustive.

## F2: Cea mai bună politică acoperă două din cele trei scenarii; verificările separate din notă nu demonstrează acoperire de 100%.

Probe: 01_contract.md#C2, 01_contract.md#C3, 02_scenarii.md#S1, 03_nota.md#N1.

Deducție: Limita superioară este două scenarii prin F1. Se atinge cu Aurora și P după ambele alerte: trece S1/S3 și eșuează S2. Nu afirmăm o probabilitate de succes de 2/3, deoarece dosarul nu dă probabilități. Nota schimbă retrospectiv transportatorul, folosind informație care nu există la ora contractării.

## Aspecte corecte

- Fiecare scenariu are cel puțin o combinație fizică PASS.
- Bugetul și calendarul sunt fixe.
- Nu se poate transforma numărul de scenarii acoperite într-o probabilitate fără date suplimentare.

## Evaluare

Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.
