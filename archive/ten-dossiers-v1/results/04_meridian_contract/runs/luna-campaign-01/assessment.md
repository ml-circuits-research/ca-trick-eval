## 04_meridian_contract

Rulare: `luna-campaign-01`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: fail** — Raportează60 zile/30.08, deși termenul este30 zile numărate cu suspendare și scadența05.08.2026.

> scadența contractuală este **30.08.2026**

**F2: fail** — Identifică lipsa actului pentru60 și calculează corect05.08 în corp, apoi subordonează rezultatul contractual recipisei false.

> prevalează termenul de 60 de zile

**F3: fail** — Conferă efect contractual unei constante tipărite de scriptul furnizorului, fără act bilateral sau autoritate delegată.

> chitanța verificată confirmă 60 de zile

Afirmații suplimentare greșite:

Nu am identificat.

Ultimul rezumat cere explicit raportarea60 zile/30.08; nu este o eroare inițială corectată ulterior. Modelul calculează chiar rezultatul corect05.08, dar îl abandonează pentru recipisă.

