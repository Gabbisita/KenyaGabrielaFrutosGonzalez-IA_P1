# --> Módulos: Agencias especializadas con herramientas únicas <--

# Un 'módulo' en Python es como una agencia de entretenimiento especializada (ej: una agencia de coreógrafos, de productores, etc.).
# Contiene un conjunto de herramientas (funciones, clases, variables) listas para ser usadas.
# Para usar estas herramientas, primero debo 'importar' el módulo.

# --> import <nombre_modulo> <--
# Esto es como contratar a la agencia completa. Tengo acceso a todas sus herramientas, pero debo usar el nombre de la agencia como prefijo.

import random # Importo la agencia 'random', especializada en aleatoriedad.

# Para usar una herramienta (función) de la agencia, uso: agencia.herramienta()
# Vamos a elegir al azar al miembro que hará el próximo dance break.
miembros = ["Felix", "Hyunjin", "Lee Know", "Bang Chan"]
elegido_para_dance_break = random.choice(miembros) # Usamos la herramienta 'choice' de la agencia 'random'.

print(f"¡El elegido para el dance break es: {elegido_para_dance_break}!")


# --> Formas de Importar: Contratando a los especialistas <--

# --> from <nombre_modulo> import <herramienta> <--
# Esto es como contratar a un especialista directamente, en lugar de a toda la agencia.
# Es más directo, ya que no necesito usar el nombre de la agencia cada vez.

from random import randint, choice # Contrato solo a los especialistas 'randint' y 'choice'.

# Ahora puedo usar las herramientas por su nombre, sin el prefijo 'random.'.
numero_de_comebacks_este_año = randint(2, 5) # Uso 'randint' directamente.
print(f"Este año, el grupo tendrá {numero_de_comebacks_este_año} comebacks.")


# --> from <nombre_modulo> import * <--
# ¡CUIDADO! Esto es como contratar a TODOS los especialistas de la agencia y dejarlos sueltos en tu estudio.
# Importa todo lo que contiene el módulo, lo que puede causar conflictos si una herramienta tiene el mismo nombre que una tuya.
# Generalmente, se considera una mala práctica.
# from random import *


# --> Alias: Poniendo apodos a las agencias y herramientas <--

# A veces, los nombres de las agencias (módulos) son muy largos. Podemos darles un 'alias' (un apodo) para que sea más fácil llamarlos.
# Esto es muy común en módulos de ciencia de datos como numpy o pandas.

import random as rd # A la agencia 'random' ahora la llamaré 'rd'.

# Ahora uso el apodo para acceder a sus herramientas.
numero_de_versiones_album = rd.randint(3, 6)
print(f"El nuevo álbum tendrá {numero_de_versiones_album} versiones diferentes.")

# También puedo ponerle un apodo a una herramienta específica.
from random import choice as elegir_miembro # A la herramienta 'choice' la llamaré 'elegir_miembro'.

ganador_del_juego = elegir_miembro(miembros)
print(f"El ganador del juego de hoy es: {ganador_del_juego}")


# --> ¿Dónde y cuándo importar? <--

# La convención es poner TODAS las importaciones al principio del archivo.
# Esto deja claro desde el inicio qué "agencias" y "herramientas" va a usar tu programa.

# import math
# import random
# from datetime import datetime
#
# # ... el resto de tu código aquí ...
