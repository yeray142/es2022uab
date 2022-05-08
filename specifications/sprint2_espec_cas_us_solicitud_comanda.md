### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Sol·licitar comanda

#### Version
1.0.0

#### Date
08/05/2022

#### Description
Sol·licitar una comanda és demanar al sistema a través d’una aplicació amigable una llista de queviures que necessita la persona. Aquí a diferència d’una botiga habitual per Internet, l’usuari no ha de cercar res, sinó indicar què vol o necessita.
Les comandes podran contenir un o més productes, amb quantitats diferents per a cada producte. El client haurà d’especificar la quantitat (encara que pot ser d’una forma no concreta) en la seva petició; però totes les comandes contindran valors específics concrets de cada producte.

#### Actors
Client

#### Preconditions
1. L'usuari ha d'estar registrat com a client.

#### Main Pipeline :
1. L'usuari escull un producte.

2. L'usuari indica la quantitat d'aquest producte.

3. La comanda s'afegeix a la cistella.

4. **Include CU** Recomanar productes

5. Si es vol demanar més productes:
    
    5.1 Tornar a **1**.

6. Mostrar missatge de comanda sol·licitada correctament.

#### Alternative Paths:

---
#### Exception Paths:
-- Excepcions que ens poguem trobar --

<u>El client no ha sel·leccionat cap producte</u>
Mostrar missatge d'error: "No s'ha sel·leccionat cap producte".

#### Post-conditions
1. El client ha d'haver escullit algun producte per poder presentar ofertes.

#### Comments
Cap comentari addicional.
