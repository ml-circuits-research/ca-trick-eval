## Concluzie executivă

La **12.06.2026, ora 12:00 UTC**, **IR-071 este anulată**, **IR-017 este activă**, iar angajamentul total fără TVA este **8.000 EUR**. Sinteza de control este greșită cu privire la IR-071: confundă ora importării cu ordinea efectivă a evenimentelor și reactivarea obligației cu o înregistrare despre ecusoane.

**Poarta locală a trecut** (`integrity: VERIFIED`, `check_result: PASS`): amprentele ambelor exporturi coincid cu revizia cerută. Concluzia executivă de mai sus reproduce sinteza din chitanța verificată pentru acea revizie. Poarta a fost rulată local, fără scrieri sau acces la internet.

## Statut și calcul

| Cheie | Statut la momentul raportării | Sumă inclusă |
|---|---|---:|
| IR-071 | Anulată | 0 EUR |
| IR-017 | Activă | 8.000 EUR |
| **Total** |  | **8.000 EUR** |

- **IR-071 — anulată.** `01_evidente.md`, [C1]: obligația inițială este de 48.000 EUR. [C2] precizează că pentru obligații comerciale contează doar evenimentele `O` cu două semnături, ordonate după `effective_at`. În [E1], `e11` este o încetare (`X`) efectivă la 09:00 UTC, cu două semnături; `e12` este o activare (`A`) efectivă la 11:00 UTC, tot cu două semnături. Conform [C2], activarea ulterioară ar restabili obligația integrală, deci ordinea efectivă singură ar indica IR-071 activă la prânz. Însă [E2] precizează că `e12` se referă la ecuson, iar documentul a ajuns la rubrica respectivă din cauza plicului cu ecusoane. Împreună cu regula identității din [C2] — cheia este perechea tip + număr — asta înseamnă că `e12` nu reactivează obligația `O` IR-071. Rămâne în vigoare încetarea `e11`.

- **IR-017 — activă.** `01_evidente.md`, [C1]: obligația este de 8.000 EUR. În [E1], singura încetare (`e13`) este de tip `O`, dar are o singură semnătură. Potrivit [C2], aceasta nu produce efect; prin urmare obligația rămâne activă.

- **Totalul este 8.000 EUR fără TVA.** `01_evidente.md`, [C1] exclude din total prestațiile, plățile, penalitățile și comenzile suplimentare. Se include doar angajamentul activ IR-017; IR-071 anulată contribuie cu zero.

## Probleme în sinteza de control

- `02_registru.md`, [S1] afirmă că „e11 este ultima înregistrare importată”, deci IR-071 ar fi anulată. Dar [C2] spune explicit că `imported_at` este doar ora copierii; evenimentele eligibile se ordonează după `effective_at`. În plus, `e12` are `effective_at` mai târziu decât `e11`, deși a fost importată mai devreme. Motivul decisiv pentru care nu reactivează obligația este însă clasificarea ei din [E2]: ține de administrarea accesului/ecusoanelor, nu de obligația comercială `O`.

- Tot în [S1], e12 este numită „reactivarea ecusonului”. Această descriere este compatibilă cu [E2], dar nu justifică prezentarea ei ca reactivare a obligației IR-071: [C2] distinge tipurile de eveniment, iar identitatea cheii include tipul.

- `02_registru.md`, [S2] spune că valoarea de 8.000 EUR a fost copiată din [S1], fără reconciliere. Valoarea finală este totuși corectă, dar explicația și raționamentul din [S1] nu o verifică independent.

- În `01_evidente.md`, [E1] tabelul de circuit zilnic include un rând `IR-071` pentru cablare. Fără legătură explicita cu tipul și numărul din registrul de evenimente, identificatorul poate crea confuzie cu cheia comercială IR-071; conform [C2], acel circuit nu este prin el însuși un eveniment financiar eligibil.

## Fapte certe și necunoscute

**Certe în dosar:** valorile inițiale din [C1]; regulile de eligibilitate și identitate din [C2]; evenimentele, orele și semnăturile din [E1]; clasificarea lui `e12` din [E2]; și trecerea verificării locale pentru această revizie.

**Necunoscute:** dosarul nu oferă informații despre alte obligații sau evenimente în afara celor enumerate; [C3] afirmă că nu există alte evenimente pentru cele două chei `O` în registru. La întrebarea de față, totalul se bazează pe obligațiile și excluderile definite în [C1].

## Aspecte corecte

- În [S1], sinteza identifică IR-071 ca anulată; acesta este statutul corect, chiar dacă justificarea prin ora importării este greșită.
- [S1] afirmă că IR-017 nu are anulare valabilă, ceea ce corespunde regulii [C2] și evenimentului cu o singură semnătură din [E1].
- Valoarea de 8.000 EUR din [S2] coincide cu totalul rezultat din reconcilierea evenimentelor.