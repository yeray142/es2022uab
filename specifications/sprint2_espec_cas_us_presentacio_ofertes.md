### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Presentar ofertes

#### Version
1.0.1

#### Date
18/05/2022

#### Description
La presentació d’ofertes és notificar a la persona de quines tendes properes li poden servir el que demana. Aquesta oferta llistarà els productes que se li serviran, indicant quantitat, preu, etc.; així com el dia d’entrega i hora aproximada. I també el preu total, incloent els càrrecs addicionals com pot ser el transport.

#### Actors
Client, Botiguer, Transportista, SysExternGoogleMaps

#### Preconditions
1. L'usuari ha d'estar registrat com a client.
2. L'usuari ha d'haver sol·licitat alguna comanda.

#### Main Pipeline :
1. Preguntar a les botigues la quantitat i preu dels productes.

2. Consultar les ofertes de les botigues.

3. Si la botiga no pot fer tota la comanda:

    3.1 Tornar a **1**.

4. Si la botiga utilitza l'entrega pròpia:

    4.1 Contactar amb un transportista.

6. Calcular trajecte amb l'API de Google Maps.

7. Afegir preu del transport a la oferta final.

8. Afegir oferta a la llista d'ofertes.

9. Si queden més botigues per revisar:

    9.1 Tornar a **1**.

10. Mostrar llista d'ofertes al client.

#### Alternative Paths:

4.2 Si el transportista no està disponible:

    4.2.1 Tornar a **4**.

---
#### Exception Paths:

<u>No hi ha botigues pròximes que puguin oferir la comanda</u>
Mostrar missatge d'error: "No s'han trobat botigues pròximes".

<u>No hi ha transportistes a la zona</u>
Mostrar missatge d'error: "No s'han trobat transportistes disponibles".

<u>Si l'API de Google Maps no està disponible</u>
Mostrar missatge d'error: "Google Maps no respon".

#### Post-conditions
1. Hi ha d'haver una botiga pròximes i ofertes disponibles per poder seleccionar comanda i enviar.

#### Comments
Cap comentari addicional.
