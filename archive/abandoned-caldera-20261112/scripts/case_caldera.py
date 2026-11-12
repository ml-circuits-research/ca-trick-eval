"""A signed static PDF decision whose selected option is a vector check mark."""
from io import BytesIO
from cases import finding


def decision_pdf():
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    buffer=BytesIO()
    page=canvas.Canvas(buffer,pagesize=(595,842),invariant=1)
    page.setTitle('Caldera CI-08 - decizie de investitii')
    page.setAuthor('Caldera - secretariat; document sintetic')
    ink=HexColor('#18313e');muted=HexColor('#50626b');line=HexColor('#c3cdd2')
    page.setFillColor(ink);page.setFont('Helvetica-Bold',11)
    page.drawString(48,789,'CALDERA INDUSTRIALS / COMITETUL DE INVESTITII')
    page.setFont('Helvetica-Bold',23);page.drawString(48,744,'Decizie de investitii')
    page.setFillColor(muted);page.setFont('Helvetica',11)
    page.drawString(48,720,'Proiect CI-08 - 12 noiembrie 2026 - EUR fara TVA')
    page.setStrokeColor(line);page.line(48,695,547,695)
    page.setFillColor(ink);page.setFont('Helvetica-Bold',12)
    page.drawString(48,663,'[D1] Plafonul total aprobat pentru CI-08')
    page.setFont('Helvetica',11)
    page.drawString(48,639,'Se aplica exclusiv optiunea bifata. Optiunile nu se cumuleaza.')
    page.drawString(48,621,'Un rand nebifat nu constituie aprobare.')
    for y,label in [(560,'100.000 EUR fara TVA'),(495,'60.000 EUR fara TVA')]:
        page.setStrokeColor(line);page.setLineWidth(1)
        page.roundRect(48,y-17,499,53,5,stroke=1,fill=0)
        page.setStrokeColor(ink);page.setLineWidth(1.3);page.rect(67,y,17,17,stroke=1,fill=0)
        page.setFillColor(ink);page.setFont('Helvetica-Bold',16);page.drawString(105,y+1,label)
    # Static ink strokes, as on a signed paper form; no contradictory field data.
    page.setStrokeColor(ink);page.setLineWidth(2.5)
    page.lines([(70,503,75,498),(75,498,83,511)])
    page.setFillColor(ink);page.setFont('Helvetica-Bold',12)
    page.drawString(48,420,'[D2] Aprobare si data de efect')
    page.setFont('Helvetica',11)
    page.drawString(48,395,'Optiunea bifata a fost aprobata si semnata de ambii membri.')
    page.drawString(48,377,'Decizia produce efect la 12.11.2026, ora 09:00 UTC.')
    page.setStrokeColor(line);page.line(48,307,260,307);page.line(335,307,547,307)
    page.setFont('Helvetica-Bold',11);page.drawString(48,286,'Mara Popa');page.drawString(335,286,'Andrei Rusu')
    page.setFont('Helvetica',10);page.drawString(48,268,'Presedinte comitet - semnat');page.drawString(335,268,'Responsabil risc - semnat')
    page.setFillColor(muted);page.setFont('Helvetica',9)
    page.drawString(48,113,'Document sintetic pentru review. Semnaturile sunt confirmate de mandat.')
    page.line(48,94,547,94);page.drawString(48,75,'CI-08 / DEC-12 / exemplar aprobat');page.drawRightString(547,75,'Pagina 1 din 1')
    page.showPage();page.save();return buffer.getvalue()


def build():
    docs={
'01_mandat.md':'''# Caldera — mandat pentru verificarea unei tranșe de investiții

[M1] Se verifică proiectul CI-08 la 12.11.2026, ora 12:00 UTC. Solicitarea este aprobarea unei tranșe de 80.000 EUR fără TVA. Nu există plăți sau angajamente anterioare care să consume plafonul.
[M2] Decizia semnată din 02_decizie.pdf stabilește plafonul total. Numai opțiunea bifată este aprobată; celelalte rânduri nu au efect de aprobare. O tranșă poate fi autorizată numai dacă valoarea ei nu depășește plafonul aprobat. Nu există alte condiții sau aprobări în acest dosar sintetic.
[M3] PDF-ul este exemplarul complet și aprobat. Semnăturile celor doi membri sunt autentice, ambii sunt competenți, iar actul produce efect la data indicată în el. Nu există amendamente sau condiții suspensive. Nota 03 trebuie verificată în raport cu decizia; nu o poate modifica.
''',
'02_decizie.pdf':decision_pdf(),
'03_nota.md':'''# Caldera — notă pentru directorul financiar

[N1] Pentru CI-08, nota preia plafonul de 100.000 EUR fără TVA din decizia semnată și recomandă autorizarea tranșei de 80.000 EUR: „Tranșa este cu 20.000 EUR sub plafonul aprobat și poate fi plătită integral.”
[N2] Nota nu reprezintă o nouă aprobare și nu modifică plafonul. Dosarul nu conține alte proiecte sau alte valori de tranșă.
'''}
    return dict(status='candidate',id='05_caldera_formular',title='Caldera — opțiunea aprobată dintr-un formular PDF',profile='simplu, interpretare vizuală',
        primary_mechanism='Semantica vizuală a unei opțiuni bifate se pierde la extragerea exclusivă a textului PDF.',
        task='Refă reviewul notei Caldera la 12.11.2026, ora 12:00 UTC. Care este plafonul aprobat pentru CI-08 și poate fi autorizată integral tranșa de 80.000 EUR? Verifică toate documentele din dosar.',documents=docs,
        findings=[
            finding('F1','Plafonul aprobat este 60.000 EUR fără TVA, nu 100.000 EUR.',['01_mandat.md#M2','01_mandat.md#M3','02_decizie.pdf#D1','02_decizie.pdf#D2'],'Pe pagina 1 este bifat exclusiv rândul de 60000; rândul de 100000 este nebifat. M2 și D1 dau efect numai opțiunii bifate. Decizia este valabilă și efectivă înaintea reviewului.',['T01','T13','T23']),
            finding('F2','Tranșa de 80.000 EUR nu poate fi autorizată integral: depășește plafonul cu 20.000 EUR; nota inversează sensul diferenței.',['01_mandat.md#M1','01_mandat.md#M2','02_decizie.pdf#D1','03_nota.md#N1','03_nota.md#N2'],'80000−60000=20000 peste plafon. Nota folosește opțiunea nebifată de 100000 și raportează greșit o marjă pozitivă de 20000. Nota nu are autoritate să modifice plafonul.',['T07','T08','T23'])],
        correct=['Tranșa solicitată este 80.000 EUR fără TVA.','Decizia este semnată de membrii competenți și produce efect înaintea reviewului.','Ambele valori sunt tipărite în formular; numai una este selectată.'])
