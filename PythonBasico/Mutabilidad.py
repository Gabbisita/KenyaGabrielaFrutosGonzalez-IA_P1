# --> Mutabilidad: Listas vs Tuplas <--

# Una lista es 'mutable', como un setlist de concierto. Puedo cambiar una canción por otra.
setlist_concierto = ["God's Menu", "Maniac", "LALALALA"]
setlist_concierto[1] = "Super Bowl" # Se cambia "Maniac" por "Super Bowl".
print("Setlist actualizado (lista mutable):", setlist_concierto)

# Una tupla es 'inmutable', como la discografía oficial de un álbum. No se puede alterar.
tracklist_album = ("Venom", "Maniac", "Charmer")
# Si intento cambiar una canción del tracklist oficial, Python me dará un error.


# --> Inmutabilidad de los Strings <--

# Los strings (texto) también son inmutables, como el nombre de un grupo.
# Puedo acceder a cada letra por su índice.
grupo = "ITZY"
print(grupo[0]) # Imprime 'I'

# Pero no puedo cambiar una sola letra del nombre.
# grupo[0] = 'A' # TypeError: 'str' object does not support item assignment

# Lo que sí puedo hacer es reasignar la variable a un valor completamente nuevo.
# Es como si el grupo cambiara de nombre por completo (algo raro, pero posible).
nombre_fandom = "MIDZY"
nombre_fandom = "JYP Stan" # La variable ahora apunta a un nuevo string.
print("Nuevo valor de la variable:", nombre_fandom)


# --> ¿Qué significa ser "Subscriptable"? <--

# "Subscriptable" significa que puedo acceder a los elementos internos de un objeto usando corchetes [].
# Las listas, tuplas y strings son subscriptables.

# Puedo acceder a un miembro de la lista por su índice.
lineup = ["Karina", "Giselle", "Winter", "Ningning"]
print(lineup[2]) # Imprime "Winter"

# Un número entero (int) no es subscriptable. No tiene "elementos internos".
# Es como intentar buscar el segundo miembro de "8". No tiene sentido.


# --> ¿Qué es un "Hash"? Un identificador único <--

# Un objeto inmutable (como un string o una tupla) tiene un 'hash', que es como su huella digital única.
# Este valor no cambia mientras el objeto no cambie.
print("Hash de 'aespa':", hash("aespa"))
print("Hash de la tupla de debut:", hash(("Karina", "Winter")))

# Un objeto mutable (como una lista) no puede tener un hash, porque su contenido puede cambiar en cualquier momento.
# Si su contenido cambia, su "huella digital" también debería cambiar, y eso causa problemas.
