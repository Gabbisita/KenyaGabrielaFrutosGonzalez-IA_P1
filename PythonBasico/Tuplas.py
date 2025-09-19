# --> Tuplas: El 'line-up' de debut de un grupo <--

# Una tupla es como el line-up original de un grupo: una vez que se define, no se puede cambiar.
# Se crean con paréntesis () y, a diferencia de las listas, son 'inmutables'.
lineup_debut_bts = ("RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook")
print("El line-up de debut de BTS es fijo:", lineup_debut_bts)

# Puedo acceder a un miembro por su posición (índice), igual que en las listas.
lider = lineup_debut_bts[0] # El índice 0 es el primer elemento.
print(f"El líder del grupo es: {lider}")

# Si intento modificar la tupla, Python me dará un error.
# Es como intentar cambiar la historia: ¡el line-up de debut es sagrado!


# --> Métodos de las Tuplas: Contar y Encontrar <--

# Aunque no se pueden modificar, sí puedo buscar información dentro de ellas.

# .count(): Cuenta cuántas veces aparece un elemento.
# ¿Cuántos raperos principales hay en la 3RACHA? (Imaginemos una tupla de roles).
roles_3racha = ("Productor", "Rapero", "Rapero", "Rapero", "Vocalista")
conteo_raperos = roles_3racha.count("Rapero")
print(f"En 3RACHA hay {conteo_raperos} roles de rapero.")

# .index(): Me dice la posición de la primera aparición de un miembro.
# ¿En qué posición debutó Jimin?
posicion_jimin = lineup_debut_bts.index("Jimin")
print(f"Jimin fue el miembro número {posicion_jimin + 1} en ser revelado en esta lista.")


# --> Desempaquetado de Tuplas: Presentando a las sub-unidades <--

# El desempaquetado me permite asignar los valores de una tupla a variables individuales.
# Es como presentar a cada miembro de una sub-unidad.
vocal_line_aespa = ("Karina", "Winter", "Ningning")
vocal_1, vocal_2, vocal_3 = vocal_line_aespa

print(f"Vocalista principal: {vocal_1}")
print(f"Vocalista líder: {vocal_2}")
print(f"Maknae vocal: {vocal_3}")

# Si el número de variables no coincide con el de elementos, da error.
# No puedo presentar a 3 miembros si solo tengo 2 variables.
# lider, rapero = vocal_line_aespa # ValueError: too many values to unpack

# Para solucionar esto, puedo usar un asterisco (*) para agrupar el resto de miembros en una lista.
# Presento al líder y al rapero, y el resto va a un grupo llamado 'otros_miembros'.
lineup_completo = ("Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin", "I.N")
lider, rapero_principal, *otros_miembros = lineup_completo

print(f"Líder: {lider}")
print(f"Rapero Principal: {rapero_principal}")
print(f"Otros miembros del grupo: {otros_miembros}") # 'otros_miembros' es una lista.
