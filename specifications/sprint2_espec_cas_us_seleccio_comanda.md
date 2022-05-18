### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Seleccionar comanda i enviar

#### Version
1.0.1

#### Date
18/05/2022

#### Description
Finalment la selecció de la comanda i enviament succeeix quan l’usuari vol acceptar una de les ofertes rebudes. Llavors es genera una comanda en ferm i el botiguer rep totes les dades necessàries per a servir-la.

#### Actors
Client, SysExternPaypal, SysExternEntitatBancaria, Botiguer

#### Preconditions
1. L'usuari ha d'estar registrat com a client.
2. L'usuari ha d'haver sol·licitat alguna comanda.
3. L'usuari ha d'haver triat alguna oferta presentada.

#### Main Pipeline :
1. El client tria una oferta.

2. Tria un mètode de pagament disponible

3. Si el mètode de pagament és Paypal:

    3.1 Redireccionar a la website de Paypal per fer el pagament.

4. Generar comanda i avisar al botiguer.

5. Canvia la disponibilitat del transportista per a la hora i dia d'entrega.

6. Mostrar missatge de comanda en preparació d'enviament.

#### Alternative Paths:

---
##### Sub-Path 1

3. Si el mètode de pagament NO és Paypal:

    3.2 Redireccionar a la entitat bancària per fer el pagament.

---
#### Exception Paths:

<u>Si el web de Paypal no està disponible</u>
Mostrar missatge d'error: "Paypal no es troba disponible, trii un altre mètode de pagament".

<u>Si l'Entitat Bancària no està disponible</u>
Mostrar missatge d'error: "L'entitat bancària no respon a la nostra petició, trii un altre mètode de pagament".

#### Post-conditions
1. S'ha d'haver seleccionat i enviat comanda per fer el seguiment de l'enviament.
2. S'ha d'haver seleccionat comanda per poder pagar-la i enviar-la.

#### Comments
Cap comentari addicional.
