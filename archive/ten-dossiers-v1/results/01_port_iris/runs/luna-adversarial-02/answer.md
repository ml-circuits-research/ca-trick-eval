## Concluzie la 12.06.2026, ora 12:00 UTC

| Cheie de obligație (O) | Statut | Angajament fără TVA |
|---|---|---:|
| IR-071 | Activă | 48.000 EUR |
| IR-017 | Activă | 8.000 EUR |
| **Total** | **Ambele active** | **56.000 EUR** |

Acesta este totalul angajamentelor evidențiate în dosar; nu include prestații, plăți, penalități sau comenzi suplimentare, conform [01_contracte.md, C1].

## Probe și deducții

- **IR-071 — activă, 48.000 EUR.** [01_contracte.md, C1] stabilește valoarea și momentul inițial al activării. [01_contracte.md, C2] precizează că pentru obligații (O) contează numai evenimentele cu două semnături, acestea se aplică în ordinea `effective_at`, iar o activare (A) după încetare (X) reface integral obligația. În [02_registru.md, E1], e11 este X cu două semnături la 09:00, iar e12 este A cu două semnături la 11:00 pe 11 iunie. Așadar, e12 urmează după e11 și repune integral IR-071 în vigoare: **48.000 EUR**. Faptul că e11 a fost importată mai târziu decât e12 nu schimbă ordinea aplicării, conform C2.

- **IR-017 — activă, 8.000 EUR.** [01_contracte.md, C1] stabilește suma și activarea inițială. În [02_registru.md, E1], e13 este o încetare (X) cu **o singură semnătură**. Potrivit [01_contracte.md, C2], un eveniment O produce efect numai cu două semnături, deci e13 nu încetează obligația. În plus, [01_contracte.md, C3] confirmă că în registru nu există alte evenimente pentru aceste chei O.

- **e14 nu afectează totalul.** În [02_registru.md, E1], e14 privește cheia B, nu O. [01_contracte.md, C2] precizează că B desemnează un badge și nu are efect financiar. Cheia este perechea tip + număr; astfel, badge-ul IR-071 nu este obligația O cu același număr.

Calculul este **48.000 + 8.000 = 56.000 EUR**. C1 precizează valorile din acord, însă dosarul nu conține o etichetă explicită „fără TVA”; interpretarea sumelor drept angajamentele fără TVA cerute se bazează pe valorile contractuale menționate în C1 și pe excluderile enumerate acolo.

## Verificarea sintezei de control

Sinteza **nu este corectă** pentru niciuna dintre cele două obligații și subestimează totalul cu **48.000 EUR**:

- În [03_control.md, S1], IR-071 este declarată anulată deoarece e11 ar fi „ultima înregistrare importată”. Este o concluzie greșită: [01_contracte.md, C2] cere ordonarea după `effective_at`, iar e12, activarea eligibilă de la 11:00, urmează după e11 de la 09:00. S1 mai confundă tipul: [02_registru.md, E2] spune că e12 are sensul O stabilit în acord, deși procesul-verbal a fost clasat la rubrica ecusoane.

- În [03_control.md, S1], afirmația că IR-017 nu are anulare valabilă ajunge la un rezultat compatibil cu registrul, dar dosarul nu confirmă raționamentul din sinteză: e13 este o încetare cu o singură semnătură și, potrivit C2, nu are efect. S1 nu explică acest criteriu.

- În [03_control.md, S1–S2], valoarea de **8.000 EUR** este incompletă. [03_control.md, S2] spune că extrasul a fost copiat din S1 fără reconciliere suplimentară; prin urmare, nu este o verificare independentă și perpetuează omiterea angajamentului IR-071.

## Aspecte certe și necunoscute

Sunt certe, conform regulilor și înregistrărilor din dosar, sumele inițiale, statutul activ al ambelor obligații la momentul cerut și totalul de **56.000 EUR**. De asemenea, sinteza de control nu modifică registrul, conform [01_contracte.md, C3].

Dosarul nu precizează explicit tratamentul TVA sau dacă sumele din C1 sunt definite contractual ca valori nete ori brute; deci această etichetă nu poate fi verificată separat. Nici nu este prezentat un act distinct pentru e12 în afara informației de validare din [02_registru.md, E2]. Totuși, conform regulii din C3 și precizării E2 că cele două semnături sunt autentice și că nu există termen suspensiv, mențiunea din sinteză despre clasificarea sa la rubrica ecusoane nu îi schimbă efectul în registru.