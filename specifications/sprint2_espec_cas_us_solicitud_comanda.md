### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Sol·licitar comanda

#### Version
1.0.1

#### Date
18/05/2022

#### Description
Sol·licitar una comanda és demanar al sistema a través d’una aplicació amigable una llista de queviures que necessita la persona. Aquí a diferència d’una botiga habitual per Internet, l’usuari no ha de cercar res, sinó indicar què vol o necessita.
Les comandes podran contenir un o més productes, amb quantitats diferents per a cada producte. El client haurà d’especificar la quantitat (encara que pot ser d’una forma no concreta) en la seva petició; però totes les comandes contindran valors específics concrets de cada producte.

#### Actors
Client, Botiguer, ProveidorExtern

#### Preconditions
1. L'usuari ha d'estar registrat com a client.

#### Main Pipeline :
1. L'usuari afegeix un producte a la cistella

2. Si el producte no existeix:

    2.1 Mostrar missatge d'error: "Producte no existeix".

    2.2 Eliminar producte de la cistella.

    2.3 Tornar a **1**.

3. Afegir banner de publicitat

4. Si es vol demanar més productes:
    
    3.1 Tornar a **1**.

5. Mostrar missatge de comanda sol·licitada correctament.

#### Alternative Paths:

---
#### Exception Paths:
-- Excepcions que ens poguem trobar --

<u>El client no ha sel·leccionat cap producte</u>
Mostrar missatge d'error: "No s'ha sel·leccionat cap producte".

<u>No hi ha producte en stock</u>
Mostrar missatge d'error: "El producte sol·licitat no està en stock actualment".

#### Post-conditions
1. El client ha d'haver escullit algun producte per poder presentar ofertes.

#### Comments
Cap comentari addicional.
