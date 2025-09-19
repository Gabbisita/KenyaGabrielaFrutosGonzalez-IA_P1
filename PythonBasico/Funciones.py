# --> Funciones: Creando una Sub-Unidad de K-pop <--

# Una función es como crear una sub-unidad: un bloque de código reutilizable que realiza una tarea específica.
# La defines una vez y la puedes "llamar" (usar) cuantas veces quieras.

# --> Función sin parámetros: El saludo oficial del grupo <--
# Esta función no necesita información externa para funcionar.
def saludo_oficial_skz():
    print("Step out! We are Stray Kids!")

# Para ejecutarla, simplemente la llamo por su nombre.
print("Presentando al grupo:")
saludo_oficial_skz()


# --> Función con parámetros: Un saludo personalizado para el Fandom <--
# Los 'parámetros' son variables que la función necesita para trabajar.
# Es como darle el nombre del fan para que el saludo sea personal.
def saludo_personalizado(nombre_fan):
    print(f"¡Hola, {nombre_fan}! Gracias por tu apoyo.")

# Al llamar a la función, le paso los 'argumentos' (los valores reales).
saludo_personalizado("Maria")
saludo_personalizado("Carlos")


# --> Argumentos por posición vs. por nombre <--
# Por defecto, Python asigna los argumentos por el orden en que los escribes.
def crear_perfil(nombre, grupo):
    print(f"Idol: {nombre}, Grupo: {grupo}")

# Si los paso en el orden incorrecto, el resultado es erróneo.
crear_perfil("LE SSERAFIM", "Chaewon") # Salida incorrecta

# Para evitar esto, puedo usar argumentos por nombre (keyword arguments).
# Así, el orden no importa.
print("\nUsando argumentos por nombre:")
crear_perfil(grupo="LE SSERAFIM", nombre="Chaewon") # Salida correcta


# --> El valor de retorno (return): El resultado de una actividad <--

# Una función puede simplemente hacer algo (como imprimir un saludo) o puede 'retornar' un valor.
# 'return' es como el resultado de una sesión de composición: produce algo que puedo usar después.

# --> Función sin return: Solo actúa <--
# Esta función solo imprime el resultado, no lo devuelve.
def calcular_puntuacion_show(ventas, votos):
    print(f"Puntuación final: {ventas + votos}")

print("\nCalculando puntuación (sin return):")
resultado_show = calcular_puntuacion_show(5000, 4500)
print(f"El valor guardado en la variable es: {resultado_show}") # El valor es 'None' (nada).

# --> Función con return: Produce un resultado tangible <--
# Esta función devuelve el resultado para que pueda guardarlo y usarlo en otros cálculos.
def calcular_streams_totales(spotify, youtube):
    print("Calculando el total de streams...")
    return spotify + youtube

# Guardo el valor que la función me devuelve.
total_streams = calcular_streams_totales(100_000_000, 150_000_000)
print(f"Streams totales del comeback: {total_streams}")

# Ahora puedo usar ese resultado para otras cosas.
if total_streams > 200_000_000:
    print("¡Objetivo de streams superado! ¡Felicidades, Fandom!")

# Importante: Una vez que la función ejecuta 'return', se termina.
# Cualquier código después del 'return' dentro de la función no se ejecutará.
def cancion_terminada():
    return "Fin de la canción."
    print("Esta parte nunca se mostrará.")
