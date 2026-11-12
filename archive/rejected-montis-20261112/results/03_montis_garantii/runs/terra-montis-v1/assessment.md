## 03_montis_garantii

Rulare: `terra-montis-v1`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Identifică grupul N/E/V cu cerere 120 și capacitate eligibilă 100, reutilizarea capacităților în controalele individuale și neaprobabilitatea pachetului.

> Eroarea este deducția că aceste controale individuale dovedesc acoperirea simultană.

**F2: pass** — Demonstrează atât limita superioară a acoperirii (180), cât și o alocare fezabilă care o atinge; deficitul minim este exact 20.

> Expunerea minimă neacoperită este de 20 milioane EUR

**F3: pass** — Arată că oferta exclusiv pentru S nu mărește capacitatea N/E/V și păstrează deficitul minim de 20.

> Expunerea minimă neacoperită a pachetului ar rămâne 20 milioane EUR

**F4: pass** — Oferă o alocare completă validă cu garanția nouă pentru N și distinge corect ofertele, condiționat de incorporarea ofertei.

> oferta pentru S lasă 20 milioane EUR neacoperite, iar cea pentru N reduce expunerea minimă neacoperită la zero.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate cele patru findinguri sunt demonstrate corect. Alocările alternative oferite de model au fost verificate: respectă eligibilitățile, capacitățile și principalul fiecărui credit. Nu am identificat erori materiale. Observația că ofertele nu sunt încă incorporate explicitează condiționalitatea F4, fără a fi un finding nou distinct.

