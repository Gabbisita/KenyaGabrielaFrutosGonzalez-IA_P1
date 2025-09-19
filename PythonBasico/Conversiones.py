# --> Conversión de Tipos: La transformación de un Idol <--

# Python puede convertir un tipo de dato en otro, como un idol que pasa de rapero a vocalista.

# --> Conversión Implícita: La evolución natural <--
# Cuando mezclas tipos, Python elige el más "completo".
# Sumar un 'int' (premios en Corea) y un 'float' (puntuación de fans internacional) da como resultado un 'float'.
premios_corea = 10
puntuacion_fans = 98.5
puntuacion_total = premios_corea + puntuacion_fans

print(f"Puntuación total del comeback: {puntuacion_total}")
print(f"El tipo de dato del resultado es: {type(puntuacion_total)}") # Es <class 'float'>


# --> Conversión Explícita: El cambio de concepto forzado <--

# A veces, necesito forzar un cambio de tipo usando funciones como int(), float(), str(), etc.

# int(): Convertir a entero.
# Es como redondear la duración de una canción a minutos completos, se pierden los decimales.
duracion_exacta = 3.57 # 3 minutos y 57 segundos
duracion_en_minutos = int(duracion_exacta)
print(f"Duración redondeada a minutos: {duracion_en_minutos}")

# float(): Convertir a decimal.
# Útil para manejar puntuaciones que pueden no ser enteras.
votos_del_publico = float(input("Introduce los votos del público (puede tener decimales): "))
print(f"Votos registrados: {votos_del_publico}")

# str(): Convertir a texto.
# Para poder unir un número con un texto, primero lo convierto a string.
numero_de_album = 5
nombre_album = "The " + str(numero_de_album) + "th Mini Album"
print(nombre_album)

# bool(): Convertir a booleano (True o False).
# Cualquier número diferente de 0, o cualquier texto no vacío, se convierte en True.
# El 0 y el texto vacío "" se convierten en False.
hay_comeback_este_mes = bool(1) # 1 es como "sí"
print(f"¿Hay comeback este mes? {hay_comeback_este_mes}")

no_hay_comeback = bool(0) # 0 es como "no"
print(f"¿No hay comeback? {no_hay_comeback}")


# --> Caso práctico: Sumando los streams del fandom <--

# La función input() siempre devuelve texto (str).
streams_youtube_str = input("Introduce los streams de YouTube: ")
streams_spotify_str = input("Introduce los streams de Spotify: ")

# Si los sumo directamente, se concatenan como texto: "1000" + "500" = "1000500".
suma_incorrecta = streams_youtube_str + streams_spotify_str
print(f"Resultado incorrecto (concatenación): {suma_incorrecta}")

# La solución es convertir el texto a número (int o float) antes de sumar.
# Puedo hacerlo en un paso, anidando las funciones.
streams_totales = int(streams_youtube_str) + int(streams_spotify_str)
print(f"Suma total real de streams: {streams_totales}")


# --> Otras conversiones útiles <--

# hex(): Convierte un número a su representación hexadecimal.
# A veces los colores de los lightsticks se definen con códigos hexadecimales.
color_rojo_decimal = 255
color_rojo_hex = hex(color_rojo_decimal)
print(f"El valor decimal {color_rojo_decimal} es {color_rojo_hex} en hexadecimal.")
