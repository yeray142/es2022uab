### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS - Pestanya usuari

#### Use case name
Pestanya usuari

#### Version
1.0.0

#### Date
24/04/2021

#### Description
Son les accions que es poden fer desde la pestanya d'usuari

#### Actors
Usuari

#### Preconditions
1. L'usuari te la sesio iniciada

#### Main Pipeline :

1. L'usuari clica la pestanya d'usuari

2. Es comprova que l'usuari tingui la sesio iniciada

3. Si l'usuari te la sesio iniciada:

    3.1 Mostrar dades d'usuari

4. Sino:
    
    4.1. Mostrar missatge: "Sessio no iniciada"

#### Alternative Paths:
Cap path alternatiu.

---
#### Exception Paths:

<u>No s'ha iniciat sesio correctament</u>
L'usuari i la contrasenya no coincideixen i/o no existeixen

#### Post-conditions
Cap post condició

#### Comments
Cap comentari
