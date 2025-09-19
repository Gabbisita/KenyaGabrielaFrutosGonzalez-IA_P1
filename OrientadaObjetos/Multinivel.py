# --> Herencia Multinivel: La jerarquía de una agencia de K-pop <--

# 1. La Clase Base: El punto de partida de todo artista.
class Trainee:
    """La clase base para cualquier artista en la agencia."""
    rol = "Trainee"

    def __init__(self, nombre, agencia):
        # Atributos que todo artista, sin importar su nivel, tendrá.
        self.nombre = nombre
        self.agencia = agencia

    def presentarse(self):
        print(f"Hola, soy {self.nombre} de la agencia {self.agencia}.")


# 2. Herencia Nivel 1: El Idol que ha debutado.
# 'IdolDebutado' hereda de 'Trainee'. Es un Trainee, pero con más responsabilidades y atributos.
class IdolDebutado(Trainee):
    """Un Trainee que ha debutado. Hereda de Trainee y añade nuevas características."""
    rol = "Idol" # Sobrescribe el rol.

    def __init__(self, nombre, agencia, grupo, cancion_debut):
        # Primero, llamamos al constructor de la clase padre (Trainee) con super()
        # para que se encargue de inicializar 'nombre' y 'agencia'.
        # Así no repetimos código.
        super().__init__(nombre, agencia)

        # Ahora, añadimos los nuevos atributos que solo un Idol Debutado tiene.
        self.grupo = grupo
        self.cancion_debut = cancion_debut

    def promocionar(self):
        print(f"¡{self.nombre} está promocionando la canción '{self.cancion_debut}' con el grupo {self.grupo}!")


# 3. Herencia Nivel 2: El Líder del Grupo.
# 'LiderDeGrupo' hereda de 'IdolDebutado'. Es un Idol, pero con la responsabilidad adicional de liderar.
class LiderDeGrupo(IdolDebutado):
    """Un Idol Debutado con el rol de líder. Hereda de IdolDebutado."""
    rol = "Líder de Grupo" # Vuelve a sobrescribir el rol para ser más específico.

    # No necesita su propio __init__ porque no añade nuevos atributos.
    # Usará directamente el __init__ de su padre, 'IdolDebutado'.

    # Añade un método exclusivo para los líderes.
    def dar_discurso_de_aceptacion(self):
        print(f"Como líder de {self.grupo}, quiero agradecer a nuestro fandom por este premio. ¡Gracias!")


# --> Creando la jerarquía de artistas <--

# Creamos un objeto de la clase más alta en la jerarquía.
bang_chan = LiderDeGrupo("Bang Chan", "JYP", "Stray Kids", "Hellevator")

print("--> Perfil del Líder del Grupo <--")
# Puede usar métodos de todas las clases de las que hereda.
bang_chan.presentarse()  # Método heredado de Trainee.
bang_chan.promocionar()  # Método heredado de IdolDebutado.
bang_chan.dar_discurso_de_aceptacion() # Método propio.

# Y tiene acceso a todos los atributos definidos en la cadena de herencia.
print(f"\nNombre: {bang_chan.nombre}")
print(f"Grupo: {bang_chan.grupo}")
print(f"Rol final: {bang_chan.rol}")
