# --> Operadores Aritméticos: Calculando el éxito de un grupo <--

# Podemos sumar los streams de diferentes plataformas para obtener el total.
# Es como sumar las ventas de álbumes en Corea, Japón y USA.
streams_spotify = 1_000_000
streams_youtube = 5_000_000
streams_apple_music = 500_000

total_streams = streams_spotify + streams_youtube + streams_apple_music
print(f"Total de streams del comeback: {total_streams}")


# --> Resta, Multiplicación y División <--

# Resta (-): Calcular cuántos miembros quedan si uno está en hiatus.
miembros_totales = 9
miembros_en_hiatus = 1
miembros_activos = miembros_totales - miembros_en_hiatus
print(f"Miembros activos promocionando: {miembros_activos}")

# Multiplicación (*): Calcular el costo total de las entradas para un concierto.
precio_entrada = 150
amigos_que_van = 4
costo_total = precio_entrada * amigos_que_van
print(f"Costo total de las entradas: ${costo_total}")

# División (/): Repartir las líneas de una canción entre los miembros.
duracion_cancion_segundos = 180
numero_miembros = 7
segundos_por_miembro = duracion_cancion_segundos / numero_miembros
# El resultado es un 'float' (número con decimales).
print(f"Segundos aproximados por miembro: {segundos_por_miembro:.2f}")


# --> Operadores Especiales: Módulo y División Entera <--

# Módulo (%): Sirve para saber el 'resto' de una división.
photocards_totales = 25
espacios_por_pagina = 9

paginas_completas = photocards_totales // espacios_por_pagina # División entera (//) nos da las páginas llenas.
photocards_sobrantes = photocards_totales % espacios_por_pagina # Módulo (%) nos da las que sobran para la última página.

print(f"Puedo llenar {paginas_completas} páginas completas.")
print(f"Y me sobran {photocards_sobrantes} photocards para la siguiente página.")


# --> Exponenciación (**): El crecimiento viral <--

# El operador (**) calcula la potencia.
# Imaginemos que cada fan le cuenta el nuevo comeback a otros 3 fans.
ronda_1 = 3 ** 1 # 3 personas lo saben
ronda_2 = 3 ** 2 # 9 personas lo saben
ronda_5 = 3 ** 5 # ¡243 personas ya lo saben!
print(f"Después de 5 rondas, ¡{ronda_5} personas conocen el comeback!")


# --> Jerarquía de Operaciones: La estrategia de un performance <--

# Python respeta el orden de las operaciones, igual que una coreografía tiene un orden estricto.
# Primero multiplicaciones/divisiones, luego sumas/restas.
puntuacion_show = 5000 + 1000 * 2 # Primero 1000*2, luego + 5000
print(f"Puntuación sin paréntesis: {puntuacion_show}")

# Los paréntesis cambian la prioridad, ¡como un dance break que se roba la atención!
puntuacion_con_dance_break = (5000 + 1000) * 2 # Primero (5000+1000), luego * 2
print(f"Puntuación con el efecto del dance break: {puntuacion_con_dance_break}")
