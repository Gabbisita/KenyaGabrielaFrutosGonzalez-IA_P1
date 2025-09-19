# --> Manejo de Errores: El Manager de Crisis de un Comeback <--

# En la producción de un comeback, pueden ocurrir muchos imprevistos (errores).
# Un buen manager (programador) sabe cómo anticiparlos y manejarlos para que el show continúe.

# --> 1. Tipos de Errores Comunes en la Producción <--

# - NameError: Intentar usar un idol que no ha sido anunciado.
#   print(idol_secreto) # NameError: name 'idol_secreto' is not defined.

# - TypeError: Intentar mezclar cosas incompatibles, como sumar la letra de una canción con el número de premios.
#   resultado = "LALALALA" + 5 # TypeError: can only concatenate str (not "int") to str.

# - IndexError: Intentar acceder a un miembro del grupo que no existe en esa posición.
#   miembros = ["Felix", "Hyunjin"]
#   print(miembros[2]) # IndexError: list index out of range.

# - KeyError: Pedir un dato del perfil de un idol usando una clave que no existe.
#   perfil = {"nombre": "Han"}
#   print(perfil["edad"]) # KeyError: 'edad'.

# - ZeroDivisionError: Intentar repartir las líneas de una canción entre 0 miembros.
#   lineas_totales = 120
#   reparto = lineas_totales / 0 # ZeroDivisionError: division by zero.

# - IndentationError: Un error en la coreografía del código. La indentación es crucial en Python.
#   if True:
#   print("Indentación incorrecta") # IndentationError.


# --> 2. El Bloque `try...except`: El Plan de Contingencia <--

# El bloque `try...except` es nuestro plan de contingencia.
# `try`: Intenta ejecutar este código, que podría fallar.
# `except`: Si ocurre un error específico, en lugar de detener el programa, ejecuta este otro código.
# `finally`: Este bloque se ejecuta SIEMPRE, haya habido un error o no. Es para limpiar o cerrar recursos.

def repartir_photocards(total_cards, numero_de_fans):
    """Reparte photocards entre los fans y maneja posibles errores."""
    print("\n--> Iniciando reparto de photocards <--")
    try:
        # Intenta hacer el reparto.
        cards_por_fan = total_cards / numero_de_fans
        print(f"Cada fan recibe {cards_por_fan:.1f} photocards.")
    except ZeroDivisionError:
        # Se ejecuta si 'numero_de_fans' es 0.
        print("¡Error! No se puede repartir entre cero fans.")
    except TypeError:
        # Se ejecuta si los datos no son números.
        print("¡Error! Los datos deben ser numéricos.")
    except Exception as e:
        # Un 'except' genérico que atrapa cualquier otro tipo de error.
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        # Se ejecuta siempre, para confirmar que el proceso terminó.
        print("--> Reparto finalizado <--")

# Casos de prueba:
repartir_photocards(1000, 50)  # Caso exitoso.
repartir_photocards(1000, 0)   # Provoca ZeroDivisionError.
repartir_photocards(1000, "diez") # Provoca TypeError.


# --> 3. Validando la Entrada del Fandom <--
# Es crucial validar los datos que introduce el usuario para evitar errores.

# Se pide la edad para entrar a un concierto. El bucle no se detendrá hasta que se introduzca un número válido.
while True:
    try:
        edad_fan = int(input("\nIntroduce tu edad para verificar tu entrada al concierto: "))
        break # Si la conversión a 'int' funciona, se rompe el bucle.
    except ValueError:
        # Si el usuario escribe texto en lugar de un número, se ejecuta esto.
        print("Por favor, introduce un número válido para la edad.")

print(f"Edad verificada: {edad_fan} años. ¡Bienvenido al concierto!")


# --> 4. `assert`: Verificaciones internas del Staff <--
# `assert` comprueba si una condición es verdadera. Si no lo es, detiene el programa con un AssertionError.
# Es una herramienta de depuración para asegurar que el estado interno del programa es el correcto. No es para errores de usuario.

def programar_comeback(mes):
    """Programa un comeback, pero solo en meses válidos."""
    assert 1 <= mes <= 12, "Error de planificación: El mes debe estar entre 1 y 12."
    print(f"Comeback programado para el mes {mes}.")

# programar_comeback(15) # AssertionError: Error de planificación...


# --> 5. Creando Excepciones Personalizadas: Reglas de la Agencia <--
# Podemos crear nuestros propios tipos de error para situaciones específicas de nuestro programa.

class ReglaDeAgenciaError(Exception):
    """Excepción personalizada para cuando no se cumplen las reglas de la agencia."""
    pass

def aceptar_trainee(edad):
    """Acepta un trainee solo si cumple con el requisito de edad."""
    if not 15 <= edad <= 22:
        # Lanzamos nuestro propio error si no se cumple la regla.
        raise ReglaDeAgenciaError(f"La edad {edad} está fuera del rango permitido para trainees (15-22).")
    else:
        print(f"Trainee de {edad} años aceptado.")

try:
    aceptar_trainee(14)
except ReglaDeAgenciaError as e:
    print(f"No se pudo aceptar al trainee. Motivo: {e}")
