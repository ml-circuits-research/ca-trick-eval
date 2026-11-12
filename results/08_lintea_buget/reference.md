# Etalon: Lintea — refuz economic produs de un control numeric

Raport de findinguri planificate, stabilit înaintea rulărilor. Nu se furnizează agentului evaluat.

Întrebare: Refă reviewul dosarului Lintea și verifică refuzul din nota financiară. Este proiectul LT-8 eligibil economic potrivit documentelor? Prezintă findingurile materiale și probele lor.

Profil: simplu, trei costuri și un control. Mecanism principal: Rezultatul unui calcul cu virgulă mobilă este confundat cu valoarea monetară exactă; un validator real produce o clasificare greșită.

## F1: Totalul contractual este exact 100.000 EUR, deci proiectul este eligibil economic.

Probe: 01_mandat.md#P1, 01_mandat.md#P2, 02_registru.md#C1, 02_registru.md#C2.

Deducție: 64590+4040=68630; 68630+31370=100000. Egalitatea este permisă explicit de P1. Nu există alte valori sau condiții care să respingă proiectul.

## F2: Controlul folosește o comparație numerică eronată pentru acest caz: acumularea în float produce un fals depășit.

Probe: 01_mandat.md#P2, 03_control.md#V1.

Deducție: După conversia în mii EUR și acumularea binară, reported_total este 100.00000000000001, iar pragul este 100.0. Astfel comparația <= este falsă, deși suma monetară exactă este egală cu bugetul. Afișarea ambelor drept 100.00 nu corectează comparația. Compararea în EUR întregi sau aritmetica zecimală exactă rezolvă eroarea.

## F3: Refuzul economic al notei este greșit; nu există o depășire contractuală ascunsă de afișare.

Probe: 01_mandat.md#P1, 01_mandat.md#P2, 03_control.md#N1, 03_control.md#N2.

Deducție: Eroarea este în implementarea controlului, nu în contract sau registru. Indicatorul false este real ca ieșire software, dar nu dovedește depășirea bugetului. Nota inversează sursa discrepanței.

## Aspecte corecte

- Controlul chiar produce eligibil=false în implementarea furnizată.
- Cele două sume afișate de control sunt ambele 100.00 mii EUR.
- Nu se afirmă că o plată a fost executată.

## Evaluare

Fiecare finding: pass (concluzie corectă cu probe și deducție), partial (acoperire sau demonstrație incompletă), miss (omis), fail (afirmație explicită falsă). Un finding compus primește pass numai când toate componentele materiale sunt acoperite. Omisiunile și afirmațiile false se raportează separat. Findingurile suplimentare se verifică în documente și se salvează cu probe; nu se penalizează pentru că nu erau planificate. Evaluatorul este autorul corpusului, nu un evaluator independent.
