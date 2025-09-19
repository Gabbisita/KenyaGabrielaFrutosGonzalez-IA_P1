# --> Funciones Avanzadas: El estudio de producción de K-pop <--

# --> 1. Funciones y `return`: Componiendo la melodía <--
# Una función puede 'imprimir' una acción o 'retornar' un resultado.
# 'return' es clave para que el resultado de una función pueda ser usado por otra.

def componer_melodia(nota_1, nota_2):
    """Devuelve una melodía combinando dos notas."""
    return f"{nota_1} ~ {nota_2}"

melodia_principal = componer_melodia("Do", "Sol")
print(f"Melodía base compuesta: {melodia_principal}")


# --> 2. Argumentos por defecto: El beat estándar <--
# Se pueden asignar valores por defecto a los parámetros.
# Son útiles para opciones comunes que no siempre se quieren especificar.

def crear_beat(bpm, estilo="Trap"):
    """Crea un beat con un BPM y un estilo opcional."""
    return f"Beat de {estilo} a {bpm} BPM."

beat_estandar = crear_beat(120) # Usa el estilo por defecto "Trap".
beat_personalizado = crear_beat(90, estilo="Lo-fi")
print(f"Beat estándar: {beat_estandar}")
print(f"Beat personalizado: {beat_personalizado}")


# --> 3. *args: Añadiendo capas de sonido ilimitadas <--
# `*args` permite a una función aceptar un número variable de argumentos posicionales.
# Los agrupa en una tupla.

def mezclar_sonidos(*instrumentos):
    """Mezcla varios instrumentos en una pista."""
    print("\nMezclando los siguientes instrumentos:")
    for instrumento in instrumentos:
        print(f"- {instrumento}")
    return "Pista de instrumentos mezclada."

mezclar_sonidos("Batería", "Bajo", "Sintetizador", "Guitarra Eléctrica")


# --> 4. **kwargs: El panel de efectos especiales <--
# `**kwargs` permite pasar un número variable de argumentos con nombre (clave-valor).
# Los agrupa en un diccionario.

def aplicar_efectos_mastering(**efectos):
    """Aplica efectos de mastering a la canción final."""
    print("\nAplicando efectos de mastering:")
    for nombre_efecto, valor in efectos.items():
        print(f"- {nombre_efecto}: {valor}")
    return "Mastering completo."

aplicar_efectos_mastering(reverb="Hall", compresion="Alta", delay="Sutil")


# --> 5. Funciones Lambda: Ajustes rápidos en la mesa de mezclas <--
# Una función 'lambda' es una pequeña función anónima y de una sola línea.
# Perfecta para operaciones sencillas.

# Función lambda para duplicar el volumen de un track.
duplicar_volumen = lambda volumen_actual: volumen_actual * 2
volumen_bajo = 5
volumen_final = duplicar_volumen(volumen_bajo)
print(f"\nVolumen del bajo ajustado de {volumen_bajo} a {volumen_final}.")


# --> 6. Decoradores: El "efecto de estudio" que envuelve una función <--
# Un decorador es una función que modifica o "envuelve" a otra función.

def efecto_eco(funcion_vocal):
    """Decorador que añade un 'eco' antes y después de una pista vocal."""
    def wrapper(*args, **kwargs):
        print("(Eco: ...cantando...)")
        funcion_vocal(*args, **kwargs)
        print("(Eco: ...do...do...o...)")
    return wrapper

@efecto_eco
def grabar_coro(letra):
    """Graba la línea principal del coro."""
    print(f'"{letra}"')

print("\nGrabando el coro con efecto de eco:")
grabar_coro("You make Stray Kids stay!")


# --> 7. Generadores y `yield`: Creando un beat paso a paso <--
# Una función generadora usa `yield` para producir una secuencia de valores uno a uno.
# A diferencia de `return`, no termina la función, sino que la pausa, recordando su estado.
# Es ideal para secuencias largas, ya que no consume memoria creando toda la lista a la vez.

def generador_de_beat_808():
    """Genera los componentes de un beat de batería 808, uno por uno."""
    print("\n--- Generador de Beat 808 Activado ---")
    yield "Kick"
    print("...pausa...")
    yield "Snare"
    print("...pausa...")
    yield "Hi-hat"
    print("...pausa...")
    yield "Clap"

# Se crea el objeto generador.
beat_paso_a_paso = generador_de_beat_808()

# Se usa `next()` para obtener el siguiente valor, uno a la vez.
print(f"Paso 1: {next(beat_paso_a_paso)}")
print(f"Paso 2: {next(beat_paso_a_paso)}")
print("...haciendo otros arreglos en la canción...")
print(f"Paso 3: {next(beat_paso_a_paso)}")
print(f"Paso 4: {next(beat_paso_a_paso)}")
# Si llamo a next() de nuevo, daría un error StopIteration porque el generador ya no tiene más valores que producir.
