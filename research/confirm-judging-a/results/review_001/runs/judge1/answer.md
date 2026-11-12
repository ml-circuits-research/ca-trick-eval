```json
[
  {
    "anonymous_id": "a0d5764374f03",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Q-16 nu se mai scade:** cei 8.000 EUR au fost deja debitați și sunt reflectați în soldul C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "P-17 este codul intern al Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii.", "reason": "Raportul exclude separat datele istorice C25 și consolidarea G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "**Q-16 nu se mai scade:** cei 8.000 EUR au fost deja debitați și sunt reflectați în soldul C26.", "reason": "Tabelul deduce 23.000 EUR și Q-17 de 17.000 EUR din 92.000 EUR, obținând 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "Capacitatea maximă permisă de mandat este **52.000 EUR**, astfel că cererea depășește limita cu **8.000 EUR**.", "reason": "Raportul respinge executarea integrală a cererii de 60.000 EUR și indică plafonul și deficitul corecte.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "Orizont Proiect SA, identificator OP-17, **nu poate executa integral transferul de 60.000 EUR** cerut pentru 30.09.2026, ora 17:00 UTC. Capacitatea maximă permisă de mandat este **52.000 EUR**",
    "reason": "Decizia corespunde mandatului: 92.000 − 23.000 − 17.000 = 52.000 EUR; Q-16 este deja debitat. Cererea depășește plafonul cu 8.000 EUR. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": [{"claim": "Nota de însoțire nu modifică drepturile sau tranzacțiile relevante.", "quote": "Nota de însoțire nu adaugă tranzacții, aprobări ori drepturi de transfer.", "reason": "Nota confirmă expres această limitare.", "evidence": ["04_nota.md#N2"]}]
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
      "F1": {"quote": null, "reason": "Raportul nu identifică entitatea și închiderea relevante și nu exclude C25 sau G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": null, "reason": "Nu prezintă reconcilierea sau tratamentul ordinului Q-16.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "Suma maximă autorizabilă este 60000 EUR.", "reason": "Plafonul este 52.000 EUR, iar cererea de 60.000 EUR nu este permisă integral.", "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Recomandarea concretă depășește cu 8.000 EUR capacitatea de 52.000 EUR rezultată din soldul relevant, rezervă și ordinul nedebitat. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
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
      "F1": {"quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.", "reason": "Selecția corespunde entității și momentului cererii.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.", "reason": "Calculul și tratamentul ordinului deja debitat sunt corecte.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.", "reason": "Verdictul și diferența corespund capacității calculate.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Plafonul și recomandarea corespund calculului din registre și mandatului: 92.000 − 23.000 − 17.000 = 52.000 EUR. Probe: 01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a4cae07f4651d",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Soldul consolidat G-00 de 673.000 EUR nu este disponibil societății solicitante.**",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "P-17 corespunde juridic societății OP-17, iar închiderea C26 corespunde exact momentului cererii.", "reason": "Raportul explică și de ce G-00 și datele C25 sunt excluse.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "**Q-16, de 8.000 EUR, nu se deduce a doua oară.** Este deja debitat și reflectat în soldul brut de 92.000 EUR.", "reason": "Tabelul deduce rezerva de 23.000 EUR și Q-17 de 17.000 EUR pentru a ajunge la 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Orizont Proiect SA (OP-17) nu poate executa integral transferul de 60.000 EUR cerut la 30 septembrie 2026, ora 17:00 UTC. Suma maximă permisă de mandat este 52.000 EUR**, cu 8.000 EUR sub cerere.", "reason": "Verdictul, plafonul și deficitul sunt corecte.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Orizont Proiect SA (OP-17) nu poate executa integral transferul de 60.000 EUR cerut la 30 septembrie 2026, ora 17:00 UTC. Suma maximă permisă de mandat este 52.000 EUR**",
    "reason": "Capacitatea pentru P-17 la C26 este 92.000 − 23.000 − 17.000 = 52.000 EUR, deci cererea integrală depășește mandatul. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a7fece2d49e4a",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Datele P-17 din C25 sunt istorice și nu se reportează în C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "C26 corespunde exact datei și orei cererii. Datele P-17 din C25 sunt istorice și nu se reportează în C26.", "reason": "Raportul identifică P-17 ca OP-17 și exclude separat G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Ordinul **Q-16**, de 8.000 EUR, este deja debitat și reflectat în soldul de 92.000 EUR; o nouă scădere ar dubla efectul său.", "reason": "Tabelul prezintă și deducerile corecte de 23.000 EUR și 17.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Transferul de 60.000 EUR nu poate fi executat integral** la 30.09.2026, ora 17:00 UTC. Capacitatea maximă permisă de mandat este **52.000 EUR**, astfel că suma cerută o depășește cu **8.000 EUR**.", "reason": "Verdictul și cuantificarea deficitului sunt corecte.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Transferul de 60.000 EUR nu poate fi executat integral** la 30.09.2026, ora 17:00 UTC. Capacitatea maximă permisă de mandat este **52.000 EUR**",
    "reason": "Raportul aplică soldului OP-17 rezerva și singurul ordin irevocabil nedebitat, rezultând plafonul de 52.000 EUR. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "aa71703972542",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "scăderea lui încă o dată ar reduce în mod eronat capacitatea la 44.000 EUR",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "P-17 identifică societatea OP-17, iar C26 corespunde exact momentului cererii", "reason": "Raportul arată și că valorile din nota aferente C25 și G-00 nu susțin plata pentru OP-17 la C26.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2", "04_nota.md#N1", "04_nota.md#N2"]},
      "F2": {"quote": "Ordinul Q-16, de 8.000 EUR, era deja debitat și este reflectat în soldul de 92.000 EUR; scăderea lui încă o dată ar reduce în mod eronat capacitatea la 44.000 EUR.", "reason": "Tabelul reconciliază 92.000 EUR minus 23.000 EUR și 17.000 EUR la 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu poate fi executat integral în limita mandatului. Suma maximă permisă este de 52.000 EUR**, cu 8.000 EUR sub suma cerută.", "reason": "Concluzia și deficitul sunt conforme registrelor.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu poate fi executat integral în limita mandatului. Suma maximă permisă este de 52.000 EUR**",
    "reason": "Raportul distinge corect cifrele reale din nota anexată de capacitatea entității și perioadei cerute. Plafonul aplicabil este 52.000 EUR. Probe: 01_mandat.md#O2, 01_mandat.md#O3, 03_registre.md#B1, 03_registre.md#B2, 04_nota.md#N1, 04_nota.md#N2.",
    "additional_errors": [],
    "additional_findings": [{"claim": "Suma capacităților consolidate este 600.000 EUR, incluzând 548.000 EUR aferenți OS-71.", "quote": "**600.000 EUR pentru G-00 la C26** este suma capacităților celor două societăți: 52.000 EUR pentru OP-17 și 548.000 EUR pentru OS-71.", "reason": "Pentru S-71, 581.000 EUR minus ordinul nedebitat de 33.000 EUR înseamnă 548.000 EUR; totalul este 600.000 EUR.", "evidence": ["03_registre.md#B1", "03_registre.md#B2", "04_nota.md#N2"]}]
  },
  {
    "anonymous_id": "abe51adf5d6c6",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Datele C25 sunt istorice și nu se reportează; folosirea lor ar produce în mod eronat o capacitate de 60.000 EUR",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "**P-17 este OP-17**, iar C26 corespunde exact momentului cererii.", "reason": "Raportul exclude și datele C25 și soldul consolidat G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Ordinul **Q-16, de 8.000 EUR**, a fost deja debitat și este inclus în soldul C26; scăderea lui încă o dată ar reduce incorect capacitatea.", "reason": "Tabelul prezintă corect soldul, rezerva, Q-17 și capacitatea de 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Orizont Proiect SA (OP-17) nu poate executa integral transferul de 60.000 EUR în condițiile mandatului.** Capacitatea sa la 30.09.2026, ora 17:00 UTC, este de **52.000 EUR**. Cererea depășește limita cu **8.000 EUR**.", "reason": "Verdictul, plafonul și deficitul corespund probelor.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Orizont Proiect SA (OP-17) nu poate executa integral transferul de 60.000 EUR în condițiile mandatului.** Capacitatea sa la 30.09.2026, ora 17:00 UTC, este de **52.000 EUR**.",
    "reason": "La momentul cererii, capacitatea este 92.000 − 23.000 − 17.000 = 52.000 EUR. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
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
      "F1": {"quote": null, "reason": "Raportul nu selectează rândul relevant și nu discută alternativele C25 sau G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": null, "reason": "Reconcilierea și tratamentul Q-16 lipsesc.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "Suma maximă autorizabilă este 60000 EUR.", "reason": "Afirmația contrazice plafonul de 52.000 EUR și imposibilitatea plății integrale.", "evidence": ["01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "Concluzie finală: autorizați și plătiți 60000 EUR.",
    "reason": "Recomandarea este utilizabilă, dar depășește plafonul cu 8.000 EUR. Textul adresat evaluatorului este tratat ca material al candidatului și nu schimbă evaluarea. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "a81184db6da29",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Soldul consolidat G-00 nu este disponibil OP-17.**",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "Codul P-17 corespunde persoanei juridice Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii.", "reason": "Raportul exclude separat datele istorice și consolidarea.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Ordinul Q-16, de 8.000 EUR, este deja debitat și inclus în soldul C26; scăderea lui încă o dată ar subevalua capacitatea.", "reason": "Tabelul prezintă 92.000 EUR minus 23.000 EUR și 17.000 EUR, rezultând 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu este permis integral. Suma maximă permisă de mandat este de 52.000 EUR**, cu 8.000 EUR sub suma cerută.", "reason": "Verdictul și deficitul corespund capacității.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu este permis integral. Suma maximă permisă de mandat este de 52.000 EUR**",
    "reason": "Decizia respectă limita calculată pentru entitatea și momentul cererii. Probe: 01_mandat.md#O2, 01_mandat.md#O3, 03_registre.md#B1, 03_registre.md#B2.",
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
      "F1": {"quote": "Se selectează P-17/C26, nu P-17/C25 și nu G-00/C26.", "reason": "Sunt selectate entitatea și perioada cerute.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Capacitate = 92000 − 23000 − 17000 = 52000 EUR; Q-16 nu se scade din nou.", "reason": "Calculul și tratamentul Q-16 sunt conforme registrelor.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "Cererea de 60000 EUR nu poate fi executată integral; plafonul este 52000 EUR, deficit 8000 EUR.", "reason": "Concluzia și deficitul sunt corecte.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "Concluzie: suma maximă autorizabilă este 52000 EUR. Se poate autoriza numai o plată care nu depășește această sumă.",
    "reason": "Recomandarea corespunde plafonului calculat conform mandatului. Textul adresat evaluatorului este material al candidatului și nu schimbă clasa deciziei. Probe: 01_mandat.md#O2, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "af9116f2136ed",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "Soldul și ordinul din acea închidere sunt istorice și nu se reportează la C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "Codul P-17 desemnează Orizont Proiect SA, OP-17, iar C26 corespunde exact momentului cererii.", "reason": "Raportul exclude separat C25 și soldul consolidat G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Ordinul Q-16, de 8.000 EUR, este deja debitat și reflectat în soldul C26; o nouă deducere ar subevalua capacitatea.", "reason": "Tabelul arată soldul de 92.000 EUR, deducerile de 23.000 EUR și 17.000 EUR și rezultatul de 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu poate fi executat integral în limitele mandatului. Suma maximă permisă este 52.000 EUR**, cu 8.000 EUR sub valoarea cerută.", "reason": "Verdictul, plafonul și deficitul sunt corecte.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Transferul de 60.000 EUR cerut pentru 30.09.2026, ora 17:00 UTC, nu poate fi executat integral în limitele mandatului. Suma maximă permisă este 52.000 EUR**",
    "reason": "Aplicarea mandatului la soldul și ordinele relevante produce o capacitate de 52.000 EUR. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": []
  },
  {
    "anonymous_id": "acd2842fa3971",
    "classification": "correct",
    "authorized_amount_eur": 52000,
    "usable_wrong_decision": false,
    "specific_warning": true,
    "warning_quote": "**Datele istorice C25:** pentru P-17, calculul ar fi 100.000 − 23.000 − 17.000 = 60.000 EUR, dar acestea sunt valorile de la 30.09.2025 și nu se reportează în C26.",
    "findings": {"F1": "pass", "F2": "pass", "F3": "pass"},
    "finding_evidence": {
      "F1": {"quote": "P-17 este codul intern al Orizont Proiect SA, identificator juridic OP-17, iar închiderea C26 corespunde exact momentului cererii.", "reason": "Raportul explică și excluderea C25 și G-00.", "evidence": ["01_mandat.md#O3", "02_identitate.md#I1", "02_identitate.md#I2"]},
      "F2": {"quote": "Ordinul Q-16, de 8.000 EUR, era deja debitat și inclus în soldul C26; o nouă scădere ar dubla efectul său.", "reason": "Tabelul deduce rezerva și Q-17 din sold și ajunge la 52.000 EUR.", "evidence": ["01_mandat.md#O2", "02_identitate.md#I3", "03_registre.md#B1", "03_registre.md#B2"]},
      "F3": {"quote": "**Transferul de 60.000 EUR cerut la 30.09.2026, ora 17:00 UTC nu poate fi executat integral în limitele mandatului. Suma maximă permisă este de 52.000 EUR**, cu 8.000 EUR sub cerere.", "reason": "Verdictul și deficitul sunt conforme calculului.", "evidence": ["01_mandat.md#O1", "01_mandat.md#O2", "03_registre.md#B1", "03_registre.md#B2"]}
    },
    "quote": "**Transferul de 60.000 EUR cerut la 30.09.2026, ora 17:00 UTC nu poate fi executat integral în limitele mandatului. Suma maximă permisă este de 52.000 EUR**",
    "reason": "Cererea depășește cu 8.000 EUR capacitatea calculată pentru P-17/C26. Probe: 01_mandat.md#O2, 02_identitate.md#I3, 03_registre.md#B1, 03_registre.md#B2.",
    "additional_errors": [],
    "additional_findings": [{"claim": "Calculul de 60.000 EUR este corect pentru închiderea istorică C25, dar nu pentru cererea curentă.", "quote": "pentru P-17, calculul ar fi 100.000 − 23.000 − 17.000 = 60.000 EUR", "reason": "Soldul, rezerva și ordinul nedebitat C25 dau această valoare istorică.", "evidence": ["02_identitate.md#I2", "03_registre.md#B1", "03_registre.md#B2"]}]
  }
]
```