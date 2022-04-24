### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS (EXEMPLE no relacionat amb la pràctica)

#### Use case name
Afegir producte al carret-online

#### Version
1.0.0

#### Date
17/04/2021

#### Description
Aquesta es una petita descripció del cas d'ús (1-3 linies)

#### Actors
Actor1, Actor2, Actor3, ...

#### Preconditions
-- Llistat precondicions, podría estar buit si fos el cas --
1. L'usuari està a la pagina de productes
2. Precondició numero 2
3. ...

#### Main Pipeline :
-- Flux principal del cas d´ús enumerats --

1. L'usuari escull un producte.

2. Es comprova que el producte estigui en stock.

3. Si el producte esta en stock. S'afegeix al carret de compra.

4. Si l'usuari demana informació del producte escollit.
    
    4.1 **Include CU** DonarInformació

5. Si es vol demanar més productes:
    
    5.1 Tornar a **1**.

6. Si l'usuari vol modificar la comanda:
    
    6.1. **Extend CU** ModificarComanda

7. Mostrar missatge de gràcies per la compra.

#### Alternative Paths:
-- Fluxos alternatius --

---
##### Sub-Path 1
3. Si el producte no esta en stock
4. En paral·lel:
4.1. Informem al client que la petició s'esta procesant.
4.2. Busquem fabricants del producte
4.2.1. Enviem notificació a proveïdors.
4.2.2. Esperem resposta
4.2.3. Filtrem el que tinguin millor preu.
4.2.4. Afegim el producte al nostre stock

---
##### Sub-Path 2
5. Si no es vol demanar més productes:
5.1 Mostrar missatge de "Bona compra".

---
#### Exception Paths:
-- Excepcions que ens poguem trobar --

<u>Búsqueda de fabricants invàlida</u>
Hem búscat per un ID de fabricants que ja no es vàlid. Emetre missatge d'error i demanar
actualitzar els proveïdors.

#### Post-conditions
-- Llistat post-condicions, podría estar buit si fos el cas --
1. L'usuari ha de tenir el carret de compra preparat per poder començar a pagar.
2. Post-condició numero 2
3. ...

#### Comments
-- Afegir comentari si fos el cas --
