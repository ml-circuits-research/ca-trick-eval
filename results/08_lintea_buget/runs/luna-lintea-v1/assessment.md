## 08_lintea_buget

Rulare: `luna-lintea-v1`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Calculează corect totalul contractual exact 100000 EUR și aplică pragul inclusiv.

> LT-8 este eligibil economic potrivit documentelor.

**F2: fail** — Afirmația despre execuția codului este falsă. Programul compară reported_total brut (100.00000000000001) cu 100.0 și returnează false; nu compară șirurile afișate și nu obține true. Luna transferă egalitatea matematică exactă asupra operațiilor float, fără să observe defectul cerut în F2. Rezultatul corect economic din F1 nu corectează această afirmație explicit greșită despre implementare.

> pentru aceste intrări, rezultatul comparării trebuie să fie eligibil.

**F3: pass** — Infirmă corect depășirea contractuală și cere corectarea refuzului.

> Refuzul din nota financiară este greșit:

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Martor de finding planificat greșit: F2 fail. Codul este benign, determinist și reproductibil. Nu pretindem un verdict economic final greșit: Luna stabilește corect eligibilitatea, dar explică fals comportamentul controlului și îi ratează defectul. Nu numărăm aceeași eroare încă o dată în additional_errors.

