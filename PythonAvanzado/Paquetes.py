# --> Paquetes y Módulos: La estructura de una agencia de K-pop <--

# Un 'módulo' es un archivo .py con herramientas (funciones, clases).
# Un 'paquete' es una carpeta que contiene módulos. Es como un 'departamento' de la agencia.

# --> 1. Importando Módulos de un Paquete <--
# Se importa el departamento y el módulo específico que se necesita.
# Sintaxis: import nombre_paquete.nombre_modulo

# Se importa el módulo 'vocal_line' y 'dance_line' del paquete 'stray_kids'.
import stray_kids.vocal_line
import stray_kids.dance_line

# Se llama a la función 'cantar' del módulo 'vocal_line'.
stray_kids.vocal_line.cantar()
# Se llama a la función 'bailar' del módulo 'dance_line'.
stray_kids.dance_line.bailar()


# --> 2. Importando funciones específicas <--
# Es más directo importar solo la herramienta que se necesita.
# Sintaxis: from nombre_paquete.nombre_modulo import nombre_funcion

from stray_kids.rap_line import producir_beat

# Se usa la función directamente, sin necesidad de prefijos.
beat_nuevo = producir_beat("Trap")
print(beat_nuevo)


# --> 3. Usando Alias para acortar nombres <--
# Se usan alias ('as') para hacer el código más corto y legible.

import stray_kids.vocal_line as vocales
import stray_kids.dance_line as baile

vocales.cantar()
baile.bailar()


# --> 4. El archivo __init__.py: El recepcionista del departamento <--

# Cada paquete (carpeta) debe contener un archivo llamado __init__.py.
# Este archivo se ejecuta automáticamente cuando se importa el paquete.
# Sirve para inicializar el paquete o definir qué se puede importar.

# Si el __init__.py de 'stray_kids' está vacío, un 'import stray_kids' no da acceso directo a los módulos.
# import stray_kids
# stray_kids.vocal_line.cantar() # Esto daría un error.

# Para que funcione, el __init__.py puede importar los módulos él mismo.
# Contenido del archivo stray_kids/__init__.py:
# print("Departamento 'stray_kids' inicializado.")
# from . import vocal_line, dance_line, rap_line

# Con ese __init__.py, el siguiente código funcionaría:
# import stray_kids
# stray_kids.vocal_line.cantar()


# --> 5. La variable __name__: ¿Quién está en el escenario principal? <--

# __name__ es una variable especial que contiene el nombre del módulo actual.
# Si ejecutas un archivo directamente, su __name__ será "__main__".
# Si el archivo es importado, su __name__ será el nombre del módulo (ej: 'stray_kids.vocal_line').

# Esto permite tener código que solo se ejecuta cuando el archivo es el programa principal.
# Es como tener una sección de "ensayo" que no se muestra durante el "concierto" (cuando es importado).

# Ejemplo de código dentro de un módulo:
# def ensayar():
#     print("Ensayo de la coreografía...")
#
# if __name__ == "__main__":
#     # Este bloque solo se ejecuta si corro este archivo directamente.
#     print("Este es un ensayo privado, no una presentación oficial.")
#     ensayar()


# --> 6. La variable __all__: La lista de invitados VIP <--

# Dentro del __init__.py, se puede definir una lista llamada __all__.
# Esta lista especifica qué módulos se importarán cuando alguien use 'from nombre_paquete import *'.
# Es una forma de controlar la importación masiva y no exponer módulos internos.

# Contenido del archivo stray_kids/__init__.py:
# __all__ = ["vocal_line", "rap_line"]

# Código en el archivo principal:
# from stray_kids import *
# vocal_line.cantar() # Funciona, porque 'vocal_line' está en __all__.
# rap_line.producir_beat("Lo-fi") # Funciona.
# dance_line.bailar() # NameError: 'dance_line' no está en __all__, por lo que no se importó.
