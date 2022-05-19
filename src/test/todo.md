# Llista de tests a realitzar

## Introducció:
A continuació s'expliquen els tests plantejats per a la comprovació del correcte funcionament
del cas d'ús **" Cerca de Producte"**, que es pot definir com a part del cas d'ús **" Sol·licitud
de Comanda"**.

## Tests
En total, disposeu de 5 tests, explicats i detallats a continuació. 

### Test 1: Disponibilitat
El primer test comprova que els resultats proporcionats coincideixen efectivament
amb productes disponibles i no resultats que no siguin coherents.

El test comprovarà, amb una mostra controlada, si els productes marcats com a disponible realment 
són disponibles en alguna de les botigues de la base de dades.

Aquest test **accedeix a la base de dades de les botigues**.

### Test 2: Manca de botigues
Es comprova, **accedint a la base de dades de les botigues**, que s'han revisat totes i cadascuna
de les botigues de la base de dades abans de retornar el resultat.

Amb una mostra controlada, revisarem si hi ha algun producte marcat com a no disponible i que 
realment sí que és disponible en alguna de les botigues.

### Test 3: Banners incongruents
Comprova que els productes retornats són efectivament aquells que tenen un banner associat
i no hi ha incongruències amb el resultat.

Aquest test utilitza el **Mock del servei de bàners**.

### Test 4: Productes incoherents
Comprova que no s'hagi retornat algun producte que no coincideix amb la cerca feta, és a dir, 
amb aquells productes que tenim a la comanda.

### Test 5: Manca de banners
Comprova que els productes retornats són aquells que efectivament tenen publicitat associada
i no hi manca cap d'ells.

Aquest test utilitza el **Mock del servei de bàners**.