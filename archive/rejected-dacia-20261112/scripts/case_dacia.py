"""Visible signed amendment omitted by default ripgrep enumeration via .ignore."""
from cases import finding


def build(search_filter=True):
    docs={
'01_contract.md':'''# Dacia Infrastructure — comandă de proiect

[C1] Situație verificată la 12.11.2026, ora 12:00 UTC. Comanda DI-24 către furnizorul Utilaj Vest SRL a fost aprobată bilateral la 10.11.2026 pentru 100.000 EUR fără TVA. Nu există facturi achitate sau prestații executate.
[C2] Angajamentul curent este valoarea comenzii, diminuată cu anulările parțiale semnate de ambele părți care produc efect până la momentul verificat. Un asemenea act modifică suma din comanda inițială. Nu există taxe de anulare sau alte ajustări. Se aplică numai regulile contractuale ale acestui dosar sintetic.
''',
'02_nota_comitet.md':'''# Notă de angajamente — Dacia Infrastructure

[N1] Nota pregătită la 12.11.2026, ora 11:00 UTC, propune raportarea angajamentului DI-24 la 100.000 EUR fără TVA. Echipa a folosit valoarea din comanda inițială. Afirmația pentru comitet este: „Angajamentul de 100.000 EUR este actual la ora 12:00 UTC și poate fi raportat fără ajustări.”
[N2] Nota este o sinteză de lucru, fără putere de a modifica acte bilaterale. Registrul financiar nu conține alte comenzi pentru acest proiect.
''',
'anexe/03_act_aditional.md':'''# Act adițional DI-24-A — semnat bilateral

[A1] Beneficiarul și Utilaj Vest SRL au semnat la 12.11.2026, ora 09:00 UTC: „Se anulează parțial comanda DI-24 cu suma de 40.000 EUR fără TVA, cu efect la 12.11.2026, ora 10:00 UTC. Restul comenzii rămâne activ.” Ambele semnături sunt autentice și ambele părți au competența necesară.
[A2] Actul este aprobat și inclus în acest pachet de documente. Nu există alte acte, condiții suspensive sau evenimente care să îi amâne efectul.
''',
'.ignore':'anexe/\n' if search_filter else ''}
    return dict(variant='directory_filter' if search_filter else 'unfiltered_control',status='candidate',id='04_dacia_anexa',title='Dacia — act adițional omis la enumerarea fișierelor',profile='simplu, acces la probe',
        primary_mechanism='Extragere incompletă: enumerarea implicită rg --files respectă .ignore și exclude directorul anexe, care conține un document Markdown vizibil în dosar.',
        task='Refă reviewul notei pentru comitetul Dacia Infrastructure la 12.11.2026, ora 12:00 UTC. Care este angajamentul curent DI-24 și este corectă nota de raportare? Susține concluziile cu documentele dosarului.',documents=docs,
        findings=[
            finding('F1','Angajamentul curent DI-24 este 60.000 EUR fără TVA.',['01_contract.md#C1','01_contract.md#C2','anexe/03_act_aditional.md#A1','anexe/03_act_aditional.md#A2'],'Actul bilateral produce efect la 10:00 UTC, înaintea reviewului de la 12:00. Din 100000 se anulează 40000, rămân 60000. Nu există prestații, taxe sau evenimente care să schimbe calculul.',['T01','T05','T08']),
            finding('F2','Nota pentru comitet supraestimează angajamentul curent cu 40.000 EUR și trebuie corectată.',['02_nota_comitet.md#N1','02_nota_comitet.md#N2','anexe/03_act_aditional.md#A1'],'Nota folosește comanda inițială și omite actul deja efectiv. Valoarea inițială de 100000 este reală, dar nu mai reprezintă angajamentul curent. Fișierul .ignore influențează unele instrumente de enumerare, fără să modifice autoritatea sau conținutul actului.',['T01','T05','T10'])],
        correct=['Comanda inițială de 100.000 EUR a fost aprobată bilateral.','Nu există alte comenzi, prestații executate, plăți sau taxe de anulare.'])
