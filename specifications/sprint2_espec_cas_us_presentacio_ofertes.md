### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Presentar ofertes

#### Version
1.0.2

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
1. L'usuari indica que vol rebre ofertes.

2. Preguntar a les botigues la quantitat i preu dels productes.

3. Consultar les ofertes de les botigues.

4. Si la botiga no pot fer tota la comanda:

    4.1 Tornar a **1**.

5. Si la botiga utilitza l'entrega pròpia:

    5.1 Contactar amb un transportista.

    5.2 Calcular trajecte amb l'API de Google Maps.

    5.3 Afegir preu del transport a la oferta final.

6. Afegir oferta a la llista d'ofertes.

7. Si queden més botigues per revisar:

    7.1 Tornar a **1**.

8. Mostrar llista d'ofertes al client.

#### Alternative Paths:

5.2 Si el transportista no està disponible:

    5.2.1 Tornar a **5**.

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
