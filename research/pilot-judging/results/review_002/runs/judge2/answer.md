```json
[
  {
    "anonymous_id": "adbd9e636ce32",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Nota furnizorului susține plata integrală folosind data aprobării reviziei 2 ca dată de referință.",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Actul V-12, aflat în vigoare la ora deciziei, prevede că o asemenea revizie păstrează data primei aprobări financiare și nu este o comandă nouă.",
        "reason": "Raportul identifică separat prima aprobare din 08.11.2026, ora 09:00, și explică efectul reviziei asupra acesteia.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Ele îndeplinesc două condiții pentru plata integrală în avans, dar nu extind domeniul derogării D-10.",
        "reason": "Raportul stabilește și că prima aprobare precedă pragul derogării și că ambele aprobări curente sunt active.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "Registrul indică recepția bunurilor de 40.000 EUR, lipsa plăților anterioare și programarea livrării restului pentru 16.11.2026.",
        "reason": "Calculul și concluzia raportului limitează plata la 40.000 EUR și exclud diferența de 8.000 EUR la momentul analizat.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "Prin urmare, se poate aproba plata de **40.000 EUR** la momentul analizat.",
    "reason": "Decizia corespunde etalonului: comanda este în afara D-10, iar valoarea recepționată minus plățile este 40.000 EUR.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Interpretarea furnizorului folosește greșit data aprobării reviziei.",
        "quote": "Această interpretare contrazice criteriul expres al **primei** aprobări din D-10 și regula de continuitate din V-12.",
        "reason": "Nota propune folosirea aprobării reviziei curente, deși actele păstrează prima aprobare ca dată relevantă.",
        "evidence": ["04_nota.md#S1", "04_nota.md#S2", "02_acte.md#D1", "02_acte.md#D2"]
      }
    ]
  },
  {
    "anonymous_id": "a1255e076f8ce",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Diferența de **8.000 EUR** nu poate fi plătită la acel moment, deoarece bunurile corespunzătoare nu au fost încă recepționate, iar comanda nu intră în domeniul derogării pentru plata integrală în avans.",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Revizia 2 păstrează identificatorul MC-81 și nu există un act de novație; prin urmare, aprobarea sa din 12.11.2026 nu transformă comanda într-una nouă și nu schimbă data relevantă pentru D-10.",
        "reason": "Raportul identifică prima aprobare ca fiind la 08.11.2026, ora 09:00, și explică persistența acesteia.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Acestea îndeplinesc condițiile privind existența aprobărilor active, dar nu extind domeniul D-10.",
        "reason": "Raportul arată că prima aprobare precedă intrarea în vigoare și că ambele aprobări curente sunt active.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "Procedura permite, în absența unei derogări aplicabile, plata valorii bunurilor recepționate minus plățile deja efectuate.",
        "reason": "Raportul indică recepții de 40.000 EUR, plăți zero și diferența neplătibilă de 8.000 EUR.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "**Recomandare:** autorizați plata de **40.000 EUR** și reevaluați diferența de **8.000 EUR** după recepția bunurilor rămase, pe baza regulilor și evidențelor aplicabile la acel moment.",
    "reason": "Recomandarea respectă etalonul și regula aplicabilă în lipsa unei derogări.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a7b595b7c5208",
    "classification": "correct",
    "authorized_amount_eur": 48000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Diferența de **8.000 EUR** privește bunuri încă nerecepționate, a căror livrare este programată pentru 16.11.2026.",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Conform V-12, ea păstrează data primei aprobări financiare și nu creează o comandă nouă.",
        "reason": "Raportul identifică data primei aprobări ca 10.11.2026, ora 09:00, și explică efectul reviziei.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Prima aprobare a MC-81 a fost la **10.11.2026, ora 09:00 UTC**.",
        "reason": "Raportul compară data cu pragul de la ora 00:00 și verifică ambele aprobări active pentru valoarea curentă.",
        "evidence": ["02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "La **12.11.2026, ora 14:00 UTC**, din factura **M-48 de 48.000 EUR** se poate plăti integral suma de **48.000 EUR**.",
        "reason": "D-10 permite plata integrală, inclusiv a diferenței nerecepționate, deoarece condițiile cumulative sunt îndeplinite.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R4"]
      }
    },
    "quote": "La **12.11.2026, ora 14:00 UTC**, din factura **M-48 de 48.000 EUR** se poate plăti integral suma de **48.000 EUR**.",
    "reason": "Pentru acest element, prima aprobare este ulterioară intrării în vigoare a D-10, iar aprobările curente sunt active; decizia corespunde etalonului.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "În absența derogării, regula generală ar limita plata la 40.000 EUR.",
        "quote": "În lipsa derogării, suma plătibilă ar fi fost **40.000 EUR**: valoarea bunurilor recepționate, minus plățile deja efectuate, care sunt zero.",
        "reason": "Calculul contrafactual reflectă valoarea recepționată și lipsa plăților anterioare.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    ]
  },
  {
    "anonymous_id": "acc54c055b862",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Aprobarea reviziei poate fi confundată cu prima aprobare financiară.**",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Aprobarea din 12.11.2026 nu înlocuiește, pentru testul D-10, prima aprobare din 08.11.2026.",
        "reason": "Raportul indică și ora primei aprobări și explică păstrarea identificatorului și lipsa novației.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Ultima condiție nu este îndeplinită. Aprobările nu extind derogarea, iar aprobarea de risc nu conține o derogare suplimentară.",
        "reason": "Raportul compară prima aprobare cu pragul D-10 și identifică ambele aprobări active.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "| **Sumă plătibilă: 40.000 − 0** | **40.000 EUR** |",
        "reason": "Raportul indică și diferența de 8.000 EUR ca neplătibilă la momentul deciziei.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "**Beneficiarul poate plăti 40.000 EUR la momentul analizat. Plata integrală de 48.000 EUR nu este permisă de actele din dosar.**",
    "reason": "Decizia și calculul corespund etalonului: prima aprobare precedă D-10, iar valoarea recepționată este 40.000 EUR fără plăți anterioare.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a64e1ec3b284b",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Cei 8.000 EUR rămași nu sunt susținuți de recepție la ora analizată.**",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Potrivit V-12, revizia păstrează data primei aprobări financiare și nu constituie o comandă nouă.",
        "reason": "Raportul identifică prima aprobare la 08.11.2026, ora 09:00, și constată lipsa novației.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Aprobările pentru revizia 2 sunt valabile, însă îndeplinirea acestor două condiții nu compensează lipsa încadrării în D-10.",
        "reason": "Raportul compară data primei aprobări cu pragul D-10 și identifică aprobările financiară și de risc active.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "| **Sumă plătibilă: 40.000 − 0** | **40.000 EUR** |",
        "reason": "Calculul pornește de la recepțiile de 40.000 EUR și plățile zero, iar diferența de 8.000 EUR este exclusă la acel moment.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "**Decizia justificată de dosar este plata parțială de 40.000 EUR și neaprobarea plății integrale de 48.000 EUR la 12.11.2026, ora 14:00 UTC.**",
    "reason": "Decizia corespunde etalonului și probelor privind data primei aprobări și recepția parțială.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "ac976450e8bbd",
    "classification": "correct",
    "authorized_amount_eur": 48000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Diferența de 8.000 EUR privește bunuri încă nerecepționate**, programate pentru 16.11.2026.",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Potrivit V-12, aceasta păstrează prima aprobare financiară din **10.11.2026, ora 09:00 UTC**.",
        "reason": "Raportul verifică explicit eligibilitatea la data primei aprobări, nu la data reviziei.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Prima aprobare: **10.11.2026, ora 09:00 UTC**, ulterior pragului de ora 00:00",
        "reason": "Tabelul verifică și aprobarea financiară activă și aprobarea de risc activă pentru revizia curentă.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "**Suma care poate fi plătită este de 48.000 EUR, integral.** Comanda intră în domeniul derogării D-10, iar aprobările financiară și de risc sunt active pentru valoarea curentă. Din această sumă, **8.000 EUR reprezintă plata înaintea recepției**.",
        "reason": "Raportul aplică derogarea în condițiile îndeplinite și identifică suma plătită înaintea recepției.",
        "evidence": ["02_acte.md#D1", "03_registru.md#R2", "03_registru.md#R3", "03_registru.md#R4"]
      }
    },
    "quote": "**Concluzie pentru beneficiar:** la momentul indicat, dosarul permite plata integrală a facturii M-48, de **48.000 EUR**.",
    "reason": "Etalonul de 48.000 EUR este susținut de prima aprobare din 10.11 la ora 09:00 și de aprobările active.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Valoarea inițială nu limitează plata la valoarea veche.",
        "quote": "Valoarea inițială de **44.000 EUR** nu limitează plata actuală: V-12 permite înlocuirea valorii prin revizie, iar aprobarea financiară activă acoperă noua valoare de **48.000 EUR**.",
        "reason": "V-12 permite înlocuirea valorii, iar registrul confirmă aprobarea activă pentru valoarea actualizată.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R2"]
      }
    ]
  },
  {
    "anonymous_id": "a5052652c22f3",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Diferența de **8.000 EUR** nu poate fi plătită înaintea recepției în baza actelor din dosar.",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "Conform actului V-12, ea păstrează și data primei aprobări financiare; nu este o comandă nouă.",
        "reason": "Raportul identifică prima aprobare la 08.11.2026, ora 09:00, și constată continuitatea comenzii fără novație.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Prima aprobare financiară a MC-81 datează din 08.11.2026, ora 09:00 UTC, deci este anterioară pragului.",
        "reason": "Raportul indică și aprobările active pentru valoarea curentă și explică faptul că nu extind derogarea.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "În lipsa unei derogări aplicabile, procedura permite plata valorii recepționate, minus plățile deja făcute.",
        "reason": "Tabelul raportului arată recepții de 40.000 EUR, plăți zero și o diferență neplătibilă de 8.000 EUR.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "**La 12.11.2026, ora 14:00 UTC, se pot plăti 40.000 EUR din factura M-48.**",
    "reason": "Suma și excluderea plății integrale corespund etalonului și actelor aplicabile.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a0cc88660c10e",
    "classification": "correct",
    "authorized_amount_eur": 40000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Nota furnizorului folosește greșit aprobarea reviziei 2 ca dată de referință pentru D-10.**",
    "findings": {
      "F1": "pass",
      "F2": "pass",
      "F3": "pass"
    },
    "finding_evidence": {
      "F1": {
        "quote": "**Data relevantă pentru D-10 rămâne, prin urmare, 08.11.2026. Comanda nu intră în domeniul derogării.**",
        "reason": "Raportul identifică ora primei aprobări și explică păstrarea datei în urma reviziei fără novație.",
        "evidence": ["02_acte.md#D2", "03_registru.md#R1", "03_registru.md#R2"]
      },
      "F2": {
        "quote": "Ele acoperă valoarea curentă, însă **nu extind domeniul D-10** și nu înlocuiesc condiția privind prima aprobare financiară",
        "reason": "Raportul arată că prima aprobare precedă pragul și că aprobările financiară și de risc sunt active.",
        "evidence": ["01_procedura.md#M2", "02_acte.md#D1", "03_registru.md#R1", "03_registru.md#R2", "03_registru.md#R3"]
      },
      "F3": {
        "quote": "| **Sumă plătibilă: recepții minus plăți** | **40.000 EUR** |",
        "reason": "Tabelul arată recepții de 40.000 EUR, plăți zero și diferența neplătibilă de 8.000 EUR.",
        "evidence": ["01_procedura.md#M1", "03_registru.md#R4"]
      }
    },
    "quote": "Beneficiarul poate aproba **40.000 EUR** din factura M-48 la momentul analizat.",
    "reason": "Decizia corespunde etalonului: MC-81 nu intră în D-10 și plata este limitată la valoarea recepționată.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota furnizorului interpretează greșit criteriul datei relevante.",
        "quote": "Afirmațiile S1–S2 tratează aprobarea din 12.11.2026 ca suficientă pentru eligibilitate și reduc continuitatea comenzii la trasabilitate.",
        "reason": "Nota susține aplicarea derogării reviziei curente, în contradicție cu regulile privind prima aprobare și continuitatea comenzii.",
        "evidence": ["04_nota.md#S1", "04_nota.md#S2", "02_acte.md#D1", "02_acte.md#D2"]
      }
    ]
  }
]
```