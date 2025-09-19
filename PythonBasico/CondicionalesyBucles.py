# --> Estructuras Condicionales: Tomando decisiones en la industria <--

# --> if/else: ¿El grupo es popular o no? <--
# El 'if' evalúa una condición. Si es True, ejecuta su bloque de código.
# El 'else' se ejecuta si la condición del 'if' es False.

streams_comeback = 150_000_000
if streams_comeback > 100_000_000:
    print("¡El comeback es un éxito masivo!")
else:
    print("El comeback tuvo un rendimiento modesto.")


# --> elif: Clasificando el nivel de un grupo <--
# 'elif' (else if) nos permite añadir más condiciones en cadena.
# Python las revisa en orden y ejecuta solo el primer bloque que sea True.

años_de_experiencia = 7
if años_de_experiencia < 1:
    print("Es un grupo 'Rookie' (novato).")
elif años_de_experiencia < 3:
    print("Es un grupo en crecimiento.")
elif años_de_experiencia < 7:
    print("Es un grupo 'Senior' (veterano).")
else:
    print("Es un grupo legendario de la industria.")


# --> Operador Ternario: Una decisión rápida <--
# Es una forma compacta de escribir un if/else en una sola línea.

edad_idol = 17
resultado = "Es mayor de edad en Corea" if edad_idol >= 19 else "Es menor de edad en Corea"
print(resultado)


# --> match/case: Identificando el rol de un idol (Python 3.10+) <--
# 'match' es como un 'if/elif/else' más potente y legible, ideal para comparar un valor con varios patrones.

rol = "Main Rapper"
match rol:
    case "Main Vocalist" | "Lead Vocalist":
        print("Se especializa en el canto.")
    case "Main Rapper" | "Lead Rapper":
        print("Se especializa en el rap.")
    case "Main Dancer" | "Lead Dancer":
        print("Se especializa en el baile.")
    case "Visual":
        print("Es el rostro del grupo.")
    case _: # El guion bajo actúa como el 'else', atrapa cualquier otro caso.
        print("Rol no especificado.")


# --> Bucles: Repitiendo el Fanchant <--

# --> for: Recorriendo una lista o un rango <--
# El bucle 'for' itera sobre los elementos de una secuencia (lista, tupla, string, etc.).

miembros_aespa = ["Karina", "Giselle", "Winter", "Ningning"]
print("--- Fanchant de aespa ---")
for miembro in miembros_aespa:
    print(f"¡{miembro}!")

# También es común usarlo con range() para repetir una acción un número de veces.
print("\n--- Contando hasta el comeback ---")
for i in range(1, 4): # Itera desde 1 hasta 2 (el 3 no se incluye).
    print(f"D-{i}...")
print("¡Comeback!")


# --> while: Practicando hasta que salga perfecto <--
# El bucle 'while' se repite mientras una condición sea True.

horas_de_practica = 0
while horas_de_practica < 5:
    print(f"Hora {horas_de_practica + 1}: ¡Practicando la coreografía!")
    horas_de_practica += 1 # Es crucial incrementar el contador para no crear un bucle infinito.
print("¡La coreografía está perfecta!")


# --> Controlando los Bucles: Pausas y Saltos en el Concierto <--

# --> continue: Saltarse una canción del setlist <--
# 'continue' salta la iteración actual y pasa a la siguiente.

setlist = ["Maniac", "God's Menu (Ballad Ver.)", "LALALALA"]
print("\n--- Setlist del concierto ---")
for cancion in setlist:
    if "(Ballad Ver.)" in cancion:
        print("(Nos saltamos la balada para mantener la energía alta)")
        continue # Salta esta canción y sigue con la próxima.
    print(f"¡Ahora suena: {cancion}!")


# --> break: Terminar el concierto antes de tiempo <--
# 'break' rompe y finaliza el bucle por completo.

print("\n--- Encore ---")
for cancion_encore in ["Youtiful", "Star Lost", "Mixtape: OH"]:
    if cancion_encore == "Star Lost":
        print("¡Problemas técnicos! El concierto debe terminar aquí.")
        break # El bucle se detiene por completo.
    print(f"Canción del encore: {cancion_encore}")


# --> Bonus: Recorriendo un Diccionario <--
# Para iterar sobre un diccionario, se usa el método .items(), que nos da la clave y el valor en cada paso.

perfil_idol = {"Grupo": "LE SSERAFIM", "Nombre": "Chaewon", "Rol": "Líder"}
print("\n--- Perfil del Idol ---")
for clave, valor in perfil_idol.items():
    print(f"- {clave}: {valor}")
