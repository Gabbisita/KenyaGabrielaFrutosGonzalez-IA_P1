# --> El Parámetro 'self': La identidad de cada Idol <--

# 'self' es el primer parámetro obligatorio en casi todos los métodos de una clase.
# Representa a la instancia específica (al objeto) que está llamando al método.
# Es la forma que tiene un idol de referirse a sí mismo y a sus propias características.

class Idol:
    def __init__(self, nombre, grupo):
        # 'self' aquí se refiere al objeto que se está creando (ej: 'felix' o 'hyunjin').
        # Asigna el nombre y grupo a ESE objeto en particular.
        self.nombre = nombre
        self.grupo = grupo

    # --- Métodos de Instancia: Acciones individuales ---
    # Estos métodos necesitan 'self' para saber QUIÉN está realizando la acción.
    def presentarse(self):
        # Usa 'self.nombre' para acceder al nombre del idol específico que se está presentando.
        print(f"¡Hola! Soy {self.nombre} de {self.grupo}.")

    def firmar_autografos(self):
        print(f"{self.nombre} está firmando autógrafos para el fandom.")

    def hacer_aegyo(self):
        # Sin 'self', el método no sabría qué nombre mostrar.
        print(f"¡{self.nombre} está haciendo un aegyo adorable!")


# --> Creando nuestros Idols (Objetos) <--
felix = Idol("Felix", "Stray Kids")
hyunjin = Idol("Hyunjin", "Stray Kids")


# --> ¿Qué pasa cuando llamamos a un método? <--

# Cuando escribo `felix.presentarse()`, ocurren dos cosas en segundo plano:
# 1. Python llama al método `presentarse` de la clase `Idol`.
# 2. Automáticamente, pasa el propio objeto `felix` como el primer argumento, el `self`.

# Por eso, estas dos líneas de código son equivalentes:
print("--> Llamada normal (la que siempre usamos) <--")
felix.presentarse()

print("\n--> Llamada explícita (lo que Python hace por detrás) <--")
Idol.presentarse(felix) # Pasamos manualmente el objeto que actuará como 'self'.


# --> La importancia de 'self' para acceder a los atributos <--

# Dentro de un método, si quiero usar un atributo de ese objeto (como su nombre),
# DEBO usar `self.nombre_del_atributo`.

# Si no uso 'self', Python buscará una variable local llamada 'nombre', no el atributo del objeto,
# y dará un error porque no la encontrará.

print("\n--> ¡Idols en acción! <--")
# Cada idol usa sus propios datos gracias a 'self'.
felix.firmar_autografos()
hyunjin.hacer_aegyo()
