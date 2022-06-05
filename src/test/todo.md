# Llista de tests a realitzar (TODO list)

A continuació s'expliquen els tests plantejats per a la comprovació del correcte funcionament
del cas d'ús **"Cerca de Producte"**, que es pot definir com a part del cas d'ús **"Sol·licitud
de Comanda"**:

1. Comprovar que es crida al Proveïdor Extern una vegada per cada producte de la comanda.
2. Comprovar que la funció retorna una tupla amb dues llistes, una de disponibilitats i l'altre de bàners.
3. Comprovar que quan la publicitat retorna "True" (té bàner) llavors la funció retorna "True" en aquest producte, sinó "False".
4. Comprovar que es crida a la base de dades dels productes disponibles.
5. Comprovar que quan està disponible en alguna botiga, llavors la funció retorna "True" en aquest producte, sinó "False".