# --> Herencia: La familia de Artistas de K-pop <--

# La herencia nos permite crear una clase nueva que "hereda" todos los atributos y métodos de una clase existente.
# Es como tener una clase base 'Artista' y luego clases más específicas como 'Rapero' o 'Vocalista' que son, en esencia, tipos de artistas.

# --> La Clase Padre (Superclase): El Artista base <--
# Esta es nuestra clase principal. Define lo que todo artista de K-pop es y puede hacer.
class Artista:
    def __init__(self, nombre, agencia):
        self.nombre = nombre
        self.agencia = agencia
        self.rol = "Artista"

    def presentarse(self):
        print(f"Hola, soy {self.nombre} de la agencia {self.agencia}. Mi rol es: {self.rol}.")


# --> La Clase Hija (Subclase): El Rapero especializado <--
# La clase 'Rapero' hereda de 'Artista'. Se especifica poniendo el nombre de la clase padre entre paréntesis.
# Un Rapero ES UN Artista, pero con un rol más específico.
class Rapero(Artista):
    # Usamos __init__ para especializar a nuestro rapero.
    def __init__(self, nombre, agencia):
        # 'super()' es una llamada a la clase padre (Artista).
        # Le decimos: "Oye, Artista, ejecuta TU propio __init__ con estos datos".
        # Así, el rapero obtiene los atributos 'nombre' y 'agencia' definidos en el padre.
        # Le pasamos el rol específico "Rapero" para que se inicialice correctamente.
        super().__init__(nombre, agencia)
        self.rol = "Rapero" # Sobrescribimos el rol general con uno específico.

    # Además, puede tener sus propios métodos exclusivos.
    def hacer_freestyle(self):
        print(f"¡{self.nombre} está improvisando un rap increíble!")


# --> Otra Clase Hija: La Vocalista especializada <--
class Vocalista(Artista):
    def __init__(self, nombre, agencia):
        # De nuevo, llamamos al constructor del padre para que haga el trabajo base.
        super().__init__(nombre, agencia)
        self.rol = "Vocalista" # Especializamos el rol.

    # Método exclusivo de los vocalistas.
    def cantar_nota_alta(self):
        print(f"¡{self.nombre} acaba de alcanzar una nota altísima!")


# --> Creando nuestra familia de artistas <--

# Un artista genérico.
idol_generico = Artista("Lee Know", "JYP")

# Un rapero, que hereda de Artista.
han = Rapero("Han", "JYP")

# Una vocalista, que también hereda de Artista.
seungmin = Vocalista("Seungmin", "JYP")


# --> ¡Todos en acción! <--
print("--> Presentaciones <--")
# Todos pueden usar el método .presentarse() porque lo heredaron de la clase Artista.
idol_generico.presentarse()
han.presentarse()
seungmin.presentarse()

print("\n--> Habilidades Especiales <--")
# Solo los objetos de las clases específicas pueden usar sus métodos exclusivos.
han.hacer_freestyle()
seungmin.cantar_nota_alta()
# idol_generico.hacer_freestyle() # Esto daría un error, un Artista genérico no tiene este método.
