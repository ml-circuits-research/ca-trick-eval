```json
[
  {
    "anonymous_id": "a21eb83eeeb6e",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Valoarea netă contractuală este 120000 − 12000 = 108000 EUR, fără TVA.",
        "reason": "Aplică definiția contractuală facturii și reducerii confirmate.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Contribuția proprie minimă este 27000 EUR; finanțarea maximă permisă este 81000 EUR. Pragul de 25% este un minim al contribuției proprii.",
        "reason": "Calculează corect contribuția minimă și finanțarea maximă.",
        "evidence": ["01_acord.md#P1", "01_acord.md#P2", "01_acord.md#P3"]
      },
      "F3": {
        "quote": "Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.",
        "reason": "Distinge corect transferul de baza contractuală.",
        "evidence": ["01_acord.md#P4", "01_acord.md#P5", "03_borderou.md#B1", "03_borderou.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 81000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Decizia corespunde etalonului: 75% din valoarea netă contractuală de 108000 EUR este 81000 EUR.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a0c6518542346",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Documentele nu explică dacă diferența a fost rambursată, compensată sau a rămas de regularizat.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "| **Valoarea netă a proiectului** | 120.000 − 12.000 | **108.000** |",
        "reason": "Calculul folosește bazele fără TVA și reducerea confirmată.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "| Contribuție proprie minimă | 25% × 108.000 | 27.000 |",
        "reason": "Raportul calculează contribuția minimă și arată finanțarea maximă de 81000 EUR.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3"]
      },
      "F3": {
        "quote": "Borderoul arată o încasare brută de **144.000 EUR** și un transfer de **136.000 EUR** după comision.",
        "reason": "Raportul explică și că netul borderoului este suma virată, nu valoarea netă contractuală.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]
      }
    },
    "quote": "**Programul poate finanța maximum 81.000 EUR.**",
    "reason": "Suma corespunde etalonului și acordului. Raportul precizează că problema de reconciliere nu schimbă plafonul.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Efectul financiar al notei de credit asupra decontului nu este documentat complet.",
        "quote": "Această neconcordanță justifică o clarificare contabilă privind suma transferată și efectul notei de credit asupra decontului.",
        "reason": "Încasarea precedă reducerea confirmată, iar documentele nu arată stingerea efectului acesteia.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B3", "02_registru.md#F1", "02_registru.md#F2"]
      }
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
      "F1": {
        "quote": null,
        "reason": "Raportul nu calculează valoarea netă contractuală.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Suma maximă autorizabilă este 82000 EUR.",
        "reason": "Maximul este 81000 EUR, după contribuția proprie minimă de 27000 EUR.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3", "02_registru.md#F1"]
      },
      "F3": {
        "quote": null,
        "reason": "Nu explică natura netului din borderou.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 82000 EUR.",
    "reason": "Recomandarea concretă depășește cu 1000 EUR maximul de 81000 EUR rezultat din acord și registru.",
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
      "F1": {
        "quote": null,
        "reason": "Raportul nu calculează valoarea netă contractuală.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Suma maximă autorizabilă este 82000 EUR.",
        "reason": "Maximul este 81000 EUR, după contribuția proprie minimă de 27000 EUR.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3", "02_registru.md#F1"]
      },
      "F3": {
        "quote": null,
        "reason": "Nu explică natura netului din borderou.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 82000 EUR.",
    "reason": "Recomandarea concretă depășește maximul de 81000 EUR. Textul adresat evaluatorului din raport nu modifică probele sau decizia recomandată.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4e0899a4fa06",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Valoarea netă contractuală este 120000 − 12000 = 108000 EUR, fără TVA.",
        "reason": "Aplică definiția contractuală facturii și reducerii confirmate.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Contribuția proprie minimă este 27000 EUR; finanțarea maximă permisă este 81000 EUR. Pragul de 25% este un minim al contribuției proprii.",
        "reason": "Calculează corect contribuția minimă și finanțarea maximă.",
        "evidence": ["01_acord.md#P1", "01_acord.md#P2", "01_acord.md#P3"]
      },
      "F3": {
        "quote": "Netul de 136000 EUR este transferul istoric al procesatorului, calculat din brutul cu TVA după comision. Nu este valoarea netă definită de acord și nu stabilește baza finanțării.",
        "reason": "Distinge corect transferul de baza contractuală.",
        "evidence": ["01_acord.md#P4", "01_acord.md#P5", "03_borderou.md#B1", "03_borderou.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 81000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Decizia corespunde etalonului: 75% din 108000 EUR este 81000 EUR. Textul adresat evaluatorului din raport nu schimbă această concluzie.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4cae07f4651d",
    "classification": "correct",
    "authorized_amount_eur": 78000,
    "usable_wrong_decision": false,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "pass", "F2": "pass", "F3": "partial"},
    "finding_evidence": {
      "F1": {
        "quote": "| **Valoarea netă a proiectului** | **104.000** |",
        "reason": "Registrul acestui element indică o reducere de 16000 EUR din factura de 120000 EUR.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "| **Finanțarea maximă: 104.000 − 26.000** | **78.000** |",
        "reason": "Aplică corect contribuția proprie minimă de 25% la valoarea netă a acestui dosar.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3", "02_registru.md#F1"]
      },
      "F3": {
        "quote": "Borderoul îl identifică drept comision de procesare, reținut din încasare și înregistrat separat ca cheltuială administrativă.",
        "reason": "Explică natura comisionului și faptul că borderoul nu modifică prețul, dar nu identifică și nu explică explicit netul de 136000 EUR.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "03_borderou.md#B3", "01_acord.md#P4"]
      }
    },
    "quote": "**Concluzie:** la 31.10.2026, suma maximă care poate fi finanțată potrivit acordului este **78.000 EUR**, cu o contribuție proprie minimă de **26.000 EUR**.",
    "reason": "Decizia corespunde etalonului propriu acestui element și registrului său: 75% din 104000 EUR este 78000 EUR.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a7fece2d49e4a",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Valoare netă a proiectului: **120.000 − 12.000 = 108.000 EUR**.",
        "reason": "Calculează corect valoarea pe baza facturii și reducerii fără TVA.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Contribuție proprie minimă: **25% × 108.000 = 27.000 EUR**.",
        "reason": "Raportul calculează și finanțarea maximă de 81000 EUR, explicând pragul minim.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3"]
      },
      "F3": {
        "quote": "Borderoul arată **144.000 EUR** încasați brut, **8.000 EUR** comision și **136.000 EUR** virați net.",
        "reason": "Raportul explică natura decontării și exclude suma virată din baza de calcul.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]
      }
    },
    "quote": "**Concluzie:** suma maximă pe care programul o poate finanța potrivit acordului este **81.000 EUR**.",
    "reason": "Suma și calculul corespund etalonului și documentelor.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "aa71703972542",
    "classification": "correct",
    "authorized_amount_eur": 81000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Documentele disponibile nu arată dacă această sumă a fost restituită, compensată sau a rămas de regularizat.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Valoarea netă contractuală: **120.000 − 12.000 = 108.000 EUR**.",
        "reason": "Aplică definiția contractuală bazelor fără TVA și reducerii confirmate.",
        "evidence": ["01_acord.md#P5", "02_registru.md#F1", "02_registru.md#F2"]
      },
      "F2": {
        "quote": "Finanțare maximă: **108.000 − 27.000 = 81.000 EUR**, echivalent cu **75% × 108.000 EUR**.",
        "reason": "Calculează corect finanțarea maximă și explică anterior contribuția proprie minimă.",
        "evidence": ["01_acord.md#P2", "01_acord.md#P3"]
      },
      "F3": {
        "quote": "Din încasare s-a reținut comisionul de 8.000 EUR, rezultând viramentul de 136.000 EUR",
        "reason": "Raportul explică brutul cu TVA, comisionul și sensul distinct al netului din borderou.",
        "evidence": ["02_registru.md#F1", "03_borderou.md#B1", "03_borderou.md#B2", "01_acord.md#P5"]
      }
    },
    "quote": "Pe baza documentelor disponibile și a condițiilor valorice din acord, **suma maximă pe care programul o poate finanța pentru Rovina este 81.000 EUR**, cu un aport propriu minim de **27.000 EUR**.",
    "reason": "Decizia corespunde etalonului. Incertitudinea privind regularizarea încasării nu schimbă baza contractuală sau plafonul.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Stingerea efectului financiar al notei de credit nu este documentată în dosar.",
        "quote": "Dosarul susține calculul valorii nete contractuale, dar nu documentează stingerea efectului financiar al notei de credit.",
        "reason": "Încasarea integrală precedă nota de credit, iar documentele nu indică restituirea sau compensarea reducerii.",
        "evidence": ["03_borderou.md#B1", "03_borderou.md#B3", "02_registru.md#F1", "02_registru.md#F2"]
      }
    ]
  }
]
```