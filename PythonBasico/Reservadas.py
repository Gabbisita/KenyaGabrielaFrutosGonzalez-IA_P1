# --> Reglas para nombrar variables: Las palabras reservadas <--

# En Python, hay ciertas palabras que tienen un significado especial para el lenguaje.
# Son como los nombres de los grupos de K-pop: son únicos y no puedes usarlos para otra cosa.
# Estas palabras se llaman "palabras reservadas" o "keywords".

# Si intentas usar una palabra reservada como nombre de variable, Python te dará un error.
# Por ejemplo, 'global' es una palabra reservada.
# Para evitar esto, podemos simplemente modificar el nombre.
variable_global = 10
print("Esto sí funciona:", variable_global)


# --> ¿Cómo saber cuáles son las palabras reservadas? <--

# Python nos proporciona una lista oficial de todas sus palabras reservadas.
# Podemos importarla usando el módulo 'keyword'.
import keyword

print(" Palabras Reservadas de Python (Keywords)")
print(keyword.kwlist)
print("---------------------------------------------")

# Como puedes ver en la lista, palabras como 'False', 'True', 'if', 'for', 'while', etc.,
# tienen un propósito específico y no pueden ser nombres de variables.


# --> Un caso especial: 'match' <--

# A partir de Python 3.10, 'match' se convirtió en una "palabra clave suave".
# Esto significa que, aunque forma parte de la nueva sintaxis 'match-case' (similar a un switch),
# Python todavía permite usarla como nombre de variable por retrocompatibilidad.

match = 10 # En versiones recientes de Python, esto es válido.
print("El valor de 'match' es:", match)

# Sin embargo, es una MUY BUENA PRÁCTICA evitar usar 'match' y otras palabras reservadas
# como nombres de variables para no generar confusión.
