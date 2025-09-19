# --> Comentarios de una sola línea <--

# El '#' es para mis apuntes. Python no lo lee, pero a mí me sirve para entender el código.
# Es como el fanchant que me aprendo: no es la canción, pero me guía.
print("¡BLACKPINK in your area!") # Este comentario es para recordar que esta es la frase icónica de BLACKPINK.

# También puedo usar el '#' para desactivar código sin tener que borrarlo.
# Útil para pausar una parte del código y probar otra.
# print("Esta parte del código está en pausa.")
print("¡Ahora suena 'How You Like That'!")


# --> Comentarios multilínea <--

"""
Si necesito escribir una nota más larga, como la info de un grupo,
puedo usar tres comillas dobles. Así puedo escribir en varias líneas
sin poner '#' en cada una.

Grupo: LE SSERAFIM
Debut: 2022
Fandom: FEARNOT
"""

'''
También puedo usar tres comillas simples para lo mismo.
Funcionan igual que las dobles. Lo importante es ser consistente.
'''

# Los comentarios multilínea son perfectos para desactivar un bloque grande de código.
# Por ejemplo, si quiero saltarme una parte para probar el final.
print("Iniciando el conteo para el próximo comeback...")
for i in range(1, 4):
    print(f"D-{i}")

"""
# Este bloque de la cuenta regresiva no se va a ejecutar porque lo comenté.
print("¡Cuenta regresiva para el encore!")
for i in range(10, 0, -1):
    print(i)
"""


# --> Docstrings <--

# El docstring es un comentario multilínea especial que va justo después de definir una función o clase.
# Su objetivo es documentar qué hace mi código. Es como la descripción oficial de un álbum.
# Así, si vuelvo a ver esta función en el futuro, sabré exactamente para qué la hice.

def mostrar_miembros(grupo):
    """
    Esta función que creé sirve para imprimir los miembros de un grupo de K-pop.

    La idea es que me ayude a recordar cómo usarla, qué necesita (el 'grupo')
    y qué hace (imprimir los nombres).
    """
    if grupo == "TWICE":
        print("Nayeon, Jeongyeon, Momo, Sana, Jihyo, Mina, Dahyun, Chaeyoung, Tzuyu")
    elif grupo == "Stray Kids":
        print("Bang Chan, Lee Know, Changbin, Hyunjin, Han, Felix, Seungmin, I.N")
    else:
        print("Este grupo no está en mi base de datos.")

# Aquí estoy probando la función que acabo de documentar.
mostrar_miembros("TWICE")
