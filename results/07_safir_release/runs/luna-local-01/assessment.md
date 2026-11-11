## 07_safir_release

[Răspuns brut](answer.md) · [Etalon](reference.md)

**F1: pass** — Compară numeric componentele versiunii și verifică exact digestul și mediul testului.

> `2.10 > 2.9`

**F2: pass** — Invalidează tokenul pe baza revocării certificatului cu efect la 09:00, separând timpul de efect de timpul înregistrării.

> chiar dacă revocarea a fost introdusă în registru abia la 10:15 UTC

**F3: pass** — Convertește corect ora, recunoaște condiția calendarului ca satisfăcută, dar refuză lansarea pe celelalte două condiții; respinge explicit nota READY.

> Asta corespunde orei 09:30 UTC.

Afirmații suplimentare greșite:

Nu am identificat.

Rezumatul păstrează ambele impedimente, iar backupul și calendarul nu sunt transformate în probe ale autorizării.

