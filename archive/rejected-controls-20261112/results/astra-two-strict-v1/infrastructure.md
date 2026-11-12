# Încercare tehnic invalidă — exclusă din evaluarea modelului

Filesystem-ul izolat nu monta inițial ținta symlinkului `/etc/resolv.conf`, aflată în `/run/systemd/resolve/`. Cererile de rețea au expirat înaintea obținerii unui review. Rularea a fost întreruptă, nu este model păcălit și nu produce scor de findinguri.

Remediere: se montează read-only numai fișierul resolverului, fără a expune restul `/run` sau proiectul. Încercarea corectată folosește un run-id nou, `astra-two-strict-v2`, cu aceleași documente și același prompt.
