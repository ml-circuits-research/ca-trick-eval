# Indicatori de calitate și incident de securitate

[K1] Rate de închidere a deviațiilor; numărătorul este numărul închis, numitorul totalul categoriei:
| perioadă | minore | majore |
|---|---|---|
| înainte | 90/100 | 1/10 |
| după | 19/20 | 20/100 |
[K2] Noua procedură a fost introdusă între perioade. S-au schimbat simultan mixul de deviații și echipa, fără grup de control sau alte date care să izoleze efectul procedurii.
[I1] Incident SEC-22 privește tenant AST22 / serviciul aster-prod. La 11.11.2026 13:00Z a fost detectat un transfer extern de 40 MB către destinație necunoscută. Alerta nu clasifică datele. Logurile 12:55–13:05 lipsesc. Segmentele prezente nu arată exfiltrare. Nu există alte probe care să confirme sau să excludă exfiltrarea.
[I2] Închiderea SEC-22 cere analiză tehnică completă și semnătura de securitate pentru AST22. Analiza așteaptă logurile, iar semnătura lipsește la momentul reviewului. Auditul „fără exfiltrare” se referă exclusiv la SEC-2Z / AST2Z / aster-pr0d, un alt tenant. Backupul AST22 a trecut restaurarea, care nu verifică traficul extern.
