# --> Operadores de Comparación: ¿Quién gana el Music Show? <--

# Los operadores de comparación nos devuelven un resultado booleano: True o False.
# Son perfectos para comparar las puntuaciones de dos grupos.
puntuacion_skz = 9500
puntuacion_itzy = 9200

# == (Igual a): ¿Tuvieron la misma puntuación?
son_iguales = puntuacion_skz == puntuacion_itzy
print(f"¿Empataron en puntuación? {son_iguales}")

# != (Diferente de): ¿Tuvieron puntuaciones distintas?
son_diferentes = puntuacion_skz != puntuacion_itzy
print(f"¿Tuvieron puntuaciones diferentes? {son_diferentes}")

# > (Mayor que): ¿Stray Kids tuvo más puntos que ITZY?
skz_gano = puntuacion_skz > puntuacion_itzy
print(f"¿Stray Kids tuvo una puntuación mayor? {skz_gano}")

# < (Menor que): ¿La puntuación de ITZY fue menor?
itzy_menor_puntuacion = puntuacion_itzy < puntuacion_skz
print(f"¿ITZY tuvo una puntuación menor? {itzy_menor_puntuacion}")

# >= (Mayor o igual que): ¿La puntuación de SKZ fue al menos tan alta como la de ITZY?
skz_al_menos_igual = puntuacion_skz >= puntuacion_itzy
print(f"¿La puntuación de SKZ fue mayor o igual? {skz_al_menos_igual}")


# --> Operadores Lógicos: Analizando las condiciones para un premio <--

# Los operadores lógicos nos permiten combinar varias comparaciones.

# 'and': Todas las condiciones deben ser True para que el resultado sea True.
# Para ganar el "Daesang" (Gran Premio), se necesita una alta venta de álbumes Y un alto número de streams.
ventas_albumes_altas = True
streams_altos = True
gana_daesang = ventas_albumes_altas and streams_altos
print(f"¿El grupo gana el Daesang? {gana_daesang}")

# Si una de las dos condiciones falla, el resultado es False.
ventas_albumes_altas = True
streams_bajos = False
no_gana_daesang = ventas_albumes_altas and streams_bajos
print(f"¿Gana si los streams son bajos? {no_gana_daesang}")


# 'or': Basta con que una de las condiciones sea True para que el resultado sea True.
# Para ser nominado a "Rookie del Año", necesitas buenas ventas O buena popularidad en redes.
buenas_ventas = False
alta_popularidad_redes = True
es_nominado = buenas_ventas or alta_popularidad_redes
print(f"¿El grupo es nominado a Rookie del Año? {es_nominado}")


# 'not': Invierte el resultado de una expresión booleana. Si es True, la convierte en False, y viceversa.
# Es como preguntar lo contrario.
es_el_lider = True
no_es_el_lider = not es_el_lider
print(f"¿No es el líder del grupo? {no_es_el_lider}")


# --> Combinando todo: La estrategia completa <--
# ¿El grupo gana un premio si (las ventas son mayores a 500k Y los streams son mayores a 100M) O si (el fandom votó masivamente)?
ventas = 600_000
streams = 150_000_000
fandom_voto_masivamente = False

condicion_final = (ventas > 500_000 and streams > 100_000_000) or fandom_voto_masivamente
print(f"¿Se cumplen las condiciones para ganar el premio? {condicion_final}")
