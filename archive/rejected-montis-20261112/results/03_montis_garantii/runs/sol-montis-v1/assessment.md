## 03_montis_garantii

Rulare: `sol-montis-v1`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Identifică grupul N/E/V cu cerere 120 și capacitate eligibilă 100, reutilizarea capacităților în controalele individuale și neaprobabilitatea pachetului.

> Grupul N–E–V solicită 120 și are acces numai la GA + GB = 100.

**F2: pass** — Demonstrează atât limita superioară a acoperirii (180), cât și o alocare fezabilă care o atinge; deficitul minim este exact 20.

> acoperirea maximă este 180, iar expunerea minimă neacoperită este exact 20

**F3: pass** — Arată că oferta exclusiv pentru S nu mărește capacitatea N/E/V și păstrează deficitul minim de 20.

> totalul nominal crește cu 20, dar acoperirea maximă a pachetului nu crește deloc.

**F4: pass** — Oferă o alocare completă validă cu garanția nouă pentru N și distinge corect ofertele, condiționat de incorporarea ofertei.

> Oferta pentru N permite acoperirea integrală; cea pentru S nu.

Afirmații suplimentare greșite:

Nu am identificat.

Findinguri suplimentare propuse de agent:

Nu am identificat findinguri noi distincte de etalon.

Toate cele patru findinguri sunt demonstrate corect. Alocările alternative oferite de model au fost verificate: respectă eligibilitățile, capacitățile și principalul fiecărui credit. Nu am identificat erori materiale. Observația că ofertele nu sunt încă incorporate explicitează condiționalitatea F4, fără a fi un finding nou distinct.

