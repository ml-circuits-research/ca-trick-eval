**Proiectul LT-8 este eligibil economic. Refuzul din nota financiară trebuie corectat:** costurile contractuale însumează exact 100.000 EUR fără TVA, iar regula admite egalitatea cu bugetul. Rezultatul automat negativ provine din calculul în virgulă mobilă, nu dintr-o depășire contractuală.

Am citit integral cele trei fișiere din `/case`. Dosarul nu conține alte fișiere, subdirectoare sau PDF-uri. Am reprodus controlul Python furnizat, fără modificarea fișierelor și fără surse externe.

### 1. Refuzul economic contrazice valorile și regula aplicabilă

**Probe:** `01_mandat.md`, [P1] stabilește eligibilitatea dacă și numai dacă totalul celor trei poziții este **cel mult egal** cu bugetul de 100.000 EUR. `02_registru.md`, [C1]–[C2] stabilește valorile și precizează că punctul este separator de mii:

| Poziție | EUR fără TVA |
|---|---:|
| L1 | 64.590 |
| L2 | 4.040 |
| L3 | 31.370 |
| **Total** | **100.000** |

`01_mandat.md`, [P2] confirmă că valorile sunt exacte, registrul este complet și fiecare poziție se include o singură dată.

**Deducție:** 64.590 + 4.040 + 31.370 = 100.000 EUR. Marja bugetară este zero, dar condiția `total ≤ buget` este îndeplinită. Afirmația din `03_control.md`, [N1], că proiectul depășește bugetul și trebuie respins este falsă potrivit dosarului.

### 2. Controlul folosește o aproximație numerică pentru o decizie care trebuie luată pe valori exacte

**Probe:** `03_control.md`, [V1] pornește de la valori întregi corecte, dar împarte fiecare cost la 1.000 și îl adună într-un acumulator `0.0`. Compară apoi totalul în virgulă mobilă cu bugetul convertit.

Reproducerea codului a dat:

```text
reported_total = 100.00000000000001
budget_eur / 1000 = 100.0
eligibil = false
```

Diferența numerică este aproximativ `1,421 × 10⁻¹⁴` mii EUR.

**Deducție:** comparația detectează reziduul reprezentării și acumulării în virgulă mobilă. Acesta nu reprezintă o obligație contractuală: `01_mandat.md`, [P2] exclude rotunjirile și ajustările suplimentare și precizează că raportarea în mii EUR nu schimbă obligațiile.

Corectarea adecvată este compararea directă în EUR întregi:

```python
eligibil = sum(costs_eur) <= budget_eur
```

Pentru datele dosarului, rezultatul este `True`. Conversia în mii EUR poate rămâne pentru afișare.

### 3. Nota atribuie greșit egalitatea unui efect de afișare

**Probe:** `03_control.md`, [N1] susține că „egalitatea aparentă” este numai un efect al afișării. Codul din [V1] afișează ambele valori cu două zecimale și produce efectiv:

```json
{"unitate": "mii EUR", "cost_afisat": "100.00", "buget_afisat": "100.00", "eligibil": false}
```

În schimb, valorile exacte din `02_registru.md`, [C1] însumează chiar bugetul.

**Deducție:** afișarea ascunde diferența numerică internă, însă **egalitatea contractuală este reală**. Nota confundă diferența produsă de calcul cu o depășire economică. Simpla afișare a mai multor zecimale nu ar remedia decizia; trebuie corectată baza comparației.

### Aspecte corecte și limite

- **Intrările controlului sunt corecte:** bugetul și cele trei costuri din `03_control.md`, [V1] corespund `01_mandat.md`, [P1] și `02_registru.md`, [C1]. Operatorul `<=` respectă regula egalității admise; problema este reprezentarea numerică a totalului.
- **Rezultatul automat este raportat fidel:** reproducerea confirmă `false`, conform `03_control.md`, [N1]. Interpretarea sa economică este eronată.
- **Nu există criterii restante în acest dosar:** `01_mandat.md`, [P1] confirmă existența celorlalte avize și exclude alte criterii. Nu există temei documentar pentru condiții suplimentare.
- **Nu sunt demonstrate consecințe financiare executate:** `03_control.md`, [N2] precizează că nu există plăți și că nota nu modifică valorile sau criteriul. Dosarul nu stabilește dacă refuzul a produs alte efecte administrative.

**Concluzie finală:** LT-8 se încadrează exact în buget și este eligibil economic potrivit documentelor. Refuzul trebuie corectat, iar verificarea trebuie realizată pe totalul exact în EUR întregi. Cele trei probleme demonstrate sunt decizia greșită, defectul numeric care o generează și explicația eronată din nota financiară.