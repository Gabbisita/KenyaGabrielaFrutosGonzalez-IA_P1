# --> Clases: El "molde" para crear Idols <--

# Una 'clase' es como un plano o un molde para crear objetos.
# En nuestro caso, vamos a crear un plano para definir qué es un "Idol" de K-pop.
# La clase define las características (atributos) y las acciones (métodos) que todos los idols tendrán.

class Idol:
    """
    Esta clase es el molde para crear objetos de tipo Idol.
    Cada idol creado a partir de esta clase tendrá estas características y podrá realizar estas acciones.
    """
    # --> Atributos de Clase <--
    # Son características generales que podrían ser comunes a todos los idols.
    agencia = "JYP Entertainment" # Por ejemplo, si todos los idols que creamos son de JYP.
    profesion = "Artista de K-pop"

    # --> Métodos de la Clase <--
    # Son las acciones que un idol puede realizar.
    # El parámetro 'self' es obligatorio y se refiere al objeto específico que está realizando la acción.
    def presentarse(self):
        # 'self' nos permite acceder a los atributos del objeto en el futuro.
        print(f"¡Hola! Soy un {self.profesion} de {self.agencia}.")

    def cantar(self):
        print("La la la~ ¡Estoy cantando mi parte de la canción!")

    def bailar(self):
        print("¡Ejecutando la coreografía con energía!")


# --> ¿Qué es un Objeto? <--

# Un 'objeto' es una instancia creada a partir de una clase.
# Si la clase `Idol` es el molde, un objeto sería un idol específico que creamos con ese molde.
# En Python, todo es un objeto, incluso los tipos de datos que ya conocemos.

# Por ejemplo, un string (texto) es un objeto de la clase 'str'.
titulo_cancion = "God's Menu"
print(f"El tipo de dato de '{titulo_cancion}' es: {type(titulo_cancion)}")

# Como es un objeto, tiene sus propios métodos, como .upper().
# Aquí, el objeto 'titulo_cancion' está usando su método 'upper'.
titulo_en_mayusculas = titulo_cancion.upper()
print(f"El título usando el método .upper() es: {titulo_en_mayusculas}")
