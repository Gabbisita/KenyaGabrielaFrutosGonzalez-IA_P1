# Descripción: La clase base para todos los artistas.

class Trainee:
    """La clase base para cualquier artista en la agencia."""
    rol = "Trainee"

    def __init__(self, nombre, agencia):
        self.nombre = nombre
        self.agencia = agencia

    def presentarse(self):
        """Método de presentación básico."""
        print(f"Hola, soy {self.nombre} de la agencia {self.agencia}.")
        print(f"Mi rol actual es: {self.rol}.")

