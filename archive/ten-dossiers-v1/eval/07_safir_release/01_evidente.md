# Safir / release policy
[R1] Lansarea cere PASS de securitate pe digestul producției, cel puțin un token activ pe același digest și fereastră de mentenanță încheiată. Tokenul este activ cât cheia LUI de semnare este validă; revocarea altei chei nu îl stinge. Registrele de mai jos sunt complete, iar starea la momentul cerut se stabilește după data de efect.
[R2] Producție: aplicație2.10, digest abc210. Fereastră: până la10.10.2026 12:30 UTC+03:00. Semantica versiunii este pe componente numerice. Numele fișierelor nu identifică obiectul verificat.


# Registru semnat de livrare
[Q1] Teste de securitate:
| probă | digest | rezultat | efect |
|---|---|---|---|
| final_v12 | abc209 | PASS | 09.10T12:00Z |
| prelim_v3 | abc210 | PASS | 10.10T09:45Z |
| final_v13 | abc210 | FAIL | 10.10T10:05Z |
[Q2] Tokenuri:
| token | digest | cheie | emisie |
|---|---|---|---|
| APR-210 | abc210 | K7 | 09.10T12:00Z |
| APR-201 | abc210 | K8 | 10.10T09:40Z |
| APR-219 | abc209 | K9 | 10.10T09:50Z |
[Q3] Chei: K7 revocată efect10.10T09:00Z, înregistrată10:15Z; K8 validă de la01.10T00:00Z până la11.10T00:00Z; K9 validă. Toate orele fără altă indicație sunt UTC în2026.
