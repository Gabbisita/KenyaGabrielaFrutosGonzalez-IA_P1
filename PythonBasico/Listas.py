# -->Listas: El 'line-up' de un grupo de K-pop <--

# Una lista en Python es como el line-up de un grupo: una colección ordenada de elementos.
# Puede contener diferentes tipos de datos: strings, números, etc.
twice = ["Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"]
print("Line-up oficial de TWICE:", twice)


# --> Modificar un elemento: Cambio de posición <--

# Los elementos de una lista se pueden cambiar. Las listas son 'mutables'.
# Los índices empiezan en 0. Aquí, cambiamos el centro del performance.
posiciones_escenario = ["Vocalista", "Bailarín Principal", "Rapero"]
posiciones_escenario[1] = "Centro Visual" # El bailarín principal ahora es el centro.
print("Nuevas posiciones:", posiciones_escenario)


# --> Añadir miembros al grupo (o canciones al álbum) <--

# .append(): Añade un nuevo miembro al final del line-up.
stray_kids = ["Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin"]
stray_kids.append("I.N") # I.N se une al grupo.
print("Stray Kids con I.N:", stray_kids)

# .insert(): Añade un elemento en una posición específica.
# Es como añadir una colaboración sorpresa en medio de un concierto.
setlist = ["God's Menu", "Maniac"]
setlist.insert(1, "LALALALA (feat. Lisa)") # Se añade la colaboración en la segunda posición (índice 1).
print("Setlist actualizado:", setlist)

# .extend(): Fusiona una lista con otra, como una sub-unidad que se une al grupo principal.
dance_racha = ["Hyunjin", "Felix", "Lee Know"]
vocal_racha = ["Seungmin", "I.N"]
dance_racha.extend(vocal_racha) # Los miembros de Vocal Racha se unen al final de Dance Racha.
print("Unidad combinada:", dance_racha)


# --> Eliminar miembros (o canciones) <--

# .pop(): Elimina el último elemento si no se especifica índice.
# Es como la última canción del encore que termina.
encore = ["Mixtape: On Track", "Star Lost", "Youtiful"]
encore.pop() # Se elimina "Youtiful".
print("Encore después de la última canción:", encore)

# .pop(índice): Elimina el elemento en la posición indicada.
encore.pop(0) # Se elimina la primera canción, "Mixtape: On Track".
print("Encore final:", encore)

# .remove(valor): Busca y elimina la primera aparición de un valor específico.
# Perfecto para quitar una canción del setlist por su nombre.
canciones_repetidas = ["Case 143", "Super Bowl", "Case 143"]
canciones_repetidas.remove("Case 143") # Elimina la primera aparición de "Case 143".
print("Setlist sin la primera repetición:", canciones_repetidas)


# --> Buscar en la lista: Encontrando a tu bias <--

# .index(valor): Devuelve la posición (índice) de la primera aparición de un valor.
# ¿En qué posición del fanchant se nombra a "Felix"?
fanchant_order = ["Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix"]
posicion_felix = fanchant_order.index("Felix")
print(f"Felix es el número {posicion_felix + 1} en el fanchant.") # Sumamos 1 porque los índices empiezan en 0.

# .count(valor): Cuenta cuántas veces aparece un valor en la lista.
# ¿Cuántas líneas tiene Han en la canción?
lineas_cancion = ["Han", "Seungmin", "Han", "Lee Know", "Han"]
conteo_lineas_han = lineas_cancion.count("Han")
print(f"Han tiene {conteo_lineas_han} líneas en esta canción.")
