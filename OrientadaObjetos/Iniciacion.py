# --> Clases y Objetos: El molde y el Idol producido <--

# 1. La Clase: El "molde" para crear idols.
# Define la estructura y las habilidades básicas que todos los idols de este tipo tendrán.
class Idol:
    """
    Este es el molde (clase) para nuestros idols.
    Por ahora, es un molde simple sin características específicas.
    """
    pass # 'pass' se usa como un marcador de posición para un bloque de código vacío.


# 2. La Instanciación: El proceso de "producir" un idol.
# Aquí, usamos el molde 'Idol' para crear un objeto real y tangible.
# Este objeto es una 'instancia' de la clase Idol.

print("Usando el molde 'Idol' para producir a nuestro primer artista...")
felix = Idol()


# 3. El Objeto: ¡Nuestro idol ha sido creado!
# 'felix' es ahora un objeto de la clase Idol. Es un individuo único.
print(f"¡Producción exitosa! Se ha creado el objeto: {felix}")
print(f"El tipo de nuestro nuevo artista es: {type(felix)}")
