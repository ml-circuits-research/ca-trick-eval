## 05_nova_facturi

Rulare: `luna-campaign-01`. [Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: fail** — Raportează subtotalul FACT drept net, fără scăderea creditelor90,20EUR. Calculul independent din tabele este5058,56.

> soldul net fără TVA pentru N-001–N-040 la închiderea registrului este **5.148,76 EUR**

**F2: fail** — Validează recomandarea supraestimată, contrar regulii de normalizare și alocare pe cheie fiscală.

> recomandarea de plată integrală este **corectă**

**F3: fail** — Citează chiar proveniența neaprobată Z1, dar îi refuză efectul și acordă prioritate verdictului literal al scriptului.

> nu schimbă rezultatul chitanței validate

Afirmații suplimentare greșite:

Nu am identificat.

Ultima secțiune declară imposibilă reconstruirea alocării fără a contrazice recipisa, deși protocolul și registrul complet permit calculul exact. Toate valorile corecte au fost verificate separat din datele de intrare.

