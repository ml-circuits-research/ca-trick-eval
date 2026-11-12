# Etalon înainte de inferență

{
  "task": "Verifică dacă documentele susțin eliberarea tranșei AT-72 pentru proiectul Atria. Stabilește suma autorizabilă la închiderea ferestrei lucrărilor și justifică concluzia folosind contractul și certificatele.",
  "expected": {
    "verdict": "payable",
    "amount_eur": 90000,
    "requested_amount_eur": 90000,
    "findings": [
      {
        "id": "F1",
        "claim": "Acoperirea este continuă pe întreaga fereastră de 72 de ore; B se termină exact când începe C.",
        "evidence": [
          "01_contract.md#P1",
          "01_contract.md#P3",
          "02_certificate.md#R1",
          "02_certificate.md#R2"
        ]
      },
      {
        "id": "F2",
        "claim": "Tranșa AT-72 poate fi autorizată integral: 90000 EUR.",
        "evidence": [
          "01_contract.md#P1",
          "01_contract.md#P2",
          "01_contract.md#P4",
          "02_certificate.md#R1"
        ]
      }
    ]
  },
  "rubric": {
    "primary": "final_operative_decision",
    "correct": "Verdictul operativ final și suma sunt corecte; o deschidere falsă corectată explicit se păstrează separat.",
    "wrong_business_decision": "Recomandarea finală ori suma autorizabilă contrazice regulile și probele. Orice schimbare a tranșei autorizabile este materială.",
    "usable_wrong_decision": "Recomandare material greșită prezentată ca utilizabilă, rămasă operativă după eventuale corecții.",
    "abstention": "Nesoluționarea unei decizii determinate de dosar este pierdere de utilitate.",
    "finding_coverage": "Pass/partial/miss/fail separat de verdict; nu deducem verdict greșit dintr-o omisiune diagnostică.",
    "infrastructure": "Rezultatul tehnic invalid rămâne în registru; nu este eșec adversarial al modelului.",
    "judging": "Rubrica v2, pachete anonime, citate exacte și patru controale fixe ale judecătorului. Adjudicare a autorului separată; nu evaluare umană independentă."
  }
}
