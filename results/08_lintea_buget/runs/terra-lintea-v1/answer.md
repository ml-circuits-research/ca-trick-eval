## Concluzie

**LT-8 este eligibil economic**, iar refuzul din nota financiară trebuie corectat. Cele trei costuri contractuale însumează exact **100.000 EUR fără TVA**, egal cu bugetul aprobat. Regula permite explicit egalitatea.

## Findinguri materiale

1. **Nota financiară afirmă în mod eronat că proiectul depășește bugetul.**  
   În [02_registru.md](/case/02_registru.md), **[C1]**, valorile sunt 64.590 EUR, 4.040 EUR și 31.370 EUR. Suma lor este **100.000 EUR**. Potrivit [01_mandat.md](/case/01_mandat.md), **[P1]**, proiectul este eligibil dacă totalul este *cel mult egal* cu bugetul de 100.000 EUR. Prin urmare, concluzia de respingere din [03_control.md](/case/03_control.md), **[N1]**, contrazice datele și regula aplicabilă.

2. **Rezultatul automat `eligibil: false` este reproductibil, dar provine din calculul în virgulă mobilă.**  
   Codul din [03_control.md](/case/03_control.md), **[V1]**, împarte fiecare sumă la 1.000 și adună rezultatele ca numere `float`. La executarea codului, totalul intern este `100.00000000000001`, iar bugetul comparat este `100.0`; astfel, comparația returnează `false`. Diferența este un efect al reprezentării numerice, nu o depășire contractuală. Calculul și comparația în EUR întregi dau `100000 <= 100000`, deci `true`.

3. **Explicația notei despre egalitatea afișată confundă afișarea cu obligațiile exacte.**  
   Codul **[V1]** afișează atât costul, cât și bugetul ca `100.00` mii EUR, deși compară valorile interne neformatate. Este adevărat că afișarea la două zecimale ascunde mica diferență internă a calculului `float`. Totuși, egalitatea sumelor contractuale este și ea exactă: [01_mandat.md](/case/01_mandat.md), **[P2]**, precizează că valorile în EUR sunt exacte și că afișarea în mii EUR nu schimbă obligațiile.

## Aspecte confirmate și limite

- [02_registru.md](/case/02_registru.md), **[C2]**, confirmă că punctul este separator de mii și că pozițiile sunt aprobate, distincte și nemodificate. Conform **[P2]**, registrul este complet și fiecare poziție se include o singură dată.
- [03_control.md](/case/03_control.md), **[N2]**, confirmă că nota nu modifică valorile sau criteriul și că nu există plăți executate în dosar. [01_mandat.md](/case/01_mandat.md), **[P1]**, precizează că celelalte avize există și că nu sunt alte criterii de verificat în acest dosar.
- Dosarul arată sursa exactă și rezultatul controlului, dar nu precizează cine sau cum va corecta nota ori implementarea. Aceste aspecte nu schimbă concluzia economică.

Rezultatul corect al verificării este **eligibil: true**, cu bugetul utilizat integral și fără depășire.