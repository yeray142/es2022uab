### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Seleccionar comanda i enviar

#### Version
1.0.0

#### Date
08/05/2022

#### Description
Finalment la selecció de la comanda i enviament succeeix quan l’usuari vol acceptar una de les ofertes rebudes. Llavors es genera una comanda en ferm i el botiguer rep totes les dades necessàries per a servir-la.

#### Actors
Client, Botiguer

#### Preconditions
1. L'usuari ha d'estar registrat com a client.
2. L'usuari ha d'haver sol·licitat alguna comanda.
3. L'usuari ha d'haver triat alguna oferta presentada.

#### Main Pipeline :
1. L'usuari indica que vol seleccionar comanda.

2. **Include CU** Comprovar màxim comandes.

3. Si no hem arribat al màxim de comandes:

    3.1 Mostrar missatge de comanda seleccionada i enviada.
    
    3.2 Enviar missatge al botiguer de la selecció de la comanda.

#### Alternative Paths:

---
##### Sub-Path 1

3. Si  hem arribat al màxim de comandes:

    3.2 Mostrar missatge d'error: "Imposible enviar comanda, hem arribat al màxim de 100 simultànies"

---
#### Exception Paths:

#### Post-conditions
1. S'ha d'haver seleccionat i enviat comanda per fer el seguiment de l'enviament.
2. S'ha d'haver seleccionat comanda per poder pagar-la.

#### Comments
Cap comentari addicional.
