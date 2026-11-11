## Concluzie

La **05.09.2026**, conform regulilor operaționale din dosar, **L-09 nu a fost livrat către depozitul Lumen**. **Nu se poate certifica**: protocolul cere o înregistrare `GATE-ACCEPT` pentru cheia exactă `L-09`, iar registrul complet nu conține una.

Această concluzie privește livrarea **către depozitul Lumen**, în sensul definit de protocol. Dosarul nu permite concluzii mai largi despre locul în care se afla lotul ori despre alte evenimente din afara acestui sens.

## Probe și deducții

- **[02_protocol.md — R1]** Livrarea are loc dacă și numai dacă există o înregistrare `GATE-ACCEPT` pentru lot; toate recepțiile trec prin poartă, fără excepții offline în intervalul acoperit.  
  **Deducție:** în cadrul protocolului, recepția este definită prin registrul porții, nu prin declarații verbale.

- **[03_poarta.md — G1]** Manifestul acoperă poarta Lumen între 01.09.2026T00:00Z și 05.09.2026T23:59:59Z, este marcat `integral=1`, indică zero transporturi offline și are semnătură validă.  
  **Deducție:** intervalul relevant are acoperire completă, potrivit dosarului.

- **[03_poarta.md — G2]** Lista integrală conține `GATE-ACCEPT` pentru L-90, L-19 și L-91, dar nu pentru L-09.  
  **Deducție:** în intervalul acoperit nu există eveniment de recepție pentru cheia exactă L-09.

- **[02_protocol.md — R2]** Pentru intervalele `integral=1`, absența unui eveniment implică absența recepției în sensul R1; certificarea cere `GATE-ACCEPT` pentru cheia exactă a lotului.  
  **Deducție:** L-09 nu este livrat în sensul operațional al dosarului și nu îndeplinește condiția de certificare.

- **[01_inventar.md — D2]** L-09 este indicat ca expediat la 01.09; L-90 apare ca livrat la 02.09 și semnat „Radu Pop”, iar responsabilul L-09 este „Radu Popp”.  
  **Deducție:** expedierea nu dovedește recepția. În plus, diferența L-09/L-90 și variația Pop/Popp pot induce o asociere greșită între loturi ori persoane. Înregistrarea pentru L-90 nu poate ține locul unei înregistrări pentru L-09.

## Nota de incertitudine și problema materială

- **[01_inventar.md — D1]** Arhiva curierului pentru 01–04.09 lipsește, confirmarea curierului pentru L-09 nu este în export, iar inventarul general este marcat incomplet.
- **[01_inventar.md — D3]** Nota analistului spune că nu se poate afirma nici livrarea, nici nelivrarea, deoarece dosarul este incomplet; nota declară că s-a bazat exclusiv pe D1.

Nota este **prudentă dacă se referă doar la inventarul și arhiva curierului**, dar este **incompletă și înșelătoare ca verdict operațional**: ignoră protocolul semnat și registrul porții, care acoperă integral intervalul relevant și exclude transporturile offline. În ansamblul dosarului, lipsa confirmării curierului nu anulează efectul registrului complet potrivit R1–R2 și G1–G2.

## Fapte certe și necunoscute

**Stabilite de documentele dosarului:** L-09 a fost expediat, dar nu apare cu `GATE-ACCEPT` în intervalul complet; livrarea către depozitul Lumen nu este demonstrată și, conform protocolului, nu a avut loc; certificarea nu este posibilă pe baza acestor înregistrări.

**Rămân necunoscute:** dacă L-09 a ajuns în alt loc sau ce s-a întâmplat cu el după expediere; dosarul nu conține arhiva curierului și nu oferă o confirmare a curierului. Aceste necunoscute nu schimbă concluzia privind recepția la depozit în sensul definit de protocol.

## Aspecte corecte și surse de confuzie

- **[01_inventar.md — D1]** marchează inventarul ca incomplet și semnalează lipsa confirmării curierului: acestea sunt limite reale ale exportului.
- **[02_protocol.md — R3]** consemnează declarații contradictorii, fără `GATE-ACCEPT`. Conform R1, declarațiile nu înlocuiesc registrul.
- **[03_poarta.md — G1, G2]** oferă acoperirea și lista evenimentelor necesare pentru concluzia operațională.
- **[03_poarta.md — registrul LG-001–LG-056]** conține multe rânduri de permanență/integritate, dar niciunul nu este o înregistrare `GATE-ACCEPT` pentru L-09; prezența lor nu modifică rezultatul.
- **[01_inventar.md — D2]** asemănarea numerelor L-09 și L-90, precum și diferența dintre „Radu Pop” și „Radu Popp”, creează risc de confuzie, nu probă de livrare pentru L-09.

**Rezumat:** la 05.09.2026, dosarul susține concluzia că L-09 **nu a fost livrat la depozitul Lumen** în sensul protocolului și **nu poate fi certificat**. Nota de incertitudine surprinde incompletitudinea inventarului, dar nu integrează registrul complet al porții, care permite o concluzie operațională mai fermă.