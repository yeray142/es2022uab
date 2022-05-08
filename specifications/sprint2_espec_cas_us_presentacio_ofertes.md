### SPRINT 2 - ESPECIFICACIÓ CAS D'ÚS

#### Use case name
Presentar ofertes

#### Version
1.0.0

#### Date
08/05/2022

#### Description
La presentació d’ofertes és notificar a la persona de quines tendes properes li poden servir el que demana. Aquesta oferta llistarà els productes que se li serviran, indicant quantitat, preu, etc.; així com el dia d’entrega i hora aproximada. I també el preu total, incloent els càrrecs addicionals com pot ser el transport.

#### Actors
Client

#### Preconditions
1. L'usuari ha d'estar registrat com a client.
2. L'usuari ha d'haver sol·licitat alguna comanda.

#### Main Pipeline :
1. L'usuari indica que vol ofertes per la seva comanda.

2. **Include CU** Oferir botigues pròximes

3. L'usuari tria una de les botigues.

4. Si es vol canviar de botiga:
    
    4.1 Tornar a **2**.

5. Mostrar missatge d'oferta desada correctament.

#### Alternative Paths:

---
#### Exception Paths:

<u>No hi ha botigues pròximes</u>
Mostrar missatge d'error: "No s'han trobat botigues pròximes".

<u>L'usuari no tria cap botiga</u>
Mostrar missatge d'error: "No s'ha triat cap botiga".

#### Post-conditions
1. Hi ha d'haver una botiga escullida per poder seleccionar comanda i enviar.

#### Comments
Cap comentari addicional.
