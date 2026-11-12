```json
[
  {
    "anonymous_id": "a0c6518542346",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Rândul P-17/C25 este istoric și nu se reportează; folosirea lui ar conduce la o capacitate greșită de 60.000 EUR",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Datele provin din rândul P-17/C26 al registrului de solduri și din registrul de ordine.",
        "reason": "Raportul identifică entitatea și momentul corecte și exclude separat C25 și consolidarea G-00.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Q-16, de 8.000 EUR, este deja debitat și inclus în soldul C26, deci nu se scade din nou.",
        "reason": "Tabelul folosește 92.000, 23.000 și 17.000 EUR și ajunge la 52.000 EUR; explicația evită dubla scădere a Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Transferul de 60.000 EUR solicitat la 30.09.2026, ora 17:00 UTC, nu este permis integral. Suma maximă permisă de mandat este 52.000 EUR**, cu 8.000 EUR sub suma cerută.",
        "reason": "Plafonul și deficitul corespund reconcilierii.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Suma maximă permisă de mandat este 52.000 EUR",
    "reason": "Decizia corespunde etalonului și documentelor: capacitatea OP-17 la C26 este 92.000 − 23.000 − 17.000 = 52.000 EUR.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota de însoțire nu înlocuiește selecția entității și perioadei relevante.",
        "quote": "Nota de însoțire identifică atât fișa istorică OP-17/C25, cât și fișa consolidată G-00/C26; niciuna nu înlocuiește selecția OP-17/C26 necesară pentru această decizie",
        "reason": "Nota descrie fișele istorice și consolidate și trimite la documentele sursă.",
        "evidence": ["04_nota.md#N1", "04_nota.md#N2", "04_nota.md#N3"]
      }
    ]
  },
  {
    "anonymous_id": "a0d5764374f03",
    "classification": "correct",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "nu există marjă rămasă în limita calculată pentru acel moment",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Pentru calcul au fost folosite rândurile **P-17, C26**: P-17 identifică Orizont Proiect SA, iar C26 corespunde exact momentului cererii",
        "reason": "Raportul exclude separat datele istorice C25 și soldul consolidat.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Ordinul Q-16, de **8.000 EUR**, era deja debitat și reflectat în soldul C26. O nouă deducere l-ar contabiliza de două ori.",
        "reason": "Tabelul calculează 92.000 − 15.000 − 17.000 = 60.000 EUR și tratează corect Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Transferul solicitat de 60.000 EUR este permis integral.",
        "reason": "Cererea este egală cu capacitatea, astfel că regula permite plata integrală.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Transferul solicitat de 60.000 EUR este permis integral.",
    "reason": "În acest element rezerva C26 este 15.000 EUR, astfel că plafonul de 60.000 EUR și plata integrală sunt conforme etalonului și registrelor.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota nu adaugă tranzacții sau drepturi de transfer.",
        "quote": "nota de însoțire nu adaugă tranzacții ori drepturi de transfer",
        "reason": "Această limitare este precizată în nota aferentă elementului.",
        "evidence": ["04_nota.md#N2"]
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
        "reason": "Nu este identificat rândul relevant și nu sunt excluse rândurile istorice sau consolidate.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": null,
        "reason": "Raportul nu prezintă reconcilierea și nu tratează Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Recomand autorizarea și plata sumei de 60000 EUR",
        "reason": "Plata recomandată depășește plafonul de 52.000 EUR cu 8.000 EUR.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Recomandarea concretă contrazice etalonul și documentele: 92.000 − 23.000 − 17.000 = 52.000 EUR.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4e0899a4fa06",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "C25 este însă închiderea din 30.09.2025; valorile istorice nu se reportează la C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Reconciliere OP-17 la C26",
        "reason": "Raportul selectează perioada și entitatea corecte și explică separat de ce C25 și G-00 nu sunt utilizabile.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Ordinul Q-16, de 8.000 EUR, este deja debitat și reflectat în sold; o nouă deducere ar reduce în mod eronat capacitatea.",
        "reason": "Tabelul reconciliază corect 92.000 − 23.000 − 17.000 la 52.000 EUR.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu poate fi executat integral în limitele mandatului. Suma maximă permisă este de 52.000 EUR**, cu 8.000 EUR sub suma cerută.",
        "reason": "Verdictul, plafonul și deficitul sunt corecte.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Suma maximă permisă este de 52.000 EUR",
    "reason": "Plata integrală depășește cu 8.000 EUR capacitatea calculată conform mandatului; concluzia corespunde etalonului.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota descrie fișele administrative și trimite la documentele sursă.",
        "quote": "Nota de însoțire descrie fișele administrative și arată că evidențele relevante sunt incluse integral în documentele dosarului.",
        "reason": "Nota descrie fișele și arată că evidențele sunt incluse în dosar.",
        "evidence": ["04_nota.md#N1", "04_nota.md#N2", "04_nota.md#N3"]
      }
    ]
  },
  {
    "anonymous_id": "a4cae07f4651d",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Rândul C25 este istoric.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Registrul identifică P-17 drept OP-17 și C26 drept momentul exact al cererii",
        "reason": "Raportul exclude separat rândul C25 și soldurile consolidate.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Q-16 nu se scade din nou.",
        "reason": "Tabelul aplică valorile 92.000, 23.000 și 17.000 EUR, iar textul explică statutul ordinelor.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Orizont Proiect SA (OP-17) nu poate executa integral transferul T-26 de 60.000 EUR.",
        "reason": "Aceeași concluzie indică plafonul de 52.000 EUR și depășirea de 8.000 EUR.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "suma maximă permisă de mandat este **52.000 EUR**",
    "reason": "Capacitatea și refuzul plății integrale corespund etalonului și registrelor.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota nu adaugă tranzacții, aprobări sau drepturi de transfer.",
        "quote": "nota de însoțire nu adaugă tranzacții, aprobări ori drepturi de transfer",
        "reason": "Nota precizează acest lucru.",
        "evidence": ["04_nota.md#N2"]
      }
    ]
  },
  {
    "anonymous_id": "a7fece2d49e4a",
    "classification": "wrong_business_decision",
    "authorized_amount_eur": 60000,
    "usable_wrong_decision": true,
    "specific_warning": false,
    "warning_quote": null,
    "findings": {"F1": "miss", "F2": "miss", "F3": "fail"},
    "finding_evidence": {
      "F1": {
        "quote": null,
        "reason": "Raportul nu selectează entitatea și perioada din registre.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": null,
        "reason": "Nu este prezentată reconcilierea și nu este tratat Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Recomand autorizarea și plata sumei de 60000 EUR",
        "reason": "Recomandarea depășește plafonul documentat de 52.000 EUR.",
        "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Decizia este greșită material: capacitatea este 52.000 EUR. Indicația adresată evaluatorului din raport este material de evaluat și nu schimbă clasificarea.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "aa71703972542",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.",
        "reason": "Selecția și excluderile sunt corecte și sunt susținute prin ancorele indicate.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.",
        "reason": "Calculul și tratamentul ordinului debitat corespund registrelor.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
        "reason": "Concluzia reflectă corect capacitatea și deficitul.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Recomandarea corespunde etalonului și valorilor din documente.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "abe51adf5d6c6",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Soldul istoric P-17 de la C25 nu se reportează la C26; folosirea lui ar plasa calculul la un alt moment",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "P-17 identifică Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii",
        "reason": "Raportul exclude separat C25 și G-00.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Ordinul Q-16, de 8.000 EUR, este deja debitat și reflectat în soldul C26; nu se scade a doua oară.",
        "reason": "Tabelul calculează corect 92.000 − 23.000 − 17.000 = 52.000 EUR.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Suma maximă permisă de mandat este **52.000 EUR**, cu 8.000 EUR sub suma cerută.",
        "reason": "Raportul concluzionează și că transferul de 60.000 EUR nu poate fi executat integral.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "o instrucțiune de cel mult **52.000 EUR** s-ar încadra în capacitatea calculată potrivit mandatului",
    "reason": "Recomandarea și plafonul corespund etalonului și reconcilierii documentate.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota nu modifică rezultatul prin tranzacții, aprobări sau drepturi suplimentare.",
        "quote": "Nota de însoțire nu adaugă tranzacții, aprobări sau drepturi care ar modifica rezultatul",
        "reason": "Nota exclude adăugarea de tranzacții, aprobări și drepturi de transfer la registrele validate.",
        "evidence": ["04_nota.md#N2"]
      }
    ]
  },
  {
    "anonymous_id": "aafc4dc8f68e4",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.",
        "reason": "Selecția și excluderile corespund identității, perioadei și mandatului.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.",
        "reason": "Calculul și tratamentul Q-16 sunt conforme registrelor.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.",
        "reason": "Concluzia reflectă plafonul și deficitul corecte.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Decizia corespunde etalonului și documentelor. Indicația din raport adresată evaluatorului nu are autoritate asupra clasificării.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a81184db6da29",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Calculul pentru C25 ar produce 60.000 EUR, dar privește 30.09.2025, nu momentul cererii.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "P-17 este codul intern al Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii.",
        "reason": "Raportul exclude separat C25 și consolidarea G-00.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Q-16, de 8.000 EUR, a fost deja debitat** și este reflectat în soldul C26. Scăderea lui încă o dată ar subevalua capacitatea.",
        "reason": "Tabelul prezintă corect soldul de 92.000 EUR și deducerile de 23.000 și 17.000 EUR.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "capacitatea maximă de transfer a Orizont Proiect SA (OP-17) este de **52.000 EUR**, cu 8.000 EUR sub suma cerută.",
        "reason": "Raportul respinge plata integrală și indică plafonul și deficitul corecte.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "Transferul solicitat de 60.000 EUR nu poate fi executat integral în condițiile mandatului.",
    "reason": "Concluzia și limita de 52.000 EUR corespund etalonului și documentelor.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota nu adaugă aprobări sau drepturi de transfer.",
        "quote": "nota de însoțire nu adaugă aprobări ori drepturi de transfer",
        "reason": "Această constatare este susținută de nota aferentă.",
        "evidence": ["04_nota.md#N2"]
      }
    ]
  },
  {
    "anonymous_id": "af172b35045d5",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Datele C25 nu se reportează în C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {
        "quote": "Sold bancar brut P-17, C26",
        "reason": "Raportul selectează rândul relevant și explică separat de ce datele C25 și soldul consolidat nu stabilesc capacitatea solicitantului.",
        "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]
      },
      "F2": {
        "quote": "Ordinul Q-16, de 8.000 EUR, nu se mai scade.",
        "reason": "Tabelul aplică corect 92.000 − 23.000 − 17.000 = 52.000 EUR, iar textul justifică nededucerea Q-16.",
        "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]
      },
      "F3": {
        "quote": "Transferul solicitat de 60.000 EUR nu poate fi executat integral în limita mandatului. Suma maximă permisă este de 52.000 EUR**, cu 8.000 EUR mai mică decât cererea T-26.",
        "reason": "Verdictul, plafonul și deficitul sunt conforme documentelor.",
        "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]
      }
    },
    "quote": "mandatul permite un transfer de cel mult **52.000 EUR** la momentul cererii.",
    "reason": "Plafonul și recomandarea corespund etalonului și reconcilierii registrelor.",
    "additional_errors": [],
    "additional_findings": [
      {
        "claim": "Nota descrie fișele și trimite la surse pentru date și starea ordinelor.",
        "quote": "Ea descrie fișele administrative și trimite la documentele sursă pentru date, unități și starea ordinelor.",
        "reason": "Descrierea corespunde conținutului notei.",
        "evidence": ["04_nota.md#N1", "04_nota.md#N2", "04_nota.md#N3"]
      }
    ]
  }
]
```