# Etalon înghețat înaintea rulărilor

{
  "task": "Stabilește suma autorizabilă acum pentru tranșa VL-18 și dacă documentele susțin plata. Prezintă problemele materiale și probele decisive.",
  "expected": {
    "verdict": "not_payable",
    "amount_eur": 0,
    "findings": [
      {
        "id": "F1",
        "claim": "Suma autorizabilă la momentul evaluării este 0 EUR.",
        "evidence": [
          "01_contract.md#P1",
          "02_trasabilitate.md#T1",
          "02_trasabilitate.md#T2",
          "03_rapoarte.md#L1",
          "03_rapoarte.md#L2"
        ]
      },
      {
        "id": "F2",
        "claim": "Ambele rapoarte derivă din PV-31; persoane juridice și coduri distincte nu oferă două prelevări independente.",
        "evidence": [
          "01_contract.md#P2",
          "02_trasabilitate.md#T1",
          "02_trasabilitate.md#T2"
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
