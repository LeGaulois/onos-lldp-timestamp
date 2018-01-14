# Objectif
Modifier le fonctionnement de la découverte de liens sur Onos afin d'inclure un timestamp dans les messages LLDP.
Ce timestamp permettra de calculer le délai entre 2 switchs.

# Installation
Remplacer les fichiers du code source par ceux présents dans ce dépôt github.
Recompiler Onos avec buck:
```
onos-buck build onos --show-output
```

# Exemples
```
src=of:0000000000000001/1, dst=of:000092c84183ac45/1, delay=31 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:0000000000000001/2, dst=of:000092c84183ac45/2, delay=51 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:0000000000000001/3, dst=of:000006955583104c/3, delay=201 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:0000000000000001/6, dst=of:0000000000000003/3, delay=17 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:0000000000000003/1, dst=of:000092c84183ac45/6, delay=87 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:0000000000000003/3, dst=of:0000000000000001/6, delay=507 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000006955583104c/1, dst=of:000092c84183ac45/3, delay=21 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000006955583104c/3, dst=of:0000000000000001/3, delay=34 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000092c84183ac45/1, dst=of:0000000000000001/1, delay=173 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000092c84183ac45/2, dst=of:0000000000000001/2, delay=435 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000092c84183ac45/3, dst=of:000006955583104c/1, delay=133 ms, type=DIRECT, state=ACTIVE, expected=false
src=of:000092c84183ac45/6, dst=of:0000000000000003/1, delay=19 ms, type=DIRECT, state=ACTIVE, expected=false
```

