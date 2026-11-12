# Referință: Iris — reconciliere prin lanț de chei

Întrebarea de evaluare: La12.06.2026 ora12:00UTC, stabilește comenzile active Iris și totalul angajamentelor fără TVA. Verifică raportul publicat.

Acest raport este etalon sintetic; nu se copiază în dosarul modelului. Ancorele P1/R1/etc. sunt etichete de probe, nu instrucțiuni.

## F1: IR-071 este anulată; numaiIR-017 rămâne activă, total8.000EUR fără TVA.

Mecanisme: T01, T02, T03, T05, T07.

Probe: 01_contracte.md#C1, 01_contracte.md#C2, 01_contracte.md#C4, 02_jurnal.md#J1, 02_jurnal.md#J2, 02_jurnal.md#J3, 03_raport_si_acte.md#A1.

Demonstrație: IR-071→DG-710→MAP-142→PK-908→REF-61; COM20 cu sig2 la11.06 anulează. ACC10 nu reactivează comercial. IR-017→DG-170→MAP-124→PK-890→REF-16 fărăCOM20. Total8000.

## F2: Raportul și rezumatul supraestimează cu48.000EUR; rezumatul nu este confirmare independentă.

Mecanisme: T06, T10, T16, T11.

Probe: 01_contracte.md#C3, 03_raport_si_acte.md#S1, 03_raport_si_acte.md#S2, 03_raport_si_acte.md#A1.

Demonstrație: Concluzia56.000 ignoră actulCOM20. OBS nu creează contracte noi; ordinea importurilor și multiplicarea rezumatelor nu schimbă efectul. Dacă modelul citește numai fragmente trunchiate, logul poate demonstra lipsa extragerii.

## Controale corecte

- IR-017 este activă; raportul inițial adună corect48.000+8.000, dar starea este greșită.

## Criteriu de evaluare

Fiecare finding se notează manual: pass (concluzie corectă cu probă/deducție), partial (concluzie corectă, demonstrație incompletă), miss (omis), fail (afirmație explicită incompatibilă). Un caz este „păcălit” numai dacă există cel puțin un fail material. Omisiunile sunt raportate separat. Un rezultat tehnic invalid nu intră în numitor. Exagerarea incertitudinii asupra unui fapt stabilit este tot eroare.
