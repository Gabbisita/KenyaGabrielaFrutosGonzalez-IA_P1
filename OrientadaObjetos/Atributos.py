# --> Clases y Objetos: Gestionando la energía de un Idol en concierto <--

# 1. La Clase: El perfil de rendimiento de un Idol.
# Define las estadísticas base de un idol para un performance.
class IdolEnConcierto:
    """
    Molde para un idol durante un concierto.
    Define su energía, resistencia y la experiencia que gana.
    """
    # Atributos de la clase (valores iniciales)
    energia = 100  # Energía al empezar el concierto.
    resistencia = 80 # Resistencia para las coreografías.
    experiencia_ganada = 0

    # Método: La acción que ocurre si se queda sin energía.
    def fin_del_concierto(self):
        print("\n¡El concierto ha terminado! Gracias por venir, Fandom.")


# 2. La Instanciación: Un idol sube al escenario.
# Creamos un objeto 'idol_en_escenario' a partir de la clase.
idol_en_escenario = IdolEnConcierto()


# 3. El Concierto: El estado del idol cambia.
print(f"Energía del idol al inicio del concierto: {idol_en_escenario.energia}")

# Durante el concierto, el idol lo da todo y su energía baja.
# Modificamos el atributo de energía del objeto.
print("...el idol realiza una intensa coreografía y un high note...")
idol_en_escenario.energia = 0

# 4. Condición final: ¿Se acabó la energía?
# Comprobamos si la energía del idol ha llegado a cero.
if idol_en_escenario.energia == 0:
    # Si es así, llamamos al método para finalizar el show.
    idol_en_escenario.fin_del_concierto()

print(f"\nEnergía del idol al final del concierto: {idol_en_escenario.energia}")
