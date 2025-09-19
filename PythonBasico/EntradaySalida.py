# --> La función print(): Comunicados oficiales de la agencia <--

# La función print() muestra información en la consola.
# Se pueden pasar múltiples argumentos (texto, números, variables), y por defecto los separa con un espacio.
print("El grupo", "ITZY", "tiene", 5, "miembros.")

# El parámetro 'sep' de print() controla el separador entre los argumentos.
# Se puede cambiar el espacio por defecto por cualquier otro texto.
print("Miembros:", "Yeji", "Lia", "Ryujin", "Chaeryeong", "Yuna", sep=", ")


# --> La función input(): Interactuando con el Fandom <--

# La función input() detiene la ejecución y espera que el usuario escriba algo y presione Enter.
# El texto que el usuario introduce se guarda como una cadena de texto (string) en una variable.
bias_favorito = input("Por favor, introduce el nombre de tu bias: ")

# Se muestra un mensaje de saludo, concatenando el texto con el nombre del bias guardado.
print("¡Tu bias es " + bias_favorito + "! Una excelente elección.")

# Se puede añadir '\n' dentro del mensaje de input() para que el usuario escriba en la línea de abajo.
fandom_name = input("¿A qué fandom perteneces?\n")
print("¡Saludos, " + fandom_name + "!")


# --> El problema de input(): Todo es texto (String) <--

# La función input() siempre devuelve los datos como una cadena de texto (string).
# Se solicita el número de álbumes de dos grupos.
albumes_twice = input("Introduce el número de álbumes de TWICE: ")
albumes_itzy = input("Introduce el número de álbumes de ITZY: ")

# El operador '+' con dos strings no suma los números, sino que los une (concatena).
# Si el usuario introduce "15" y "8", el resultado será la cadena de texto "158".
total_albumes_texto = albumes_twice + albumes_itzy

# Se imprime el resultado de la concatenación de los dos strings.
print("Resultado de la concatenación (incorrecto):", total_albumes_texto)

# --> La solución: Convertir el texto a número <--

# Para poder sumar los valores numéricamente, se deben convertir los strings a números.
# La función int() convierte una cadena de texto en un número entero.
albumes_twice_num = int(albumes_twice)
albumes_itzy_num = int(albumes_itzy)

# Ahora el operador '+' realiza una suma aritmética porque las variables son de tipo numérico.
total_albumes_real = albumes_twice_num + albumes_itzy_num

# Se imprime el resultado correcto de la suma.
print("Suma total real de álbumes:", total_albumes_real)
