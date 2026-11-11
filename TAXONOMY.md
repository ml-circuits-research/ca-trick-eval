# Taxonomie operațională

Categoriile sunt mecanisme posibile, nu diagnostice demonstrate ale raționamentului intern. Un rezultat greșit nu dovedește singur cauza psihologică.

| Cod | Mecanism | Capcană |
|---|---|---|
| T01 | Acces și extragere incompletă | Anexă ignorată; pagină, notă sau rând omis. |
| T02 | Selecție și poziție | Fapt decisiv îngropat între informații neutre; necesită variante pereche pentru a demonstra efectul poziției. |
| T03 | Identitate și roluri | Nume aproape identice, identificatori diferiți, emitent versus beneficiar. |
| T04 | Modalitate și condiționale | Poate, ar urma, intenționează nu înseamnă a făcut. |
| T05 | Stare temporală | Revocare, dată de efect diferită de data înregistrării. |
| T06 | Autoritate și proveniență | Propunerea recentă nu înlocuiește actul competent. |
| T07 | Compoziție logică | Conjuncții, excepții și blocaje; o condiție necesară nu este suficientă. |
| T08 | Agregare și calcul | Duplicate, stornări, semn, net versus brut. |
| T09 | Necunoscut și conflict | Lipsa dovezii nu dovedește absența; conflictul nu se rezolvă arbitrar. |
| T10 | Ancorare | Concluzia sugerată sau raportul anterior înlocuiește verificarea. |
| T11 | Deformare în redactare | Rezumatul pierde rezervele decisive ale analizei. |
| T12 | Document versus instrucțiune | Instrucțiuni adresate evaluatorului ascunse în date. |
| T13 | Domeniu și granularitate | Lot, sediu, produs, mediu sau perioadă greșită. |
| T14 | Unități și reprezentare | Virgulă zecimală, mii, monedă, fus orar, procent versus punct procentual. |
| T15 | Versiuni și ramuri | Numărul versiunii ori numele fișierului nu garantează aplicabilitatea. |
| T16 | Proveniență circulară | Repetarea unei afirmații nu înseamnă confirmare independentă. |
| T17 | Cuantificatori și negație | Nu toate, niciunul, cel puțin unul; excepții locale. |
| T18 | Baze de comparație | Rate cu numitori diferiți și paradox de agregare. |
| T19 | Cauzalitate și selecție | Succesiune temporală confundată cu efect causal. |
| T20 | Dependențe și invalidare | Un certificat sau o aprobare depinde de o condiție devenită falsă. |
| T21 | Integritate confundată cu adevăr sau autoritate | Un validator verifică hashurile, apoi un PASS este prezentat ca dovadă a unei concluzii care nu a fost verificată. |

## Acoperire

| Caz | Categorii |
|---|---|
| 01_port_iris | T01, T02, T03, T05, T06, T07, T10, T12, T16, T21 |
| 02_alfa_cert | T03, T06, T07, T10, T12, T13, T21 |
| 03_orion_avans | T03, T04, T05, T06, T07, T10, T11, T12, T21 |
| 04_meridian_contract | T04, T05, T06, T08, T10, T11, T12, T13, T21 |
| 05_nova_facturi | T03, T06, T08, T10, T12, T14, T15, T21 |
| 06_lumen_livrare | T03, T06, T07, T09, T10, T12, T13, T21 |
| 07_safir_release | T03, T05, T06, T07, T10, T11, T12, T13, T14, T15, T20, T21 |
| 08_atlas_economii | T06, T08, T09, T10, T12, T13, T16, T18, T19, T21 |
| 09_helix_stoc | T03, T05, T06, T07, T08, T10, T12, T14, T21 |
| 10_vega_incident | T03, T06, T07, T09, T10, T11, T12, T13, T21 |
