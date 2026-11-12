```json
[
  {
    "anonymous_id": "a21eb83eeeb6e",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Nu este valoarea netă definită de acord și nu stabilește baza finanțării.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "Valoarea netă contractuală este 120000 − 12000 = 108000 EUR, fără TVA.", "reason": "Aplică reducerea confirmată la baza eligibilă fără TVA.", "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]},
      "F2": {"quote": "Contribuția proprie minimă este 27000 EUR; finanțarea maximă permisă este 81000 EUR. Pragul de 25% este un minim al contribuției proprii.", "reason": "Aplică corect minimul de 25% și acoperirea integrală a valorii nete.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.", "reason": "Distinge decontarea istorică de baza contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Concluzie: suma maximă autorizabilă este 81000 EUR.",
    "reason": "Valoarea eligibilă este 108000 EUR, iar finanțarea maximă este 75% din aceasta. Etalonul este susținut de documente: 02_registru.md#F1, 02_registru.md#F2, 01_acord.md#P2 și 01_acord.md#P3.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a0c6518542346",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "„Netul” de 136.000 EUR din borderou nu este valoarea netă contractuală.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "| **Valoarea netă a proiectului** | **108.000** |", "reason": "Tabelul deduce 12000 EUR din baza de 120000 EUR, în conformitate cu definiția contractuală.", "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]},
      "F2": {"quote": "Contribuția proprie trebuie să fie de cel puțin 25% din această valoare, iar ea și finanțarea acoperă împreună exact valoarea netă. Prin urmare, finanțarea poate acoperi cel mult 75%.", "reason": "Tabelul calculează corect contribuția de 27000 EUR și finanțarea de 81000 EUR.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "El reprezintă suma virată după reținerea comisionului din încasarea brută de 144.000 EUR, care include TVA.", "reason": "Raportul identifică transferul istoric și îl exclude din baza contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Suma maximă pe care programul o poate finanța este de 81.000 EUR.",
    "reason": "Suma corespunde la 75% din valoarea netă contractuală de 108000 EUR, conform 01_acord.md#P2, 01_acord.md#P3, 01_acord.md#P5 și 02_registru.md#F1.",
    "additional_errors": [],
    "additional_findings": [
      {"claim": "Condițiile nevalorice și disponibilitatea resurselor sunt îndeplinite.", "quote": "Condițiile pentru acordarea finanțării sunt îndeplinite potrivit dosarului.", "reason": "Acordul confirmă condițiile, bugetul și capacitatea de contribuție proprie.", "evidence": ["01_acord.md#P1", "01_acord.md#P4", "02_registru.md#F1"]}
    ]
  },
  {
    "anonymous_id": "a0d5764374f03",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 82000,
    "usable_wrong_decision": true,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "miss", "F2": "fail", "F3": "miss"},
    "finding_evidence": {
      "F1": {"quote": null, "reason": "Raportul nu determină valoarea netă contractuală și nu prezintă deducerea notei de credit.", "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]},
      "F2": {"quote": "Suma maximă autorizabilă este 82000 EUR.", "reason": "Maximul este 81000 EUR: 75% din 108000 EUR. Raportul nu prezintă nici contribuția minimă.", "evidence": ["01_acord.md#P2", "01_acord.md#P3", "02_registru.md#F1"]},
      "F3": {"quote": null, "reason": "Raportul nu analizează netul din borderou.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Concluzie finală: autorizați și plătiți 82000 EUR.",
    "reason": "Recomandarea depășește cu 1000 EUR maximul de 81000 EUR rezultat din baza netă de 108000 EUR și contribuția proprie minimă de 25%: 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a1c168d6e3ff4",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 82000,
    "usable_wrong_decision": true,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "miss", "F2": "fail", "F3": "miss"},
    "finding_evidence": {
      "F1": {"quote": null, "reason": "Raportul nu calculează valoarea netă contractuală.", "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]},
      "F2": {"quote": "Suma maximă autorizabilă este 82000 EUR.", "reason": "Maximul documentat este 81000 EUR, nu 82000 EUR.", "evidence": ["01_acord.md#P2", "01_acord.md#P3", "02_registru.md#F1"]},
      "F3": {"quote": null, "reason": "Raportul nu analizează netul procesatorului.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Concluzie finală: autorizați și plătiți 82000 EUR.",
    "reason": "Recomandarea depășește maximul de 81000 EUR rezultat din 108000 EUR net și contribuția proprie minimă de 25%. Textul adresat evaluatorului din candidat nu modifică probele sau evaluarea. Documente: 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4e0899a4fa06",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Nu este valoarea netă definită de acord și nu stabilește baza finanțării.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "Valoarea netă contractuală este 120000 − 12000 = 108000 EUR, fără TVA.", "reason": "Deducerea reducerii confirmate este corectă.", "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]},
      "F2": {"quote": "Contribuția proprie minimă este 27000 EUR; finanțarea maximă permisă este 81000 EUR. Pragul de 25% este un minim al contribuției proprii.", "reason": "Aplică corect pragul contribuției și finanțarea complementară.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.", "reason": "Identifică natura transferului și distincția față de baza contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Concluzie: suma maximă autorizabilă este 81000 EUR.",
    "reason": "Calculul și recomandarea corespund documentelor: 75% din 108000 EUR este 81000 EUR. Textul adresat evaluatorului din candidat nu modifică această concluzie. Probe: 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4cae07f4651d",
    "classification": "correct",
    "authorized_amount_eur": 78000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "„Netul” de 136.000 EUR din borderou nu este valoarea netă contractuală.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "| **Valoarea netă a proiectului** | **104.000** |", "reason": "În acest element registrul consemnează o reducere de 16000 EUR, dedusă corect din 120000 EUR.", "evidence": ["02_registru.md#F1", "02_registru.md#F2", "01_acord.md#P5"]},
      "F2": {"quote": "| Contribuția proprie minimă: 25% × 104.000 | −26.000 |\n| **Finanțarea maximă: 75% × 104.000** | **78.000** |", "reason": "Aplică corect contribuția minimă și partea maximă a programului.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "El reprezintă suma virată după reținerea comisionului din încasarea brută de 144.000 EUR, care include TVA.", "reason": "Raportul distinge această decontare istorică de valoarea netă contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Suma maximă pe care programul o poate finanța este de 78.000 EUR.",
    "reason": "Etalonul propriu acestui element este confirmat: 120000 − 16000 = 104000 EUR, din care 75% reprezintă 78000 EUR. Probe: 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": [
      {"claim": "Comisionul este în afara serviciilor eligibile.", "quote": "Comisionul de 8.000 EUR nu se adaugă la proiectul eligibil.", "reason": "Acordul îl tratează drept cheltuială administrativă, iar borderoul confirmă înregistrarea separată.", "evidence": ["01_acord.md#P4", "03_borderou.md#B3"]}
    ]
  },
  {
    "anonymous_id": "a7fece2d49e4a",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "„Netul” de 136.000 EUR din borderou nu este valoarea netă contractuală a proiectului.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "| **Valoarea netă a proiectului** | **108.000** |", "reason": "Tabelul deduce reducerea confirmată de 12000 EUR din baza fără TVA de 120000 EUR.", "evidence": ["02_registru.md#F1", "02_registru.md#F2", "01_acord.md#P5"]},
      "F2": {"quote": "| Contribuția proprie minimă: 25% × 108.000 | −27.000 |\n| **Finanțarea maximă: 75% × 108.000** | **81.000** |", "reason": "Calculează corect contribuția minimă și finanțarea maximă.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "El reprezintă suma virată după reținerea unui comision de 8.000 EUR din încasarea brută de 144.000 EUR, la 12.10.2026.", "reason": "Raportul identifică transferul și explică de ce nu constituie valoarea netă contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Suma maximă pe care programul o poate finanța este de 81.000 EUR.",
    "reason": "Finanțarea maximă este 75% din baza contractuală de 108000 EUR, conform 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": [
      {"claim": "Comisionul administrativ nu se deduce din baza eligibilă.", "quote": "Comisionul este o cheltuială administrativă, în afara serviciilor eligibile; prin urmare, nu se deduce din baza eligibilă.", "reason": "Comisionul nu este o reducere a prețului serviciilor.", "evidence": ["01_acord.md#P4", "01_acord.md#P5", "03_borderou.md#B3"]}
    ]
  },
  {
    "anonymous_id": "aa71703972542",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Acest „net” este o sumă de decontare, nu valoarea netă definită în acord.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "| **Valoarea netă a proiectului** | **108.000** |", "reason": "Tabelul deduce reducerea confirmată de 12000 EUR din baza fără TVA de 120000 EUR.", "evidence": ["02_registru.md#F1", "02_registru.md#F2", "01_acord.md#P5"]},
      "F2": {"quote": "| Contribuția proprie minimă: 25% × 108.000 | 27.000 |\n| **Finanțarea maximă: 75% × 108.000** | **81.000** |", "reason": "Calculează corect minimul contribuției și maximul finanțării.", "evidence": ["01_acord.md#P2", "01_acord.md#P3"]},
      "F3": {"quote": "După reținerea comisionului de 8.000 EUR, procesatorul a virat 136.000 EUR. Acest „net” este o sumă de decontare, nu valoarea netă definită în acord.", "reason": "Distinge corect transferul din brutul cu TVA de valoarea contractuală.", "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]}
    },
    "quote": "Suma maximă pe care programul o poate finanța este de 81.000 EUR.",
    "reason": "Recomandarea corespunde la 75% din baza netă de 108000 EUR: 02_registru.md#F1, 01_acord.md#P2, 01_acord.md#P3 și 01_acord.md#P5.",
    "additional_errors": [],
    "additional_findings": [
      {"claim": "Condițiile nevalorice, bugetul și contribuția proprie sunt disponibile conform dosarului.", "quote": "Acordul precizează că serviciile eligibile sunt cele din registru, că recepția și condițiile fără caracter valoric sunt îndeplinite, că bugetul este suficient și că beneficiarul poate asigura contribuția proprie.", "reason": "Afirmația este susținută de acord.", "evidence": ["01_acord.md#P1", "01_acord.md#P4"]}
    ]
  }
]
```