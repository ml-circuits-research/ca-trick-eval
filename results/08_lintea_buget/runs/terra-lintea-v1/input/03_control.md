# Nota departamentului financiar

[N1] Controlul automat a returnat `eligibil: false`. Nota concluzionează: „LT-8 depășește bugetul de 100.000 EUR și trebuie respins economic. Egalitatea aparentă a sumelor afișate este numai un efect al afișării.” Se solicită confirmarea sau corectarea acestui refuz.

[V1] Sursa exactă a controlului folosit, Python 3; fără alte intrări sau configurări:

```python
import json

budget_eur = 100000
costs_eur = (64590, 4040, 31370)
reported_total = 0.0
for amount in costs_eur:
    reported_total += amount / 1000

result = {
    "unitate": "mii EUR",
    "cost_afisat": f"{reported_total:.2f}",
    "buget_afisat": f"{budget_eur / 1000:.2f}",
    "eligibil": reported_total <= budget_eur / 1000,
}
print(json.dumps(result, ensure_ascii=False))
```

[N2] Nota nu modifică valorile din contract sau criteriul economic. Nu există plăți executate în acest dosar.
