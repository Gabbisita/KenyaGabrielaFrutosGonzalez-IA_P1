# --> El Método __init__: El "Debut" Oficial de un Idol <--

# Antes, para crear un idol, primero creábamos un objeto vacío y luego asignábamos sus datos uno por uno.
# Era como anunciar un idol sin nombre y luego ir dando su información a cuentagotas. ¡Poco eficiente!

# class Idol_Antiguo:
#     nombre = None
#     grupo = None
#
# # Proceso de debut antiguo:
# chaewon_antiguo = Idol_Antiguo()
# chaewon_antiguo.nombre = "Kim Chaewon"
# chaewon_antiguo.grupo = "LE SSERAFIM"


# --> La solución: El constructor __init__ <--

# El método `__init__` es un método especial llamado "constructor".
# Se ejecuta automáticamente CADA VEZ que creamos un nuevo objeto de la clase.
# Su función es inicializar los atributos del objeto desde el principio.
# ¡Es como presentar a un idol con toda su información básica desde el primer día de su debut!

class Idol:
    # Atributo de clase (compartido por todos los idols de esta clase)
    profesion = "Artista de K-pop"

    # El método constructor __init__
    def __init__(self, nombre, grupo, posicion, año_nacimiento):
        print(f"¡Debutando a un nuevo idol: {nombre}!")
        # Atributos de instancia (únicos para cada idol)
        self.nombre = nombre
        self.grupo = grupo
        self.posicion = posicion
        self.año_nacimiento = año_nacimiento
        self.apodo = "Aún sin apodo oficial" # Podemos tener atributos con valores por defecto

    # Métodos normales de la clase
    def presentarse(self):
        print(f"Hola, soy {self.nombre} de {self.grupo} y mi posición es {self.posicion}.")

    def cambiar_apodo(self, nuevo_apodo):
        self.apodo = nuevo_apodo
        print(f"¡Mi nuevo apodo es {self.apodo}!")


# --> "Debutando" idols con __init__ <--

# Ahora, al crear el objeto, DEBO pasarle los argumentos que __init__ necesita.
# Python los usará para construir el idol con sus datos desde el inicio.
chaewon = Idol("Kim Chaewon", "LE SSERAFIM", "Líder y Vocalista", 2000)
yunjin = Idol(nombre="Huh Yunjin", grupo="LE SSERAFIM", posicion="Vocalista", año_nacimiento=2001)

print("\n--- Perfiles de los idols debutados ---")
# Los atributos ya están asignados gracias a __init__
print(f"Perfil de Chaewon: {chaewon.nombre} ({chaewon.grupo})")
print(f"Perfil de Yunjin: {yunjin.nombre} ({yunjin.grupo})")

# Y los métodos funcionan con los datos inicializados.
yunjin.presentarse()

# Puedo seguir modificando los atributos después del debut.
chaewon.cambiar_apodo("Sammoo")
