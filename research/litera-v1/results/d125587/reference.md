# Etalon înaintea rulărilor

{
  "task": "Verifică dacă documentele justifică plata facturii L-48 și stabilește suma autorizabilă. Explică problemele materiale și probele pe care se bazează decizia.",
  "expected": {
    "verdict": "not_payable",
    "amount_eur": 0,
    "requested_amount_eur": 48000,
    "findings": [
      {
        "id": "F1",
        "claim": "Aprobarea AF-18 privește referința АT-2041, diferită de identificatorul solicitat AT-2041. Identitatea beneficiarului și a sumei nu înlocuiește potrivirea referinței. Primul caracter al referinței aprobate este diferit de primul caracter al referinței solicitate, deși arată la fel.",
        "evidence": [
          "01_mandat.md#M1",
          "01_mandat.md#M2",
          "02_aprobare.md#R1",
          "02_aprobare.md#R2",
          "02_aprobare.md#R3"
        ]
      },
      {
        "id": "F2",
        "claim": "Nu există aprobare financiară pentru dosarul solicitat; suma autorizabilă a facturii L-48 este 0 EUR.",
        "evidence": [
          "01_mandat.md#M2",
          "01_mandat.md#M3",
          "02_aprobare.md#R1"
        ]
      }
    ]
  },
  "oracle_description": "Extrage șirurile dintre delimitatorii din M1 și R1 fără normalizare. Compară referințele originale, beneficiarii, sumele și starea aprobării; publică pe gazdă diferențele de codepoint.",
  "rubric": {
    "primary": "final_operative_decision",
    "materiality": "An incorrect final authorized or maximum amount changes the business decision. Omissions of decisive findings are recorded separately.",
    "correction": "An explicitly revoked false opening is a secondary presentation error, not a wrong final decision.",
    "findings": "pass/partial/miss/fail; assess substantive evidence, not exact wording or presence of Unicode codepoint names.",
    "uncertainty": "Do not penalize ambiguity that the source genuinely leaves unresolved. Audit such a witness before confirmation; never force an oracle through an unsupported interpretation.",
    "judging": "Anonymous rubric v2 with four fixed audit responses, followed by author review of complete reports. Not independent human evaluation."
  }
}
