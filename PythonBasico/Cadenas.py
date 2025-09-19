# --> Concatenación de Strings: Uniendo el Fanchant <--

# Se definen dos variables de tipo string.
grupo = "Stray Kids"
lema = "Everywhere all around the world"

# El operador '+' une (concatena) dos strings. Se añade un espacio " " en medio.
frase_completa = grupo + " " + lema
print(frase_completa)


# --> Comillas dentro de Strings <--

# Para incluir comillas dobles dentro de un string, se puede definir el string con comillas simples.
print('El fanchant gritaba: "You make Stray Kids stay"')

# Para incluir comillas simples, se puede definir el string con comillas dobles.
print("El lightstick de ATEEZ se llama 'LIGHTINY'")

# Alternativamente, se puede "escapar" la comilla con una barra invertida (\).
print("El fanchant gritaba: \"You make Stray Kids stay\"")
print('El lightstick de ATEEZ se llama \'LIGHTINY\'')


# --> F-Strings: La forma moderna de incluir variables <--

# Se pide al usuario que introduzca el nombre de su bias.
bias = input("Introduce el nombre de tu bias:\n")

# Una f-string (la 'f' antes de las comillas) permite incrustar variables directamente dentro del texto.
# Es más legible que la concatenación con '+'.
print(f"¡Hola! Tu bias es {bias}, una gran elección.")

# Las f-strings también funcionan con números, evitando errores de tipo.
numero_miembros = 8
print(f"El grupo tiene {numero_miembros} miembros.")

# Se pueden realizar operaciones directamente dentro de las llaves {}.
miembros_activos = 7
miembros_totales = 8
print(f"Falta {miembros_totales - miembros_activos} miembro para que el grupo esté completo.")


# --> Métodos de String: Cambiando el estilo del texto <--

# Los métodos son funciones especiales que pertenecen a un objeto (en este caso, un string).

cancion = "god's menu"
# El método .capitalize() convierte el primer carácter del string a mayúscula.
print(cancion.capitalize())

titulo_album = "ODDINARY"
# El método .lower() convierte todos los caracteres a minúsculas.
print(titulo_album.lower())

fanchant = "jyp!"
# El método .upper() convierte todos los caracteres a mayúsculas.
print(fanchant.upper())

# Se pueden encadenar métodos. Aquí, se pide un nombre y se asegura que empiece con mayúscula.
nombre_idol = input("Escribe el nombre de un idol:\n")
print(f"El nombre capitalizado es: {nombre_idol.capitalize()}")
