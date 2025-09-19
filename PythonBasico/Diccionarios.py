# --> Diccionarios: El perfil de un Idol <--

# Un diccionario es como la ficha de perfil de un idol: guarda información usando pares de 'clave' y 'valor'.
# La 'clave' es el dato que identifica (ej: "Nombre") y el 'valor' es la información asociada (ej: "Felix").
perfil_felix = {
    "nombre_real": "Lee Yong-bok",
    "nombre_artistico": "Felix",
    "grupo": "Stray Kids",
    "posicion": "Bailarín y Rapero",
    "año_nacimiento": 2000
}


# --> Acceder a la información del perfil <--

# Para obtener un dato, uso su 'clave' entre corchetes.
# ¿Cuál es la posición de Felix en el grupo?
posicion = perfil_felix["posicion"]
print(f"La posición de Felix es: {posicion}")


# --> Modificar y añadir datos al perfil <--

# Los diccionarios son 'mutables', así que puedo actualizar la información.
# Por ejemplo, si su posición principal cambia.
print(f"La posición original era: {perfil_felix['posicion']}")
perfil_felix["posicion"] = "Bailarín Principal, Rapero y Visual"
print(f"La posición actualizada es: {perfil_felix['posicion']}")

# También puedo añadir nuevos datos que no existían en el perfil.
# Añadimos su apodo oficial.
perfil_felix["apodo"] = "Haengbokkie (Sunshine)"
print("Perfil con el apodo añadido:")
print(perfil_felix)


# --> Eliminar datos del perfil <--

# Con 'del', puedo eliminar un par clave-valor específico.
# Eliminemos el año de nacimiento para mantener el misterio.
del perfil_felix["año_nacimiento"]
print("Perfil después de eliminar el año de nacimiento:")
print(perfil_felix)

# 'del' también puede eliminar el diccionario completo de la existencia.
# Después de esto, la variable 'perfil_felix' ya no existirá.
del perfil_felix
# print(perfil_felix) # Si intentara imprimirlo, daría un error porque ya no existe.
