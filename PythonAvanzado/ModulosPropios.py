# --> Bloque 1 <--
# Este es el "módulo" que contiene las herramientas de producción.
# Lo definimos primero para que el "programa principal" pueda encontrarlo.

class TresRachaProducciones:
    """
    Esta clase actúa como nuestro módulo de producción.
    Agrupa todas las funciones relacionadas con la creación de música.
    """
    @staticmethod
    def crear_beat(genero, bpm):
        """
        Esta función simula la creación de un beat de una canción.
        Devuelve un string describiendo el beat producido.
        """
        print(f"-> [3RACHA Studio]: Produciendo un beat de {genero} a {bpm} BPM...")
        return f"Beat de {genero} a {bpm} BPM listo para usar."

    @staticmethod
    def escribir_letra(tema):
        """
        Simula la escritura de la letra para una canción.
        """
        print(f"-> [3RACHA Studio]: Escribiendo una letra sobre '{tema}'...")
        return f"Letra sobre '{tema}' finalizada."

# --> Bloque 2 <--

# En lugar de 'import 3racha_producciones', ya tenemos la clase definida arriba.
# Así que creamos una "instancia" de nuestro módulo de producción.
produccion = TresRachaProducciones()

print("--- [Agencia JYP]: ¡Iniciando preparativos para el comeback de Stray Kids! ---")

# 1. Pedimos un nuevo beat a la unidad de producción.
# La sintaxis es similar a la de un módulo: objeto.metodo()
print("\n[Agencia JYP]: Necesitamos un beat para el title track.")
nuevo_beat = produccion.crear_beat("EDM-Trap", 130)
print(f"[Agencia JYP]: ¡Producción de beat recibida! -> '{nuevo_beat}'")

# 2. Pedimos la letra para la canción.
print("\n[Agencia JYP]: Ahora necesitamos la letra.")
nueva_letra = produccion.escribir_letra("Superar las dificultades")
print(f"[Agencia JYP]: ¡Letra recibida! -> '{nueva_letra}'")

print("\n--- [Agencia JYP]: ¡Todo listo para grabar la nueva canción! ---")

# --- SALIDA QUE SE VERÁ EN LA CONSOLA ---
# --- [Agencia JYP]: ¡Iniciando preparativos para el comeback de Stray Kids! ---
#
# [Agencia JYP]: Necesitamos un beat para el title track.
# -> [3RACHA Studio]: Produciendo un beat de EDM-Trap a 130 BPM...
# [Agencia JYP]: ¡Producción de beat recibida! -> 'Beat de EDM-Trap a 130 BPM listo para usar.'
#
# [Agencia JYP]: Ahora necesitamos la letra.
# -> [3RACHA Studio]: Escribiendo una letra sobre 'Superar las dificultades'...
# [Agencia JYP]: ¡Letra recibida! -> 'Letra sobre 'Superar las dificultades' finalizada.'
#
# --- [Agencia JYP]: ¡Todo listo para grabar la nueva canción! ---
