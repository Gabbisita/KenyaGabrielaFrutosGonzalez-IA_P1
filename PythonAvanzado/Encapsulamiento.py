# --> Encapsulamiento: Los secretos de un Idol <--

# El encapsulamiento es como los diferentes niveles de información que una agencia comparte sobre un idol.
# Algunos datos son públicos, otros son para el "círculo cercano" y otros son completamente privados.

class Idol:
    def __init__(self, nombre_artistico, nombre_real, fecha_nacimiento):
        # Atributo Público: Información que todos pueden saber.
        self.nombre_artistico = nombre_artistico

        # Atributo Protegido (_): Información para la "familia" (clases hijas).
        # Es una convención, una señal de "no toques esto desde fuera a menos que sepas lo que haces".
        self._nombre_real = nombre_real

        # Atributo Privado (__): Un secreto bien guardado por la agencia.
        # Python cambia el nombre internamente para que no sea accesible fácilmente desde fuera.
        self.__fecha_nacimiento = fecha_nacimiento

    # --> Métodos Públicos: La forma oficial de interactuar <--
    # Son la vía segura para acceder o modificar datos privados.

    # Getter: Un método para "obtener" un dato privado de forma segura.
    def obtener_fecha_nacimiento(self):
        # Dentro de la clase, sí podemos acceder al atributo privado.
        return self.__fecha_nacimiento

    # Setter: Un método para "establecer" o cambiar un dato privado con control.
    def actualizar_fecha_nacimiento(self, nueva_fecha):
        print("Actualizando información confidencial...")
        self.__fecha_nacimiento = nueva_fecha


# --> Creando nuestro Idol <--
felix = Idol("Felix", "Lee Yong-bok", "15 de Septiembre de 2000")


# --> Accediendo a los diferentes niveles de información <--

# 1. Atributo Público: Se puede acceder y modificar libremente.
print(f"Nombre artístico (público): {felix.nombre_artistico}")
felix.nombre_artistico = "Felix Lee" # Se puede cambiar directamente.
print(f"Nombre artístico modificado: {felix.nombre_artistico}")

# 2. Atributo Protegido: Técnicamente se puede acceder, pero la convención dice que no deberías.
# Es como si un fan se enterara del nombre real por una fuente no oficial.
print(f"\nNombre real (protegido): {felix._nombre_real}") # Funciona, pero no es la práctica recomendada.

# 3. Atributo Privado: No se puede acceder directamente.
# print(felix.__fecha_nacimiento) # AttributeError: 'Idol' object has no attribute '__fecha_nacimiento'
# Python le ha cambiado el nombre a '_Idol__fecha_nacimiento' para protegerlo.


# --> La forma correcta de manejar datos privados: Getters y Setters <--

# Para ver la fecha de nacimiento, usamos el método público (getter) que la agencia nos proporciona.
print("\n--> Usando Getters y Setters <--")
fecha = felix.obtener_fecha_nacimiento()
print(f"Fecha de nacimiento (obtenida con un getter): {fecha}")

# Para cambiarla, usamos el método público (setter).
felix.actualizar_fecha_nacimiento("15/09/2000")
print(f"Nueva fecha de nacimiento: {felix.obtener_fecha_nacimiento()}")
