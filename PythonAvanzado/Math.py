# --> Módulo Math: La geometría de un escenario de K-pop <--

# El módulo 'math' es como el equipo de ingenieros de escenario.
# Nos da herramientas precisas para todo tipo de cálculos matemáticos.
import math

# --> math.pi: La constante para escenarios circulares <--
# 'math.pi' nos da el valor exacto de Pi (π), esencial para cualquier cálculo con círculos.
print(f"El valor de Pi (π) para nuestros cálculos es: {math.pi}")

# --> math.sqrt(): Calculando la distancia de un fanchant <--
# 'math.sqrt()' calcula la raíz cuadrada de un número.
# Imaginemos que queremos saber a qué distancia se escucha un fanchant de 90,000 fans.
numero_de_fans = 90000
distancia_impacto = math.sqrt(numero_de_fans)
print(f"Un fanchant de {numero_de_fans} fans se escucha a una 'distancia de impacto' de: {distancia_impacto:.2f} metros.")


# --> math.pow() y math.ceil(): Calculando la capacidad del estadio <--
# 'math.pow(base, exponente)' eleva un número a una potencia.
# 'math.ceil()' redondea un número SIEMPRE hacia arriba al siguiente entero.

# Si un estadio tiene un radio de 80 metros, ¿cuál es su área? (Área = π * radio^2)
radio_estadio = 80
area_estadio = math.pi * math.pow(radio_estadio, 2)
print(f"\nEl área del estadio es de {area_estadio:.2f} metros cuadrados.")

# Si cada fan necesita 1.5 metros cuadrados, ¿cuántos asientos necesitamos?
asientos_necesarios = area_estadio / 1.5
print(f"Cálculo exacto de asientos: {asientos_necesarios}")

# No podemos tener medio asiento, así que redondeamos hacia arriba con math.ceil().
asientos_totales = math.ceil(asientos_necesarios)
print(f"Total de asientos a instalar (redondeado hacia arriba): {asientos_totales}")


# --> math.floor(): Calculando el número de álbumes en una caja <--
# 'math.floor()' redondea SIEMPRE hacia abajo.
# Si en una caja caben 12.7 álbumes (por el espacio), en realidad solo podemos meter 12.
caben_en_caja = 12.7
albumes_por_caja = math.floor(caben_en_caja)
print(f"\nAunque el cálculo sea {caben_en_caja}, solo podemos meter {albumes_por_caja} álbumes por caja.")
