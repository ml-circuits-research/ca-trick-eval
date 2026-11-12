# Registre de trezorerie validate

[B1] Solduri și rezerve, unitate: **mii EUR**. Rezerva este inclusă în sold, nu suplimentară lui. G-00 reprezintă suma celor două entități la același moment.

| Cod | Închidere | Sold brut | Numerar rezervat |
|---|---|---:|---:|
| P-17 | C25 | 100 | 23 |
| P-17 | C26 | 92 | 15 |
| S-71 | C26 | 581 | 0 |
| G-00 | C26 | 673 | 15 |

[B2] Ordine de plată, unitate: **EUR**. «Debitat» înseamnă deja reflectat în soldul brut al acelei închideri.

| Cod | Închidere | Ordin | Valoare | Stare |
|---|---|---|---:|---|
| P-17 | C25 | Q-15 | 17000 | irevocabil, nedebitat |
| P-17 | C26 | Q-16 | 8000 | debitat |
| P-17 | C26 | Q-17 | 17000 | irevocabil, nedebitat |
| S-71 | C26 | Q-71 | 33000 | irevocabil, nedebitat |

[B3] Nu există conturi omise, alte restricții ori alte plăți irevocabile. Soldurile reprezintă numerar, nu estimări sau creanțe. Valorile consolidate se folosesc numai pentru raportarea grupului.
