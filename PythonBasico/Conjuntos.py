# --> Sets: Tu colección de photocards <--

# Un 'set' es como tu binder de photocards: es una colección de elementos únicos y sin un orden específico.
# No importa cuántas veces tengas la misma photocard, en tu colección solo cuenta como una.
photocards = {"Felix", "Hyunjin", "Bang Chan", "Felix", "Felix"}
print("Mi colección de photocards (sin duplicados):", photocards) # "Felix" solo aparece una vez.

# Como no tienen un orden, cada vez que lo imprimo, pueden aparecer en un orden diferente.
print("La misma colección, impresa de nuevo:", photocards)


# --> Gestionando la colección <--

# .add(): Añadir una nueva photocard a la colección.
photocards.add("Lee Know")
print("Colección con un nuevo miembro:", photocards)

# .remove(): Quitar una photocard específica.
# Si intentas quitar una que no tienes, te dará un error (KeyError).
photocards.remove("Hyunjin")
print("Colección después de un intercambio:", photocards)
# photocards.remove("Seungmin") # KeyError: 'Seungmin' no está en la colección.

# .discard(): Quitar una photocard, pero sin dar error si no la tienes.
# Es más seguro si no estás seguro de tenerla.
photocards.discard("Jeongin") # No pasa nada, aunque no estuviera en el set.
print("Intentando descartar una photocard que no tengo:", photocards)


# --> Reglas de los Sets: Solo elementos inmutables <--

# En un set solo puedes guardar elementos 'inmutables' (que no se pueden cambiar), como strings, números o tuplas.
# No puedes guardar una lista, porque es mutable.
# Es como intentar meter un setlist (que puede cambiar) dentro de tu colección de photocards (que es fija).
lineup_fijo = ("Karina", "Winter") # Una tupla es inmutable.
lineup_cambiante = ["Giselle", "Ningning"] # Una lista es mutable.

mi_coleccion = {"aespa", lineup_fijo} # Funciona porque la tupla es inmutable.

# --> Funciones útiles para colecciones <--

# len(): Me dice cuántos elementos únicos tengo en mi colección.
print(f"Tengo {len(photocards)} photocards únicas.")

# min() y max(): Me dan el primer y último elemento en orden alfabético (o el menor y mayor si son números).
# ¿Cuál es el primer miembro en orden alfabético de mi colección?
primer_miembro_alpha = min(photocards)
print(f"El primer miembro en orden alfabético es: {primer_miembro_alpha}")

# ¿Y el último?
ultimo_miembro_alpha = max(photocards)
print(f"El último miembro en orden alfabético es: {ultimo_miembro_alpha}")


# --> Frozenset: Una colección "congelada" <--

# Un 'frozenset' es como una tupla, pero para sets. Es una colección inmutable.
# Una vez que la creas, no puedes añadir ni quitar elementos.
# Es como la lista de canciones de un álbum una vez que ha sido publicado: es definitiva.
tracklist_definitivo = frozenset(["Case 143", "Chill", "Super Board"])
print("Tracklist definitivo del álbum:", tracklist_definitivo)

# Si intento añadir otra canción, Python me dará un error.
