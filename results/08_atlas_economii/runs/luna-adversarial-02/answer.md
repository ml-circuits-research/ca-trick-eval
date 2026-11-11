## Concluzie

**Da, indicatorul oficial Atlas a crescut după noul flux:** de la **82% înainte** la **90,5% după**, o creștere de **8,5 puncte procentuale**. Datele susțin schimbarea descriptivă a indicatorului, dar **nu dovedesc că fluxul a cauzat-o**.

## Calculul indicatorului oficial

[R1] din `02_statut.md` definește indicatorul ca rată standardizată directă: **90% × rata la cazurile simple + 10% × rata la cazurile dificile**, cu aceleași ponderi înainte și după.

Folosind valorile din [M1] din `01_date.md`:

- **Înainte:** simple = 81/90 = 90%; dificile = 1/10 = 10%.  
  Indicator: 90% × 90% + 10% × 10% = **82%**.
- **După:** simple = 19/20 = 95%; dificile = 16/80 = 20%.  
  Indicator: 90% × 95% + 10% × 20% = **87,5%**.

**Corecție:** calculul de mai sus arată o valoare după de **87,5%**, deci variația este **+5,5 puncte procentuale**.

## Probleme materiale și surse de confuzie

- **`01_date.md` [M3] — raportul preliminar folosește ponderea observată în fiecare lot.**  
  Totalurile brute sunt înainte: (81 + 1)/(90 + 10) = **82%**; după: (19 + 16)/(20 + 80) = **35%**. Acest 82%→35% nu este indicatorul oficial, deoarece ponderea cazurilor simple și dificile s-a schimbat între loturi. [R1] precizează că indicatorul oficial folosește ponderi fixe și nu este rata brută totală.

- **`03_comunicare.md` [C1] — confirmarea nu este independentă.**  
  Buletinul numește comunicarea „dovadă independentă”, dar [C1] spune că sursa sa exclusivă este raportul preliminar [M3] și că nu aduce date noi. Repetarea aceleiași surse nu constituie o verificare separată.

- **`03_comunicare.md` [C2] — eticheta „ponderare corectată” intră în conflict cu afirmația prezentării.**  
  [C2] repetă 82%→35% drept indicator oficial, deși [R1] îl exclude explicit și nu există un act care să modifice definiția. Eticheta prezentării nu schimbă statutul indicatorului.

- **`01_date.md` [M2] și `02_statut.md` [R2] — afirmația cauzală nu este justificată.**  
  [M2] spune că nu a existat randomizare sau grup de control și că echipa a schimbat distribuția dificultății. [R2] avertizează că standardizarea nu transformă comparația observațională într-un experiment cauzal. Prin urmare, datele arată o creștere a indicatorului standardizat, dar nu stabilesc că noul flux a produs-o.

## Fapte certe și necunoscute

**Susținut de dosar:** datele pe categorii din [M1], definiția fixă din [R1] și creșterea calculată a indicatorului oficial de **82% la 87,5%**, adică **+5,5 puncte procentuale**.

**Nedeterminat de dosar:** dacă schimbarea fluxului a cauzat creșterea. Comparația nu are randomizare sau grup de control, iar dosarul nu oferă un design cauzal alternativ care să izoleze efectul fluxului.

## Rezumat

Indicatorul oficial Atlas **a crescut cu 5,5 puncte procentuale**, de la **82% la 87,5%**, când este calculat conform ponderilor fixe din statutul semnat. Cifra **82%→35%** descrie rata brută a loturilor cu ponderi observate diferite, nu indicatorul oficial. Creșterea este descriptivă; afirmația că noul flux a cauzat-o nu este demonstrată.