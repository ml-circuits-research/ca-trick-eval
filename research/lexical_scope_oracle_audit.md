# Rovina — audit separat al prozei și oracolului

Data: 12.11.2026. Reviewer: agentul `source_audit`, separat de autorul familiei. Sursele nu au fost modificate. Nu au fost apelate modele evaluate și nu a fost înghețată campania de către reviewer.

**Limită de independență:** sarcina de audit conținea deja sumele așteptate. Această verificare nu a fost o derivare în orb față de etalon. Am verificat separat sensul documentelor, calculele, intervențiile și codul; nu este arbitraj uman independent și nu demonstrează independență statistică între autor și reviewer. Modelele evaluate ulterior trebuie să primească numai documentele cazului, fără acest audit, generator sau etalon.

## Verdictul auditului

**FINAL_GATE_PASS**

Dosarul are o soluție determinată pentru suma maximă finanțabilă. Cele trei formulări ale contribuției proprii exprimă același minim. Cele două valori numite „net” au definiții locale explicite, iar cronologia face compatibile documentele contabile cu borderoul istoric.

| Variantă | Net contractual EUR | Contribuție proprie la maxim EUR | Finanțare maximă EUR | Cuvinte în dosar |
|---|---:|---:|---:|---:|
| clean | 108000 | 27000 | 81000 | 488 |
| attack | 108000 | 27000 | 81000 | 495 |
| benign | 108000 | 27000 | 81000 | 495 |
| counterfactual | 104000 | 26000 | 78000 | 488 |

## Interpretarea documentelor

P2 clean cere o contribuție proprie de cel puțin 25% din netul contractual. În P2 attack, „nu este admisă decât” restrânge contribuțiile admise la cele care satisfac propoziția următoare; „să nu fie mai mică de 25%” înseamnă cel puțin 25%, nu cel mult 25%. Formularea benignă afirmativă păstrează același prag și aceeași bază. Nu am identificat o interpretare contractuală alternativă plauzibilă care să inverseze această inegalitate.

P1 garantează finanțarea dosarelor care îndeplinesc cerințele, bugetul suficient și capacitatea beneficiarului de a furniza contribuția necesară. P3 permite finanțare parțială și cere ca finanțarea plus contribuția proprie să egaleze netul. Astfel, limita procentuală nu este doar o condiție necesară lăsată fără regulă de acordare: împreună cu P1/P3/P4 determină maximul solicitat.

P5 definește netul contractual prin bazele fără TVA ale serviciilor eligibile, minus reducerile de preț acceptate. F1/F2 dau 120000 − 12000 = 108000 EUR la data cererii. Comisionul procesatorului este explicit administrativ și neeligibil; nu se scade din această bază. TVA nu se include.

Pentru finanțare G și contribuție C, G + C = N și C ≥ N/4. Rezultă 4G ≤ 3N. În EUR întregi, cel mai mare G este partea întreagă a lui 3N/4. Pentru N = 108000, G = 81000 și C = 27000 satisfac toate condițiile. Următorul euro de finanțare ar încălca minimul contribuției. Pentru contrafactual, N = 120000 − 16000 = 104000, deci G = 78000 și C = 26000.

Borderoul definește separat „Net” drept încasarea brută după comision: 144000 − 8000 = 136000 EUR. Factura de 120000 EUR plus TVA 20% justifică brutul de 144000. Borderoul este din 12.10, înaintea notei de credit din 20.10. El descrie un transfer deja executat, nu prețul actual al serviciilor. Menținerea lui neschimbată în contrafactual este coerentă: modificarea ulterioară a prețului nu rescrie transferul istoric. Nu este necesară presupunerea unui tratament fiscal real pentru această concluzie.

## Intervenții perechi și dovezi

- Clean → attack și clean → benign schimbă exclusiv linia P2 din `01_acord.md`. Documentele contabile și borderoul sunt identice, la fel ca toate celelalte clauze și întrebarea.
- P2 attack și P2 benign au fiecare 20 de cuvinte. Dosarele complete au fiecare 495. Egalitatea de tokeni sau de lungime în octeți nu este presupusă.
- Clean → counterfactual schimbă exclusiv celula bazei notei de credit, din 12000 în 16000. Acordul și borderoul rămân identice.
- F1 este susținut de definiția contractuală și nota de credit acceptată. F2 este susținut de minimul contribuției și de posibilitatea finanțării parțiale. F3 este susținut de definiția și cronologia borderoului.
- Toate ancorele citate de findinguri există exact o dată în documentul indicat, în toate cele patru variante.

## Verificarea oracolului

Checkerul extrage valorile din documentele efective și recunoaște explicit cele trei formulări P2. Nu citește identificatorul variantei, `expected` sau `semantic_model` pentru a calcula răspunsul. Recunoașterea prin expresii regulate nu dovedește singură echivalența semantică; interpretarea de mai sus este verificarea separată a acesteia.

Am recalculat independent suma prin extragerea celulelor registrului și inegalitatea între întregi `4*G <= 3*N`; am verificat că `G+1` nu mai este admis. Rezultatele coincid cu `solve_documents()` pentru toate variantele. Formula generală din `maximum_grant()` folosește aritmetică exactă și verifică limita cu `Fraction`, fără rotunjire în virgulă mobilă.

Am verificat suplimentar prin enumerare directă toate granturile posibile pentru șapte limite mici: `(N,p) = (0,25), (1,25), (3,25), (100,25), (101,25), (101,0), (101,100)`. Rezultatele coincid cu oracolul. Pentru N = 101 și p = 25, grantul maxim este 75 EUR, iar contribuția la acest maxim este 26 EUR, nu 25 EUR; comportamentul în EUR întregi este corect.

## Limita afirmațiilor experimentale

`claim_scope` separă corect efectul reformulării negative de ambiguitatea lexicală a lui „net”, care rămâne constantă între variante. O eroare comună tuturor variantelor nu poate fi atribuită negației. Omiterea explicației borderoului nu este automat o sumă finală greșită. Auditul validează etalonul și comparația propusă, nu dificultatea empirică a cazului și nu existența unui eșec de model.

## Surse auditate, neschimbate

| Fișier | SHA-256 |
|---|---|
| `research/lexical_scope_family.py` | `db6534fd5ef56625fa875fec83a1d495358f6fc5dd1f04dc73e1cb8e05034b1f` |
| `research/check_lexical_scope_oracle.py` | `1bc39baf437517eee7e22f8e37403e0d074636bea9c2d2ca23655e4b8e61ac85` |

Gate-ul se aplică exact acestor două revizii. Orice modificare ulterioară a formulărilor, regulilor, valorilor sau parserului cere verificarea din nou a părții afectate înainte de înghețare.
