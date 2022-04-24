### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS - Fer seguiment d'enviament

#### Use case name
Fer seguiment d'enviament

#### Version
1.0.0

#### Date
24/04/2021

#### Description
Opcions de fer seguiment de l'enviament desde el mapa de google maps.

#### Actors
Usuari, SysExternGoogleMaps

#### Preconditions
1. L'usuari te la sesio iniciada
2. Hi hagi una entrega pendent


#### Main Pipeline :

1. L'usuari clica a Fer Seguiment d'enviaments

2. Es comprova que l'usuari tingui la sesio iniciada

3. Si l'usuari te la sesio iniciada:

    3.1 Comprova si hi ha enviament
        
        3.1.1 Mostra el mapa de google maps
        
    3.2 Si no hi ha enviament:
        
        3.2.1 Mostrar missatge: "No existeix cap enviament pendent"

4. Sino:
    
    4.1. Mostrar missatge: "Sessio no iniciada"

#### Alternative Paths:
Cap path alternatiu.

---
#### Exception Paths:

<u>No s'ha iniciat sesio correctament</u>
L'usuari i la contrasenya no coincideixen i/o no existeixen

<u>No existeix enviaments</u>
No hi ha enviaments pendents

<u>No funciona Google maps</u>
Servei de Google maps no disponible

#### Post-conditions
Cap post condició

#### Comments
Cap comentari
