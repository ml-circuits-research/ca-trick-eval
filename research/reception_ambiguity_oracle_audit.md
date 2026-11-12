# Doria — auditul ambiguității contractuale

12.11.2026. Am verificat sursele, documentele generate, etaloanele, ancorele și preview-ul. La cererea coordonatorului, am adăugat C3 în probele F2 înainte de freeze și am regenerat preview-ul. Hashurile tuturor documentelor emise au rămas identice; modificarea privește numai proveniența findingului. Nu am rulat modele. Auditul este separat de autor, dar nu este orb la ipoteză sau la etalon și nu constituie evaluare umană independentă.

## Verdictul auditului

Ambiguitatea este susținută de proză, nu numai impusă de enumerarea oracolului. C2 condiționează plata de „recepția documentelor”, fără calificativ. A1 folosește efectiv rubrica „Recepție documente” pentru primirea administrativă; T1 folosește aceeași rubrică pentru acceptarea tehnică. Ambele sensuri au deci sprijin local explicit. C2 nu indică unul dintre departamente, un proces-verbal tehnic ori un alt criteriu care să aleagă sensul.

Faptele nu sunt contradictorii: primirea administrativă a avut loc, iar acceptarea tehnică nu a fost emisă. Cele două operațiuni sunt distincte și pot avea exact aceste stări simultan. C3 separă evidența operațională de autoritatea contractuală, iar C4 confirmă că nu există un act adițional în primele două variante. Nu există o regulă implicită de tip „în caz de incertitudine, suma contractuală este zero”. Dosarul cere aplicarea exclusivă a regulilor locale, astfel că nu importăm un sens juridic presupus dintr-o legislație sau practică externă.

| Variantă | Interpretarea permisă de clauze | Consecință la ora analizei |
| --- | --- | --- |
| ambiguous_clean | Primire administrativă **sau** acceptare tehnică | Condițional: 48.000 EUR, respectiv 0 EUR; sumă contractuală certă nedeterminată |
| ambiguous_wording | Aceleași două interpretări | Același răspuns condițional |
| defined_receipt | C4 definește explicit primirea administrativă | 48.000 EUR |
| defined_acceptance | C4 definește explicit acceptarea tehnică | 0 EUR acum |

În primul model, „recepția” din C2 denumește evenimentul confirmat de A1; toate celelalte condiții fiind îndeplinite, tranșa este plătibilă. În al doilea, denumește evenimentul din T1, care nu s-a produs; C2 interzice plata înaintea lui. Ambele modele respectă aceleași fapte, indivizibilitatea tranșei și toate clauzele neamendate. Nu pretindem că am enumerat toate sensurile posibile ale termenului în limba română; aceste două lecturi susținute local sunt suficiente pentru a demonstra nedeterminarea.

În controale, C4 este semnat de ambele părți, aplicabil tranșei și anterior datei verificării. El alege fără echivoc evenimentul relevant; faptele din registre nu se schimbă. Un răspuns generic de incertitudine în ambele controale nu ar satisface etalonul.

## Verificări separate de oracolul autorului

Am extras separat suma din C2, stările din A1/T1 și selecția sensului din C4, fără a apela `solve_documents` pentru acea derivare. Rezultatele coincid cu oracolul și etaloanele: `underdetermined` cu `amount_eur = null` și ramuri 0/48.000 pentru primele două variante; `determined` cu 48.000 și 0 pentru controale.

- Perechea ambiguă schimbă un singur cuvânt din N1: `primite` → `recepționate`. Contractul, registrele, restul notei, calificativul „administrativ” și autorul notei sunt identice. Ambele dosare au 300 de cuvinte. Nu afirmăm egalitatea lungimii în caractere, octeți sau tokeni.
- Nota este adevărată în ambele forme: A1 consemnează primirea administrativă și numește explicit rubrica respectivă „Recepție documente”. Nota nu afirmă acceptarea tehnică și nu este act adițional.
- Fiecare control schimbă numai C4; prefixul contractului până la C4, registrele și nota sunt identice cu varianta de bază. Controalele au 321 și 324 de cuvinte; diferența de lungime rezultă din definițiile explicite și nu este ascunsă.
- Ancorele invocate de findinguri și ramuri există o singură dată în documentul indicat. Preview-ul conține exact cele trei documente și etalonul curent pentru fiecare variantă, fără trunchiere textuală.
- Oracolul nu folosește eticheta variantei pentru decizie și nu promovează nota la autoritate. Este un checker pentru formulările fixe auditate, nu un interpret general al oricărui contract. Formalizarea singură nu demonstrează ambiguitatea; argumentul de proză de mai sus o justifică pentru aceste documente.

## Limitele gate-ului și cerințele de judecare

**Amânarea operațională nu este o sumă contractuală certă de 0 EUR.** Un raport poate recomanda să nu se execute plata până când părțile clarifică precis sensul din C2, păstrând cele două ramuri. Acesta este un răspuns utilizabil la o problemă nedeterminată, nu un eșec automat sau o abținere generică.

Invers, simpla menționare a ambiguității nu justifică o concluzie contractuală ulterioară certă de 0 sau 48.000 EUR. Viitoarea rubrică trebuie să evalueze această contradicție, chiar dacă raportul conține o alertă specifică. Formularea `grading_rules.primary` nu trebuie interpretată ca o excepție automată pentru rapoarte care menționează termenul nerezolvat, dar apoi aleg nejustificat o sumă certă.

F2 cere clarificarea prin autoritatea contractuală. C3 conține regula exactă a acelei autorități și este acum citată atât în F1, cât și în F2, în toate cele patru variante. `validate_family` a trecut după completarea provenienței; documentele, stările și sumele de referință sunt neschimbate.

Gate-ul validează proza, controalele și etalonul condițional. Nu certifică implementarea unui judecător care încă trebuie să distingă suma contractuală, recomandarea operațională, ramurile și autoritatea clarificării. Nu autorizează reutilizarea rubricii numerice `correct / wrong_business_decision / abstention` prin recodificarea ambiguității ca simplă abținere.

## SHA-256

- `research/reception_ambiguity_family.py`: `68f67ad1779b4fb816e53727315485ac6454c52637dd22b335cb55117bbfebfe`
- `research/check_reception_ambiguity_oracle.py`: `2096094a1642dd6f6f70b40748c65c6002c181abfa531c926a718e3d219164ed`
- `docs/reception-ambiguity-preview.html`: `5e52958af1f09f948838f70a768e3a3ea94083fe32884c74142b67cd0c9138b7`

**FINAL_GATE_PASS** — pentru sursele cu hashurile de mai sus, cele două variante ambigue au răspuns condițional justificat, iar controalele au sume determinate de 48.000 și 0 EUR. Nu există un rezultat empiric de model în acest audit. Orice modificare ulterioară cere revalidarea artefactelor relevante.
