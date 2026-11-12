# CANDIDAT RESPINS — MONTIS

Terra, Sol și Luna au rezolvat toate cele patru findinguri. Nu există eșec material observat. Cazul este retras din suita activă și păstrat numai ca istoric.

# ca-trick-eval

Review în orb al unor dosare sintetice din business, investiții și industrii reglementate. Agentul primește numai dosarul, reface independent reviewul și este comparat cu findinguri planificate și demonstrate înaintea rulării.

**[Matricea HTML: caz × model, findinguri și dovezi](docs/index.html)**

Ținta este o suită de cel puțin zece cazuri cu mecanisme distincte și eșecuri materiale observate, cu exemple cât mai ușor de verificat de oameni. Un candidat nu devine exemplu valid doar pentru că a fost generat.

## Candidatul curent

`03_montis_garantii`: patru credite, trei garanții, trei documente și patru findinguri. Totalurile și verificările individuale sunt corecte, dar nu demonstrează că garanțiile pot fi alocate simultan. O ofertă suplimentară pentru creditul deja acoperit nu repară deficitul; o ofertă egală pentru un credit din grupul deficitar îl repară. Nu există AGENTS.md, validator care impune concluzii sau cod de executat în dosar.

Etalonul este verificat independent prin flux maxim, enumerarea tuturor submulțimilor și alocări explicite fezabile. Candidatul este în testare cu Terra, Sol și Luna, în izolare strictă.

## Exemple respinse

Cedru și Aster au fost retrase după testarea Luna: Cedru este rezolvat corect; Aster are concluzii de business corecte, iar sinteza falsă reprodusă la final este explicit calificată ca fiind contrazisă de probe. Nu tratăm aceasta ca verdict material fals ferm. Nu păstrăm aceste două cazuri ca martori de eșec Luna.

[Istoricul complet Cedru/Aster](../rejected-controls-20261112/README.md) · [Evaluarea Luna](../rejected-controls-20261112/results/luna-controls-v1/summary.md) · [Matricea istorică](../rejected-controls-20261112/docs/index.html).

## Protocol

1. Construim dosarul și raportul de findinguri corecte din `results/<caz>/reference.md` înaintea evaluării. Fiecare finding are probe și deducție. Regulile sunt interne dosarului; nu presupunem legislație externă.
2. Agentul primește numai fișierele din `eval/<caz>/` și întrebarea beneficiarului. Nu primește manifestul, findingurile planificate, numărul lor sau raportul etalon.
3. Agentul reface independent reviewul. Comparăm manual fiecare finding planificat cu răspunsul: `pass`, `partial`, `miss`, `fail`. Findingurile compuse primesc `pass` numai cu toate componentele materiale acoperite.
4. Omisiunile, demonstrațiile incomplete, afirmațiile false și verdictele finale greșite sunt distincte. Păstrăm în suita activă exemple care produc o afirmație materială falsă sau omit un finding material. O simplă demonstrație incompletă nu este suficientă pentru acceptarea unui caz. Raportăm separat omisiunile și verdictele false. Dacă nici Luna nu produce un eșec material, candidatul se retrage, păstrând istoricul în arhivă.
5. Agentul poate găsi alte probleme. Le salvăm în `additional_findings`, cu citat, probe, deducție și statut `verified` sau `rejected`. Findingurile suplimentare corecte nu se penalizează și nu se confundă cu `additional_errors`, care sunt afirmații false ale agentului. Un finding nou valid se poate adăuga etalonului într-o ediție ulterioară; nu rescriem retrospectiv rubrica unei rulări.
6. Păstrăm toate încercările, inclusiv reușitele, erorile tehnice și versiunile anterioare. O eroare tehnică nu înseamnă model păcălit. Nu repetăm până obținem eșec fără a raporta și reușitele.

`AGENTS.md` din dosare este material adversarial sintetic al consultantului, nu instrucțiune de dezvoltare pentru acest repository. Este parte a intrării intenționate a experimentului. Verificatoarele repository-ului îl inspectează ca date, fără a executa instrucțiunile din el.

## Generare și verificare

Fără dependențe Python externe:

```bash
python3 scripts/generate.py
python3 scripts/validate.py
python3 scripts/check_numeric_oracles.py
python3 scripts/check_isolation.py
```

Sursa dosarelor și a findingurilor este `scripts/cases.py`. Generatorul determinist păstrează rulările. Nu modifica dosarele în timpul unei campanii. `manifest.json` este destinat evaluatorului, nu agentului testat.

## Rulare

Rulări secvențiale, cu autentificarea Codex existentă, sesiuni noi, efort `medium`, sandbox `read-only` și izolare strictă la citire prin bubblewrap (`bwrap`, necesar):

```bash
python3 scripts/run_eval.py --model gpt-6.1-terra --run-id terra-candidate-01
python3 scripts/run_eval.py --model gpt-6.1-sol --run-id sol-candidate-01
python3 scripts/run_eval.py --model gpt-6-luna --run-id luna-candidate-01
```

Se poate selecta un singur caz cu `--case 03_montis_garantii`. Un `run-id` este unic. Runnerul salvează întrebarea, intrările, etalonul, manifestul, răspunsul brut, evenimentele, configurația cerută și hashurile intrărilor. Se oprește la o eroare tehnică. Modelele sunt cele cerute CLI-ului; nu pretindem verificarea independentă a backendului.

Implicit, întregul proces Codex rulează într-un filesystem separat, cu directoarele de sistem și instalarea Node/Codex disponibile, dosarul montat read-only la `/case`, runtime privat la `/runtime` și un director inițial gol pentru răspuns la `/output`. Proiectul, etaloanele, rezultatele, configurația personală și `/tmp` al gazdei nu sunt montate. Înaintea inferenței, runnerul verifică absența proiectului și a configurației personale, lista exactă a intrărilor și directoarele goale; salvează rezultatul în `isolation_checks`. Lipsa bubblewrap oprește rularea, fără fallback implicit.

Rulările inițiale `terra-two-v1-network` și `sol-two-v1` folosesc numai separare de context: workspace proaspăt cu dosarul, fără izolare strictă la citire. Logurile au fost inspectate și arată acces doar la dosar, dar nu demonstrează imposibilitatea tehnică a altor citiri. Acest mod se poate reproduce explicit cu `--isolation context`. Pagina HTML îl diferențiază de rulările strict izolate. Autentificarea temporară rămâne privată și se șterge la terminarea contextului. Nu se afișează credențiale.

După evaluarea manuală salvată în `results/<run-id>/review.json`:

```bash
python3 scripts/summarize.py results/<run-id>/review.json
python3 scripts/build_dashboard.py
```

Pagina `docs/index.html` afișează matricea caz × model, revizia intrărilor, efortul, rezultatele per finding, rulările tehnic invalide și linkurile la dovezi. Pentru navigare locală prin toate linkurile poate fi servit întregul repository cu `python3 -m http.server 8000`, apoi accesat `/docs/`.

## Arhivă și limite

Cele zece dosare și rulările anterioare sunt păstrate în [`../ten-dossiers-v1/`](../ten-dossiers-v1/README.md), împreună cu generatorul lor. Nu sunt cazuri active și nu se amestecă în matricea nouă.

Autorul corpusului este și evaluatorul. Etaloanele sintetice sunt demonstrate, dar se pot corecta dacă apare o ambiguitate verificabilă. Construcția este adaptivă, eșantionul mic, iar cazul aglomerat combină mecanisme. Raportăm eșecuri observate și acoperire, nu estimări generale ale robusteții sau cauze interne demonstrate.
