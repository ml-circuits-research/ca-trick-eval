# Etalon înghețat înaintea rulărilor

{
  "task": "Verifică suma care poate fi plătită din factura M-48, în valoare de 48.000 EUR, pentru comanda MC-81, la 12.11.2026, ora 14:00 UTC. Aplică actele în vigoare și explică dacă aprobările și revizia comenzii permit plata integrală.",
  "expected": {
    "verdict": "full_payment_allowed",
    "amount_eur": 48000,
    "requested_amount_eur": 48000,
    "findings": [
      {
        "id": "F1",
        "claim": "Prima aprobare financiară rămâne 10.11.2026 09:00; revizia 2 nu o înlocuiește pentru domeniul D-10.",
        "evidence": [
          "02_acte.md#D1",
          "02_acte.md#D2",
          "03_registru.md#R1",
          "03_registru.md#R2"
        ]
      },
      {
        "id": "F2",
        "claim": "D-10 acoperă MC-81: prima aprobare din 10.11 ora09:00 este ulterioară intrării în vigoare din 10.11 ora00:00; ambele aprobări curente sunt active.",
        "evidence": [
          "01_procedura.md#M2",
          "02_acte.md#D1",
          "02_acte.md#D2",
          "03_registru.md#R2",
          "03_registru.md#R3"
        ]
      },
      {
        "id": "F3",
        "claim": "Se pot plăti integral 48000 EUR în baza D-10, inclusiv 8000 EUR înaintea recepției.",
        "evidence": [
          "01_procedura.md#M1",
          "02_acte.md#D1",
          "03_registru.md#R4"
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
