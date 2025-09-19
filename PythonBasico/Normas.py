# --> 1. Reglas para nombrar variables <--

# Recordatorio de las reglas básicas para los nombres de variables.
# No puedo empezar un nombre con un número ni usar caracteres extraños como '$' o '-'.

# Esto NO funciona y me dará error:
# 1er_comeback = "Fearless"
# $money = 1000            
# cancion-titulo = "Antifragile" # Python piensa que estoy intentando restar

# Pero sí puedo usar números en otras posiciones y guiones bajos.
# Estos nombres son totalmente válidos.
cancion_1 = "Perfect Night"
_bias_secreto = "Chaewon"


# --> 2. Sensibilidad a mayúsculas y minúsculas (Case-Sensitive) <--

# Debo recordar que Python distingue entre mayúsculas y minúsculas.
# Para Python, estas tres variables son completamente diferentes.
grupo = "Le Sserafim"
GRUPO = "IVE"
Grupo = "NewJeans"

# Si imprimo 'grupo', obtendré "Le Sserafim".
print(grupo)


# --> 3. Estilo recomendado: snake_case <--

# La convención en Python para nombres de variables y funciones es 'snake_case'.
# Consiste en usar minúsculas y separar las palabras con guiones bajos.
# Es más fácil de leer y es lo que la comunidad de Python prefiere.

# Ejemplos de nombres en snake_case:
nombre_completo = "Huh Yunjin"
fecha_debut = "2022-05-02"
cancion_con_mas_streams = "Antifragile"

# También es importante que los nombres sean descriptivos.
# Un nombre como 'a' no me dice nada, pero 'album_precio' sí.
a = 19.99                 # Mal nombre, no es descriptivo.
album_precio = 19.99      # Buen nombre, sé exactamente qué significa.


# --> 4. Convención para constantes: SCREAMING_SNAKE_CASE <--

# Para valores que no deberían cambiar, como el número de miembros originales o un valor matemático,
# la convención es usar mayúsculas y guiones bajos.
# Esto no impide que el valor cambie, pero es una señal visual para mí (y otros) de que no debería tocarlo.

MIEMBROS_ORIGINALES_LSF = 6
PI = 3.14159

# Podría cambiarlo, pero la convención me dice que no lo haga.
# MIEMBROS_ORIGINALES_LSF = 5 # Técnicamente posible, pero es una mala práctica.
