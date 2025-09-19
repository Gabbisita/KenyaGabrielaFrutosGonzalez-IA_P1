# --> Clases Abstractas: El "Contrato" del Trainee <--

# Una Clase Abstracta es como una plantilla o un "contrato" que define qué habilidades MÍNIMAS debe tener un idol para poder debutar.
# No puedes "debutar" (crear un objeto) de una plantilla de trainee, solo de un idol que ya cumplió con el contrato.

# Para crear este contrato, importamos ABC (Abstract Base Class) y abstractmethod.
from abc import ABC, abstractmethod

# --> La Clase Abstracta: El Contrato de la Agencia <--
# Esta clase 'Trainee' hereda de ABC para convertirse en una plantilla abstracta.
class Trainee(ABC):

    # El decorador @abstractmethod marca una habilidad como obligatoria.
    # Es una regla en el contrato que dice: "Para debutar, DEBES saber cómo presentarte".
    # El método se deja vacío con 'pass' porque la plantilla solo establece la regla, no cómo se cumple.
    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def mostrar_talento_principal(self):
        pass

# Si intento "debutar" a un trainee directamente desde la plantilla, Python me dará un error.
# No se puede crear un objeto de una clase abstracta.
# trainee_generico = Trainee() # TypeError: Can't instantiate abstract class.


# --> Las Clases Concretas: Idols que cumplen el contrato <--

# Para poder debutar (crear un objeto), una clase hija DEBE implementar TODOS los métodos abstractos.

# --> El Rapero: Cumple el contrato a su manera <--
class Rapero(Trainee):
    # Implementa el método obligatorio 'presentarse'.
    def presentarse(self):
        print("Yo! Soy el rapero, listo para romperla.")

    # Implementa el método obligatorio 'mostrar_talento_principal'.
    def mostrar_talento_principal(self):
        print("...haciendo un freestyle de rap a alta velocidad...")

# --> La Vocalista: Cumple el contrato con su propio estilo <--
class Vocalista(Trainee):
    # Implementa 'presentarse' a su manera.
    def presentarse(self):
        print("Hola a todos~ Soy la vocalista, espero que disfruten mi voz.")

    # Implementa 'mostrar_talento_principal' con su habilidad.
    def mostrar_talento_principal(self):
        print("...cantando una nota alta y sostenida...")


# --> ¿Qué pasa si un trainee no cumple el contrato? <--

# Esta clase 'BailarinIncompleto' hereda de Trainee, pero se "olvida" de implementar el método 'mostrar_talento_principal'.
class BailarinIncompleto(Trainee):
    def presentarse(self):
        print("Soy el bailarín, ¡miren mis movimientos!")
    # Falta el método mostrar_talento_principal()

# Si intento debutar a este trainee, Python me detendrá.
# ¡No ha cumplido todas las cláusulas del contrato!
# bailarin = BailarinIncompleto() # TypeError: Can't instantiate abstract class...


# --> ¡Debut exitoso! <--
# Como las clases Rapero y Vocalista sí cumplen con todo el contrato, puedo crear objetos de ellas sin problemas.
print("--> ¡Show de talentos de los nuevos idols! <--")
han = Rapero()
han.presentarse()
han.mostrar_talento_principal()

print("\n")

seungmin = Vocalista()
seungmin.presentarse()
seungmin.mostrar_talento_principal()
