# --> Herencia: De Trainee a Idol Principal <--

# El problema: Tenemos dos clases, 'Trainee' y 'IdolPrincipal', que son muy parecidas.
# Ambas tienen nombre, agencia y un método para presentarse.
# Esto es código repetido y difícil de mantener.

# class Trainee:
#     estatus = "Trainee"
#     puede_hacer_comeback = False
#
#     def __init__(self, nombre, agencia):
#         self.nombre = nombre
#         self.agencia = agencia
#
#     def presentarse(self):
#         print(f"Hola, soy {self.nombre} de la agencia {self.agencia}.")
#
# class IdolPrincipal:
#     estatus = "Idol Principal"
#     puede_hacer_comeback = True
#
#     def __init__(self, nombre, agencia):
#         self.nombre = nombre
#         self.agencia = agencia
#
#     def presentarse(self):
#         print(f"Hola, soy {self.nombre} de la agencia {self.agencia}.")


# --> La solución con Herencia <--

# 1. Creamos una clase base (Padre) que contiene todo lo común.
class Trainee:
    """La clase base para cualquier artista en la agencia."""
    estatus = "Trainee"
    puede_hacer_comeback = False

    def __init__(self, nombre, agencia):
        self.nombre = nombre
        self.agencia = agencia

    def presentarse(self):
        print(f"Hola, soy {self.nombre} de la agencia {self.agencia}.")
        print(f"Mi estatus actual es: {self.estatus}.")


# 2. Creamos una clase hija que hereda de la clase padre.
# 'IdolPrincipal' hereda todos los atributos y métodos de 'Trainee'.
class IdolPrincipal(Trainee):
    """
    Esta clase hereda de Trainee, pero sobrescribe los atributos
    para reflejar su nuevo estatus como idol principal.
    """
    # Sobrescribimos los atributos de la clase padre para especializarlos.
    estatus = "Idol Principal"
    puede_hacer_comeback = True


# --> ¡Debut y Promoción! <--

# Creamos un objeto de la clase hija 'IdolPrincipal'.
# Nota: No necesitamos redefinir __init__ o presentarse(), ¡ya los heredó de Trainee!
felix = IdolPrincipal("Felix", "JYP Entertainment")

# Podemos usar el método heredado .presentarse()
print("--> Presentación del Idol Principal <--")
felix.presentarse()

# Y podemos acceder a sus atributos (los que heredó y los que sobrescribió).
print(f"\n¿Puede este idol hacer un comeback? {felix.puede_hacer_comeback}")

# Si creamos un Trainee, usará los atributos de la clase base.
nuevo_trainee = Trainee("Chris", "JYP Entertainment")
print("\n--> Presentación del nuevo Trainee <--")
nuevo_trainee.presentarse()
