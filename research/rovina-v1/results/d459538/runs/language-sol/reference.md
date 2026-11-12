# Etalon înaintea rulărilor

{
  "task": "Analizează dosarul Rovina la 31.10.2026. Care este suma maximă, în EUR, pe care programul o poate finanța potrivit acordului? Prezintă calculul și constatările materiale susținute de documente.",
  "expected": {
    "verdict": "payable_up_to_limit",
    "amount_eur": 78000,
    "findings": [
      {
        "id": "F1",
        "claim": "Valoarea netă contractuală este 120000 − 16000 = 104000 EUR, fără TVA.",
        "evidence": [
          "01_acord.md#P4",
          "01_acord.md#P5",
          "02_registru.md#F1",
          "02_registru.md#F2",
          "02_registru.md#F3"
        ]
      },
      {
        "id": "F2",
        "claim": "Contribuția proprie minimă este 26000 EUR; finanțarea maximă permisă este 78000 EUR. Pragul de 25% este un minim al contribuției proprii.",
        "evidence": [
          "01_acord.md#P1",
          "01_acord.md#P2",
          "01_acord.md#P3",
          "02_registru.md#F1"
        ]
      },
      {
        "id": "F3",
        "claim": "Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.",
        "evidence": [
          "01_acord.md#P4",
          "01_acord.md#P5",
          "02_registru.md#F1",
          "03_borderou.md#B1",
          "03_borderou.md#B2"
        ]
      }
    ]
  },
  "oracle_description": "Parsează exclusiv faptele și clauza efectivă din cele trei documente; mapează formulările recunoscute la aceeași limită minimă. Calculează finanțarea în EUR întregi, fără eticheta variantei sau semantic_model.",
  "rubric": {
    "primary": "final_operative_decision",
    "materiality": "An incorrect final authorized or maximum amount changes the business decision. Omissions of decisive findings are recorded separately.",
    "correction": "An explicitly revoked false opening is a secondary presentation error, not a wrong final decision.",
    "findings": "pass/partial/miss/fail; assess substantive evidence, not exact wording or presence of Unicode codepoint names.",
    "uncertainty": "Do not penalize ambiguity that the source genuinely leaves unresolved. Audit such a witness before confirmation; never force an oracle through an unsupported interpretation.",
    "judging": "Anonymous rubric v2 with four fixed audit responses, followed by author review of complete reports. Not independent human evaluation."
  }
}
