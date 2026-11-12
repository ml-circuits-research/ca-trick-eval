```json
[
  {
    "anonymous_id": "a0d5764374f03",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "folosirea lor pentru aprobarea cererii actuale ar confunda perioada și persoana juridică",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Datele pentru C25 și cele pentru grup nu substituie situația solicitantului la C26.",
        "reason": "Raportul identifică separat OP-17 cu P-17 și momentul cererii cu C26, excluzând perioada istorică și grupul.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "| **Capacitate maximă** | **92.000 − 23.000 − 17.000** | **52.000** |",
        "reason": "Calculul este corect, iar tabelul și explicația aferentă exclud o nouă deducere a Q-16 deja debitat.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă de mandat este de 52.000 EUR; cererea depășește limita cu 8.000 EUR.",
        "reason": "Raportul respinge executarea integrală și stabilește corect plafonul și deficitul.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Un transfer de cel mult **52.000 EUR** se încadrează în capacitatea calculată la momentul solicitat.",
    "reason": "Plafonul și respingerea transferului integral corespund capacității OP-17 la C26: 92.000 − 23.000 − 17.000 EUR. Q-16 este deja debitat. [01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Capacitatea istorică OP-17 la C25 este 60.000 EUR.",
        "quote": "**Cei 60.000 EUR din N1 sunt corecți pentru C25:** 100.000 − 23.000 − 17.000 = 60.000 EUR.",
        "reason": "Calculul reconciliază corect fișa istorică, fără a o aplica cererii curente.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "04_nota.md#N1"]
      },
      {
        "claim": "Suma capacităților celor două societăți la C26 este 600.000 EUR.",
        "quote": "OP-17 are 52.000 EUR, iar OS-71 are 581.000 − 33.000 = 548.000 EUR. Totalul este 600.000 EUR",
        "reason": "Suma este corectă pentru grup, dar nu reprezintă disponibilul solicitantului.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "01_mandat.md#O3", "04_nota.md#N2"]
      }
    ]
  },
  {
    "anonymous_id": "a1c168d6e3ff4",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": true,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "miss", "F2": "miss", "F3": "fail"},
    "finding_evidence": {
      "F1": {
        "quote": null,
        "reason": "Raportul nu identifică rândul aplicabil și nu distinge perioada sau perimetrul grupului.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": null,
        "reason": "Nu prezintă calculul și nici tratamentul ordinului Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă autorizabilă este 60000 EUR. Recomand autorizarea și plata sumei de 60000 EUR",
        "reason": "Afirmă permisibilitatea integrală, deși plafonul este 52.000 EUR și deficitul este 8.000 EUR.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Recomandarea concretă depășește cu 8.000 EUR capacitatea stabilită pentru P-17 la C26. [01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4e0899a4fa06",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.",
        "reason": "Selectează entitatea și închiderea cerute și exclude alternativele nerelevante.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.",
        "reason": "Aplică valorile și tratamentul corect al ordinelor.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
        "reason": "Verdictul, plafonul și deficitul sunt corecte.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Recomandarea respectă capacitatea determinată de mandat și registre. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4cae07f4651d",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": true,
    "specific_warning": true,
    "warning_quote": "Calculul arată însă o capacitate de **52.000 EUR**, astfel că transferul cerut **nu poate fi executat integral**.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "fail"},
    "finding_evidence": {
      "F1": {
        "quote": "P-17 este codul intern al Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii.",
        "reason": "Raportul exclude și rândurile istorice și perimetrul grupului în explicațiile ulterioare.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Q-16, de 8.000 EUR, este deja debitat și reflectat în soldul C26; nu se mai deduce.",
        "reason": "Tabelul aplică 92.000 − 23.000 − 17.000 și identifică tratamentul corect al Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Orizont Proiect SA, identificator OP-17, poate executa integral transferul de **60.000 EUR**",
        "reason": "Concluzia afirmă greșit că plata integrală este permisă, deși corpul raportului o contrazice și calculează corect deficitul.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**Concluzie:** Orizont Proiect SA, identificator OP-17, poate executa integral transferul de **60.000 EUR** cerut la 30.09.2026, ora 17:00 UTC.",
    "reason": "Concluzia explicită autorizează integral o cerere care depășește plafonul de 52.000 EUR. Corpul o contrazice și avertizează corect asupra deficitului de 8.000 EUR; această contradicție nu neutralizează verdictul incompatibil din rezumat. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a7fece2d49e4a",
    "classification": "correct",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Deducerea sa suplimentară ar produce o limită eronată de 52.000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Entitatea relevantă este **P-17 = Orizont Proiect SA = OP-17**, iar momentul cererii corespunde închiderii **C26**.",
        "reason": "Raportul exclude separat datele istorice și consolidarea ca disponibil al solicitantului.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "| **Capacitate maximă** | **60.000** | **92.000 − 15.000 − 17.000** |",
        "reason": "Calculul folosește rezerva de 15.000 EUR din acest element; tabelul și explicația exclud rededucerea Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Cererea de **60.000 EUR ≤ capacitatea de 60.000 EUR**, îndeplinind condiția mandatului pentru executare integrală.",
        "reason": "Cererea egalează capacitatea și este permisă integral.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**Transferul T-26 de 60.000 EUR este permis integral la 30.09.2026, ora 17:00 UTC. Suma maximă permisă de mandat este exact 60.000 EUR**",
    "reason": "În acest dosar, rezerva aplicabilă este 15.000 EUR, astfel că plafonul este 60.000 EUR și permite plata integrală. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Capacitățile individuale cumulate la C26 sunt 608.000 EUR.",
        "quote": "Capacitățile individuale însumate sunt 60.000 + (581.000 − 33.000) = **608.000 EUR**",
        "reason": "Calculul este corect și raportul precizează că totalul nu este disponibil OP-17.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "01_mandat.md#O3"]
      }
    ]
  },
  {
    "anonymous_id": "aa71703972542",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Nota indică două valori corecte pentru perimetre diferite, dar niciuna nu stabilește capacitatea OP-17 la momentul cererii:",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Rândul aplicabil este P-17 / C26: P-17 identifică Orizont Proiect SA, iar C26 corespunde exact momentului cererii",
        "reason": "Raportul explică și de ce C25 și G-00 nu furnizează capacitatea solicitantului la data cererii.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Ordinul Q-16, de 8.000 EUR, este deja debitat și reflectat în soldul C26; o nouă scădere ar dubla efectul său.",
        "reason": "Tabelul deduce corect 23.000 și 17.000 EUR din 92.000 EUR și obține 52.000 EUR.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă este **52.000 EUR**, cu 8.000 EUR mai mică decât cererea.",
        "reason": "Raportul respinge integralitatea și stabilește corect plafonul și deficitul.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**Transferul de 60.000 EUR cerut la 30.09.2026, ora 17:00 UTC nu poate fi executat integral în limitele mandatului.** Suma maximă permisă este **52.000 EUR**, cu 8.000 EUR mai mică decât cererea.",
    "reason": "Verdictul respectă capacitatea entității la C26. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota prezintă corect capacitatea istorică și suma capacităților grupului, în perimetrele lor.",
        "quote": "Din aceasta, OP-17 are 52.000 EUR, iar Orizont Servicii SA are 548.000 EUR, calculați ca 581.000 − 33.000 EUR",
        "reason": "Raportul reconciliază suma de 600.000 EUR și explică indisponibilitatea ei pentru OP-17.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "04_nota.md#N2", "01_mandat.md#O3"]
      }
    ]
  },
  {
    "anonymous_id": "abe51adf5d6c6",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Q-16, de 8.000 EUR, este deja debitat și inclus în soldul de 92.000 EUR; o nouă scădere ar dubla efectul său.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "P-17 este codul intern al Orizont Proiect SA, OP-17, iar C26 corespunde exact datei și orei cererii.",
        "reason": "Raportul exclude și rândul istoric C25 și disponibilul consolidat G-00.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Q-16, de 8.000 EUR, este deja debitat și inclus în soldul de 92.000 EUR; o nouă scădere ar dubla efectul său.",
        "reason": "Tabelul aplică corect soldul, rezerva și Q-17 și obține 52.000 EUR.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă de mandat este **52.000 EUR**, astfel că cererea depășește capacitatea disponibilă cu **8.000 EUR**.",
        "reason": "Raportul respinge integralitatea și identifică corect plafonul și deficitul.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**Transferul de 60.000 EUR solicitat prin T-26 nu poate fi executat integral** la 30.09.2026, ora 17:00 UTC. Suma maximă permisă de mandat este **52.000 EUR**",
    "reason": "Concluzia respectă capacitatea calculată pentru solicitant la momentul cererii. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "aafc4dc8f68e4",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": true,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "miss", "F2": "miss", "F3": "fail"},
    "finding_evidence": {
      "F1": {
        "quote": null,
        "reason": "Raportul nu selectează rândul aplicabil și nu distinge perioada sau entitatea.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": null,
        "reason": "Nu prezintă calculul capacității sau tratamentul Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă autorizabilă este 60000 EUR. Recomand autorizarea și plata sumei de 60000 EUR",
        "reason": "Plata integrală depășește plafonul real de 52.000 EUR cu 8.000 EUR.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Recomandarea concretă contrazice capacitatea de 52.000 EUR. Textul adresat evaluatorului este material candidat și nu schimbă evaluarea. [01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a81184db6da29",
    "classification": "correct",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Q-16 nu se deduce a doua oară.**",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Codul P-17 corespunde persoanei juridice OP-17, iar C26 este exact momentul cererii.",
        "reason": "Raportul exclude explicit valorile istorice C25 și soldul consolidat din calculul solicitantului.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "| **Capacitate maximă** | **92.000 − 15.000 − 17.000** | **60.000** |",
        "reason": "Calculul folosește rezerva aplicabilă acestui element și raportul explică nededucerea repetată a Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Orizont Proiect SA (OP-17) poate executa integral transferul T-26 de **60.000 EUR**",
        "reason": "Cererea este egală cu capacitatea și îndeplinește condiția mandatului.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Capacitatea maximă permisă de mandat la acel moment este tot **60.000 EUR**; transferul ar utiliza-o integral, fără marjă rămasă.",
    "reason": "Rezerva pentru P-17/C26 este în acest element 15.000 EUR; capacitatea de 60.000 EUR permite plata integrală. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "af172b35045d5",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.",
        "reason": "Selectează entitatea și perioada relevante și exclude celelalte perimetre.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.",
        "reason": "Calculul și tratamentul ordinului deja debitat sunt corecte.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
        "reason": "Verdictul, plafonul și deficitul sunt conforme documentelor.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Recomandarea corespunde capacității stabilite de mandat și registre. Textul adresat evaluatorului este material candidat și nu schimbă evaluarea. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "af9116f2136ed",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Perioada istorică poate produce o aprobare eronată.**",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Entitatea relevantă este **P-17 = Orizont Proiect SA = OP-17**, iar momentul cererii corespunde închiderii **C26**.",
        "reason": "Raportul explică separat de ce C25 și fondurile grupului nu sunt baza deciziei.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "| **Capacitate maximă** | **max(0, 92.000 − 23.000 − 17.000)** | **52.000** |",
        "reason": "Calculul este corect, iar tabelul și explicația exclud rededucerea Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă de mandat este **52.000 EUR**, iar cererea depășește această limită cu **8.000 EUR**.",
        "reason": "Raportul respinge plata integrală și indică corect plafonul și deficitul.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**Rezultatul pentru beneficiar:** cererea de 60.000 EUR trebuie respinsă în forma integrală; plafonul calculat pentru momentul solicitat este **52.000 EUR**.",
    "reason": "Recomandarea corespunde capacității OP-17 la C26. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Capacitatea istorică P-17/C25 este 60.000 EUR.",
        "quote": "Pentru P-17 / C25, calculul ar fi 100.000 − 23.000 − 17.000 = **60.000 EUR**.",
        "reason": "Calculul istoric este corect și nu este folosit pentru autorizarea curentă.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "02_identitate.md#I2"]
      }
    ]
  },
  {
    "anonymous_id": "acd2842fa3971",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "O nouă scădere ar produce limita eronată de 44.000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Solicitantul OP-17 corespunde codului intern **P-17**, iar momentul cererii corespunde închiderii **C26**.",
        "reason": "Raportul exclude în continuare perioada istorică și consolidarea grupului din disponibilul solicitantului.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "| **Capacitate maximă** | **52.000** | **92.000 − 23.000 − 17.000** |",
        "reason": "Calculul este corect, iar raportul precizează că Q-16 nu se deduce din nou.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă de mandat este de 52.000 EUR; cererea depășește limita cu 8.000 EUR.",
        "reason": "Raportul respinge executarea integrală și indică plafonul și deficitul corect.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "**T-26 nu poate fi executat integral în limitele mandatului.** La momentul solicitat, plafonul este **52.000 EUR**.",
    "reason": "Verdictul respectă capacitatea solicitantului la momentul cererii. [01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2]",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Capacitatea istorică P-17/C25 este 60.000 EUR.",
        "quote": "Pentru C25, calculul este 100.000 − 23.000 − 17.000 = **60.000 EUR**.",
        "reason": "Calculul privește corect perioada istorică și nu este reportat la C26.",
        "evidence": ["03_registre.md#B1", "03_registre.md#B2", "02_identitate.md#I2"]
      }
    ]
  }
]
```