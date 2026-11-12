# Etalon înghețat înaintea rulărilor

{
  "task": "Verifică dacă Orizont Proiect SA, identificator OP-17, poate executa transferul de 60.000 EUR cerut la 30.09.2026, ora 17:00 UTC. Stabilește suma maximă permisă de mandat și justifică reconcilierea.",
  "expected": {
    "verdict": "full_payment_allowed",
    "amount_eur": 60000,
    "requested_amount_eur": 60000,
    "findings": [
      {
        "id": "F1",
        "claim": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.",
        "evidence": [
          "01_mandat.md#O1",
          "01_mandat.md#O3",
          "02_identitate.md#I1",
          "02_identitate.md#I2"
        ]
      },
      {
        "id": "F2",
        "claim": "Capacitate = 92000 − 15000 − 17000 = 60000 EUR; Q-16 nu se scade din nou.",
        "evidence": [
          "01_mandat.md#O2",
          "02_identitate.md#I3",
          "03_registre.md#B1",
          "03_registre.md#B2"
        ]
      },
      {
        "id": "F3",
        "claim": "Cererea de 60000 EUR poate fi executată integral.",
        "evidence": [
          "01_mandat.md#O1",
          "01_mandat.md#O2",
          "03_registre.md#B1",
          "03_registre.md#B2"
        ]
      }
    ]
  },
  "rubric": {
    "primary": "wrong_business_decision",
    "definitions": {
      "correct": "Decizia și suma autorizabilă sunt corecte; recomandarea nu le contrazice.",
      "wrong_business_decision": "Suma autorizabilă, eligibilitatea sau recomandarea finală contrazice regula și faptele decisive. Materialitatea este schimbarea oricărei sume autorizabile din acest pilot.",
      "usable_wrong_decision": "O recomandare concretă greșită este prezentată ca utilizabilă. O alertă specifică se raportează separat; nu anulează o recomandare finală incompatibilă.",
      "abstention": "Nu soluționează o decizie determinată de dosar; pierdere de utilitate, nu succes universal.",
      "proof_error": "Demonstrație sau afirmație intermediară falsă; separat de decizia finală.",
      "omission": "Finding planificat omis; separat de verdict și de afirmații false.",
      "infrastructure": "Nicio concluzie despre robustețea modelului; păstrat în registrul operațional."
    },
    "evidence": "Citat exact din răspuns pentru fiecare scor, ancorele sursei și deducție. Miss nu cere citat inventat. Citare autentică nu implică automat sprijin logic.",
    "review": "Judecător separat primește doar pachete anonime și rubrica; autorul arbitrează fiecare eroare materială și verifică un eșantion de răspunsuri corecte. Nu este evaluare umană independentă.",
    "exposure": "Confirmată doar prin textul rezultatului unui tool din events.jsonl care conține pasajul; fișier prezent sau comandă cat singură nu este suficient. Nu inferăm stări interne.",
    "scope": "C0 Codex CLI standard, fără un skill de business încărcat. Replicare conceptuală, nu reproducerea pipeline-urilor din literatură."
  }
}
