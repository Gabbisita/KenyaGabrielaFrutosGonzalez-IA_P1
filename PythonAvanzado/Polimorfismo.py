# --> Polimorfismo: La versatilidad de un Idol <--

# El 'polimorfismo' (del griego "muchas formas") es la capacidad de objetos de diferentes clases de responder al mismo mensaje (o función) de maneras específicas para cada uno.

# --> Polimorfismo con la función len() <--
# La función len() es un gran ejemplo. Sabe cómo "medir" diferentes tipos de objetos.
nombre_grupo = "LE SSERAFIM"
miembros_tupla = ("Chaewon", "Sakura", "Yunjin", "Kazuha", "Eunchae")
perfil_idol = {"nombre": "Kazuha", "rol": "Bailarina"}

# len() sabe qué hacer en cada caso:
print(f"El nombre '{nombre_grupo}' tiene {len(nombre_grupo)} caracteres.")
print(f"El grupo tiene {len(miembros_tupla)} miembros.")
print(f"El perfil del idol tiene {len(perfil_idol)} datos.")


# --> Polimorfismo con métodos de clase <--
# Ocurre cuando una clase hija 'sobrescribe' (redefine) un método que heredó de su clase padre.

class Artista:
    def presentarse(self):
        print("Soy un artista de K-pop.")

class Rapero(Artista):
    # El Rapero redefine el método presentarse() para darle su propio estilo.
    def presentarse(self):
        print("Yo, check the mic! Soy el rapero del grupo.")

class Vocalista(Artista):
    # La Vocalista también lo redefine, pero de una manera diferente.
    def presentarse(self):
        print("Hola a todos~ ¡Soy la vocalista principal!")

# Creamos un objeto de cada clase.
artista_base = Artista()
rapero_han = Rapero()
vocalista_seungmin = Vocalista()

# Una función puede trabajar con cualquier objeto que tenga el método .presentarse().
# No le importa de qué clase sea, solo que sepa cómo "presentarse".
def iniciar_presentaciones(idol):
    idol.presentarse()

print("\n--> ¡Que comiencen las presentaciones! <--")
iniciar_presentaciones(artista_base)
iniciar_presentaciones(rapero_han)
iniciar_presentaciones(vocalista_seungmin)


# --> Sobrecarga de Métodos (Simulada): Diferentes versiones de una habilidad <--

# Python no soporta la "sobrecarga de métodos" tradicional como otros lenguajes (definir el mismo método con diferentes parámetros).
# Si defines un método con el mismo nombre dos veces, el último siempre sobrescribe al anterior.

# def producir_cancion(instrumento_1, instrumento_2):
#     print("Produciendo una canción con dos instrumentos.")
#
# def producir_cancion(instrumento_1, instrumento_2, instrumento_3):
#     print("Produciendo una canción con tres instrumentos.")
#
# # Solo la última definición existiría.
# # producir_cancion("Bajo", "Batería") # TypeError: le falta un argumento.

# --> La solución en Python: Parámetros opcionales <--
# Simulamos la sobrecarga usando parámetros con valores por defecto (como None).

def producir_cancion(beat, melodia, bajo=None, efectos=None):
    print("\nIniciando producción...")
    if bajo is not None and efectos is not None:
        print(f"Creando una pista compleja con {beat}, {melodia}, {bajo} y {efectos}.")
    elif bajo is not None:
        print(f"Creando una pista con {beat}, {melodia} y la línea de {bajo}.")
    else:
        print(f"Creando un demo simple con {beat} y {melodia}.")

# Podemos llamar a la misma función con diferente número de "capas" (argumentos).
producir_cancion("Beat de trap", "Melodía de piano")
producir_cancion("Beat de trap", "Melodía de piano", bajo="Bajo 808")
producir_cancion("Beat de trap", "Melodía de piano", bajo="Bajo 808", efectos="Sonidos de sintetizador")
