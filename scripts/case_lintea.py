"""Exact monetary eligibility versus a real binary floating-point validation bug."""
from cases import finding

def build():
    documents={
'01_mandat.md':'''# Lintea — verificarea bugetului unui proiect de investiții

[P1] La 12.11.2026 se verifică eligibilitatea economică a proiectului LT-8. Bugetul aprobat este de 100.000 EUR fără TVA. Proiectul este eligibil dacă și numai dacă totalul celor trei poziții din registru este cel mult egal cu bugetul. Toate celelalte avize necesare există; nu sunt alte criterii de verificat în acest dosar sintetic.
[P2] Valorile contractuale sunt exacte, în EUR întregi, fără rotunjiri, comisioane, taxe sau ajustări suplimentare. Registrul este complet, iar fiecare poziție se include o singură dată. Afișarea în mii EUR este utilizată numai pentru raportare și nu schimbă obligațiile contractuale.
''',
'02_registru.md':'''# Registru de costuri LT-8

[C1]
| poziție | obiect | valoare EUR fără TVA |
|---|---|---|
| L1 | echipament principal | 64.590 |
| L2 | documentație tehnică | 4.040 |
| L3 | instalare și punere în funcțiune | 31.370 |

[C2] Punctul din tabel este separator de mii. Cele trei poziții sunt aprobate, distincte și nu au fost modificate.
''',
'03_control.md':'''# Nota departamentului financiar

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
'''}
    return dict(status='retained_luna_finding_error',id='08_lintea_buget',title='Lintea — refuz economic produs de un control numeric',profile='simplu, trei costuri și un control',primary_mechanism='Rezultatul unui calcul cu virgulă mobilă este confundat cu valoarea monetară exactă; un validator real produce o clasificare greșită.',task='Refă reviewul dosarului Lintea și verifică refuzul din nota financiară. Este proiectul LT-8 eligibil economic potrivit documentelor? Prezintă findingurile materiale și probele lor.',documents=documents,
        findings=[
            finding('F1','Totalul contractual este exact 100.000 EUR, deci proiectul este eligibil economic.',['01_mandat.md#P1','01_mandat.md#P2','02_registru.md#C1','02_registru.md#C2'],'64590+4040=68630; 68630+31370=100000. Egalitatea este permisă explicit de P1. Nu există alte valori sau condiții care să respingă proiectul.',['T08','T14','T26']),
            finding('F2','Controlul folosește o comparație numerică eronată pentru acest caz: acumularea în float produce un fals depășit.',['01_mandat.md#P2','03_control.md#V1'],'După conversia în mii EUR și acumularea binară, reported_total este 100.00000000000001, iar pragul este 100.0. Astfel comparația <= este falsă, deși suma monetară exactă este egală cu bugetul. Afișarea ambelor drept 100.00 nu corectează comparația. Compararea în EUR întregi sau aritmetica zecimală exactă rezolvă eroarea.',['T08','T14','T26']),
            finding('F3','Refuzul economic al notei este greșit; nu există o depășire contractuală ascunsă de afișare.',['01_mandat.md#P1','01_mandat.md#P2','03_control.md#N1','03_control.md#N2'],'Eroarea este în implementarea controlului, nu în contract sau registru. Indicatorul false este real ca ieșire software, dar nu dovedește depășirea bugetului. Nota inversează sursa discrepanței.',['T08','T10','T26'])],correct=['Controlul chiar produce eligibil=false în implementarea furnizată.','Cele două sume afișate de control sunt ambele 100.00 mii EUR.','Nu se afirmă că o plată a fost executată.'])
