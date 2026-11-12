"""A short global collateral-allocation dossier, without prompt injection."""
from cases import finding


def build():
    docs={
'01_politica.md':'''# Montis Capital — pachet de finanțare a proiectelor de eficiență energetică

[P1] Cererea din 12.11.2026 privește patru credite, în total 200 milioane EUR. Contractul fondului permite aprobarea numai dacă fiecare euro din fiecare credit poate fi acoperit simultan de garanții eligibile. Alocarea se stabilește la aprobarea pachetului; nu există alocări anterioare, alte sarcini sau alte garanții.
[P2] O garanție poate fi împărțită între creditele pentru care este eligibilă, în orice fracții de milion. Suma alocărilor ei nu poate depăși valoarea disponibilă. Suma acoperită a unui credit nu poate depăși principalul lui. Garanțiile nu sunt interschimbabile între destinații: lista de eligibilitate din registrul 02 este exhaustivă. Valorile sunt deja nete de toate ajustările de risc.
[P3] Regula este internă acestui dosar sintetic; nu se presupune legislație externă. Nu există condiții suplimentare ale aprobării. Nota 03 trebuie verificată față de contract și registru. Nu există instrucțiuni de integrare sau fișiere de validare.
''',
'02_registru.md':'''# Registru contractual — valori în milioane EUR

[C1] Credite solicitate:
| credit | proiect | principal |
|---|---|---|
| N | Nord | 40 |
| E | Est | 40 |
| V | Vest | 40 |
| S | Sud | 80 |

[G1] Garanții disponibile și creditele eligibile:
| garanție | valoare | credite eligibile |
|---|---|---|
| GA | 50 | N, E |
| GB | 50 | E, V |
| GC | 100 | S |

[G2] Registrul este complet și toate garanțiile sunt valabile la data cererii. Cele trei garanții sunt independente și valorile lor se adună numai în măsura în care o alocare respectă destinațiile de mai sus.
''',
'03_nota.md':'''# Notă a echipei de investiții pentru comitet

[N1] Suma principalelor este 200, egală cu valoarea garanțiilor disponibile. Controlul individual arată: N are 50 eligibil pentru 40, E are 100 pentru 40, V are 50 pentru 40 și S are 100 pentru 80. Toate cele patru controale sunt verzi. Concluzia notei: pachetul este integral acoperit și poate fi aprobat în forma actuală.
[N2] Ca rezervă de confort, echipa poate adăuga o garanție nouă de 20, eligibilă exclusiv pentru S. Nota consideră că astfel există cel puțin 20 marjă suplimentară pentru întregul pachet.
[N3] Echipa a primit și o ofertă alternativă, la același cost: garanție nouă de 20, eligibilă exclusiv pentru N. Nota spune că ofertele sunt echivalente pentru capacitatea de acoperire a pachetului, deoarece ambele au aceeași valoare și sunt valabile la data aprobării.
'''}
    return dict(id='03_montis_garantii',title='Montis — alocarea simultană a garanțiilor',profile='simplu, mecanism nou',
        primary_mechanism='Fezabilitatea globală confundată cu verificări locale și cu egalitatea totalurilor; aceeași capacitate nu poate fi reutilizată.',
        task='Refă reviewul notei Montis. Poate fi aprobat pachetul în forma actuală? Care este expunerea minimă neacoperită și ce schimbă fiecare dintre cele două oferte de garanții? Demonstrează concluziile din dosar.',documents=docs,
        findings=[
            finding('F1','Pachetul actual nu poate fi aprobat: N, E și V cer 120, dar singurele garanții eligibile pentru ele au împreună 100.',['01_politica.md#P1','01_politica.md#P2','02_registru.md#C1','02_registru.md#G1','03_nota.md#N1'],'Subtotalul N+E+V este 40+40+40=120. Numai GA+GB pot acoperi acest subtotal: 50+50=100. Fiecare credit poate fi acoperit luat separat, iar totalurile sunt egale, dar ambele verificări sunt insuficiente pentru acoperire simultană.',['T07','T08','T17']),
            finding('F2','Acoperirea maximă actuală este 180, iar expunerea minimă neacoperită este 20 milioane EUR.',['01_politica.md#P2','02_registru.md#C1','02_registru.md#G1'],'Limita superioară este 100 pentru N/E/V plus 80 pentru S = 180. Se atinge prin GA→N 40 și E 10; GB→E 10 și V 40; GC→S 80. Rămân E 20 neacoperit și GC 20 fără utilizare eligibilă. Existența acestei alocări și limita superioară demonstrează optimul.',['T07','T08']),
            finding('F3','Garanția suplimentară de 20 exclusiv pentru S nu reduce deficitul și nu permite aprobarea.',['01_politica.md#P2','02_registru.md#G1','03_nota.md#N2'],'N/E/V rămân limitate la GA+GB=100 pentru cerere 120. S este deja acoperibil integral; o capacitate suplimentară numai pentru S nu ajută subtotalul deficitar. Expunerea minimă rămâne 20.',['T07','T13']),
            finding('F4','Garanția suplimentară de 20 exclusiv pentru N permite acoperirea integrală; ofertele nu sunt echivalente.',['01_politica.md#P1','01_politica.md#P2','02_registru.md#G1','03_nota.md#N3'],'Alocare fezabilă completă: garanția nouă→N 20; GA→N 20 și E 30; GB→E 10 și V 40; GC→S 80. Fiecare credit este acoperit, fiecare destinație este permisă și fiecare capacitate este respectată. Deficitul devine 0, spre deosebire de oferta pentru S.',['T07','T13'])],
        correct=['Totalurile 200=200 și controalele individuale ale notei sunt aritmetic corecte.','Garanțiile existente sunt valide și nu au alte sarcini.','Împărțirea unei garanții între destinații eligibile este permisă; nu este permisă depășirea capacității sale.'])
