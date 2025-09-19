# En Python, para declarar una variable y asignarle un valor, se usa el signo igual (=).
edad = 28.
print("La edad es:", edad)

# Python es de tipado dinámico, lo que significa que una misma variable puede cambiar de tipo.
# Aquí, 'miembro_favorito' primero es un número y luego un texto (string).
miembro_favorito = 4
miembro_favorito = "Felix"
print("Mi miembro favorito es:", miembro_favorito) # Imprimirá "Felix".

# El valor de una variable puede ser actualizado o "sobrescrito" cuantas veces sea necesario.
# Python siempre tomará en cuenta el último valor asignado.
comebacks_del_año = 3
comebacks_del_año = 5
comebacks_del_año = 6
print("Comebacks este año:", comebacks_del_año) # Imprimirá el último valor, que es 6.

# Para usar una variable, primero debe ser declarada.
# Si se intenta usar una variable que no existe, dara un error.
# print(lightstick) (ejemplo).

# Podemos inicializar una variable sin un valor específico usando 'None' o el tipo de dato vacío.
# 'int()' crea un número entero con valor 0. 'None' representa la ausencia de valor.
versiones_album = int()
print("Versiones del álbum:", versiones_album) # Imprimirá 0.

photocard_especial = None
print("Photocard especial:", photocard_especial) # Imprimirá None.

# La función print() se usa para mostrar valores o texto en la consola.
print("¡Hola, STAY!")

# Es posible asignar valores a múltiples variables en una sola línea.
# Debemos asegurararnos de que la cantidad de variables coincida con la cantidad de valores.
vocal_line, rap_line, dance_line = "Seungmin", "Changbin", "Lee Know"
print("Vocal:", vocal_line, "| Rap:", rap_line, "| Dance:", dance_line)

# Si intentamos asignar un solo valor a múltiples variables de esta forma, dará un error.
# hyung_line, maknae_line, aussie_line = 1 (ejemplo).

# Cada vez que se llama a la función print(), el resultado aparece en una nueva línea.
print("Primer premio ganado.")
print("Segundo premio ganado.")
