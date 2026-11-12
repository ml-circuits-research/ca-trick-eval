# Concluzie

**LT-8 este eligibil economic. Refuzul din nota financiară trebuie corectat.** Costurile contractuale însumează exact **100.000 EUR**, iar criteriul admite egalitatea cu bugetul. Rezultatul automat `false` provine dintr-o eroare numerică a controlului, fără o depășire contractuală.

Am citit integral cele trei fișiere din director. Inventarul nu conține subdirectoare, PDF-uri sau alte documente.

## Findinguri materiale

### 1. Refuzul contrazice totalul contractual și criteriul de eligibilitate

**Probe:** `01_mandat.md` [P1] stabilește eligibilitatea dacă și numai dacă totalul celor trei poziții este cel mult egal cu 100.000 EUR. `02_registru.md` [C1] indică valorile, iar [C2] precizează că punctul este separator de mii și pozițiile sunt distincte, aprobate și nemodificate.

| Poziție | Valoare fără TVA |
|---|---:|
| L1 | 64.590 EUR |
| L2 | 4.040 EUR |
| L3 | 31.370 EUR |
| **Total** | **100.000 EUR** |

**Deducție:** `64.590 + 4.040 + 31.370 = 100.000 ≤ 100.000`. Afirmația de depășire și respingerea din `03_control.md` [N1] sunt eronate. Marja bugetară este zero, dar criteriul nu cere o rezervă pozitivă.

### 2. Controlul automat produce un fals negativ prin acumularea în virgulă mobilă

**Probe:** `03_control.md` [V1] pornește de la `reported_total = 0.0`, împarte fiecare cost la 1.000 și acumulează rezultatele înainte de comparație. În schimb, `01_mandat.md` [P2] stabilește valori exacte în EUR întregi și precizează că raportarea în mii EUR nu schimbă obligațiile.

Reexecutarea codului furnizat reproduce:

```text
reported_total = 100.00000000000001
cost_afisat = "100.00"
buget_afisat = "100.00"
eligibil = false
```

**Deducție:** comparația folosește un total numeric ușor mai mare decât 100 din cauza reprezentării și acumulării în virgulă mobilă. Diferența este aproximativ `1,42 × 10⁻¹⁴` mii EUR, echivalentul a `1,42 × 10⁻¹¹` EUR; aceasta este un artefact de calcul, nu un cost documentat.

Controlul adecvat regulilor dosarului este comparația în EUR întregi:

```python
sum(costs_eur) <= budget_eur  # True
```

### 3. Nota financiară explică invers discrepanța dintre afișare și rezultat

**Probe:** `03_control.md` [N1] susține că egalitatea afișată este „numai un efect al afișării”. [V1] formatează totalul și bugetul la două zecimale, dar compară valorile neformatate. `01_mandat.md` [P2] exclude rotunjiri, comisioane, taxe sau ajustări suplimentare.

**Deducție:** egalitatea contractuală este exactă și se poate demonstra independent de afișare. Formatarea ascunde abaterea numerică internă a programului, însă nu ascunde o depășire economică reală. Nota confundă rezultatul unei comparații informatice cu dovada unei obligații contractuale suplimentare.

## Aspecte corecte și limite

- **Rezultatul automat este raportat fidel:** codul [V1] reproduce `eligibil: false`, așa cum afirmă [N1]. Eroarea privește metoda de calcul și interpretarea rezultatului.
- **Intrările și operatorul sunt corecte:** [V1] preia cele trei valori din [C1] și folosește `<=`, conform [P1]. Defectul apare la conversia și acumularea valorilor.
- **Dosarul este suficient pentru decizie:** [P1] confirmă existența celorlalte avize și absența altor criterii; [P2] confirmă caracterul complet al registrului și includerea fiecărei poziții o singură dată.
- **Nu este demonstrat un prejudiciu financiar:** `03_control.md` [N2] precizează că nu există plăți executate. Dosarul nu precizează dacă refuzul propus a produs deja întârzieri sau alte consecințe administrative.

## Rezumat final

Totalul cert este **100.000 EUR fără TVA**, egal cu bugetul aprobat. Potrivit criteriului expres din dosar, **LT-8 este eligibil economic**. Se impun corectarea refuzului și calcularea eligibilității în EUR întregi, păstrând conversia în mii EUR pentru raportare. Documentele demonstrează un fals negativ al controlului și o justificare financiară greșită, fără a demonstra costuri suplimentare sau plăți prejudiciabile.