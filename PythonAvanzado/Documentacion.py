# --> Documentación y Buenas Prácticas: El manual de producción de K-pop <--

# Escribir código que funcione es solo la mitad del trabajo.
# La otra mitad es escribirlo de forma que sea claro, legible y fácil de mantener.

# --> 1. Comentarios: Notas del productor <--

# Los comentarios explican el 'porqué' del código, no solo el 'qué'.

# Mal comentario (obvio):
# i += 1 # Incrementa i en 1

# Buen comentario (explica la intención):
# Se avanza al siguiente miembro para asignarle su línea en la canción.
# i += 1

# --> Comentarios especiales para organización <--

# BUG: El cálculo de streams falla si el número es negativo.
# for stream in streams_negativos: ...

# FIXME: Esta función es lenta. Debería usar un generador para procesar los lightsticks.
# def contar_lightsticks(lista_fans): ...

# TODO: Implementar la función para calcular las ganancias del tour.
# def calcular_ganancias_tour(): ...

# NOTE: Este algoritmo de mezcla es complejo pero muy eficiente. No tocar si no es necesario.
# def mezclar_pista_final(pistas): ...


# --> 2. Type Hinting: Especificando el "instrumento" correcto <--

# El 'type hinting' (pistas de tipo) es una forma de indicar qué tipo de dato se espera
# que reciba una función y qué tipo de dato se espera que devuelva.
# No cambia el comportamiento del código, pero lo hace mucho más claro y ayuda a los editores a detectar errores.

# Sin type hinting: ¿Qué es 'nombre'?, ¿qué devuelve la función?
# def crear_fanchant(nombre):
#     return f"¡{nombre.upper()}!"

# Con type hinting: Queda claro que espera un string y devuelve un string.
def crear_fanchant(nombre: str) -> str:
    """Crea un fanchant simple para un miembro del grupo."""
    return f"¡{nombre.upper()}!"

# Aunque son solo "pistas", ayudan a prevenir errores.
# Si le paso un número, mi editor podría advertirme, aunque el código falle en ejecución.
# crear_fanchant(123) # Error en ejecución, pero el type hint ya nos avisaba.


# --> 3. Docstrings: El manual de instrucciones de la función <--

# Un 'docstring' es un string que se coloca como primera línea de un módulo, clase o función.
# Su propósito es documentar qué hace, qué parámetros recibe y qué devuelve.
# Es el manual de usuario oficial de tu código.

def calcular_lineas_por_miembro(total_lineas: int, numero_miembros: int) -> float:
    """Calcula el promedio de líneas de canción por cada miembro.

    Esta función es esencial para asegurar una distribución justa de líneas
    en las producciones del grupo.

    Args:
        total_lineas (int): El número total de líneas en la letra de la canción.
        numero_miembros (int): El número de miembros que participarán en la canción.

    Returns:
        float: El promedio de líneas que le correspondería a cada miembro.
    """
    if numero_miembros == 0:
        return 0.0
    return total_lineas / numero_miembros

# --> ¿Cómo usar los Docstrings? <--

# La función help() integrada en Python muestra el docstring de forma legible.
# help(calcular_lineas_por_miembro)

# También puedes acceder a él directamente a través del atributo __doc__.
print("\n--- Documentación de la función 'calcular_lineas_por_miembro' ---")
print(calcular_lineas_por_miembro.__doc__)
