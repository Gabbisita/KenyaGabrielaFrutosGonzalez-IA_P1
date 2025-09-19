# --> Instanciación: "Produciendo" Idols a partir del molde <--

# La 'instanciación' es el proceso de crear un objeto a partir de una clase.
# Es como usar nuestro molde 'Idol' para crear un idol real y específico.
# Cada objeto es una 'instancia' independiente de la clase.

class Idol:
    # Atributos (características iniciales del molde)
    agencia = "JYP Entertainment"
    posicion = None # Aún no definida para un idol específico
    color_favorito = None

    # Métodos (acciones que pueden realizar)
    def presentarse(self):
        print(f"¡Hola! Somos de {self.agencia}")

    def mostrar_color(self):
        print(f"Mi color favorito es el {self.color_favorito}.")

# Ahora, creamos dos 'objetos' (instancias) de la clase Idol.
# Cada uno es un idol separado, aunque vengan del mismo molde.
felix = Idol()
hyunjin = Idol()

# Cada objeto ocupa un lugar diferente en la memoria, son individuos únicos.
print("Objeto 'felix':", felix)
print("Objeto 'hyunjin':", hyunjin)


# --> Atributos de Instancia: Personalizando a cada Idol <--

# Puedo acceder y modificar los atributos de cada objeto (idol) de forma individual.
# Esto no afecta a los otros objetos creados de la misma clase.

# Al principio, ambos tienen los valores por defecto del molde.
print(f"\nColor inicial de Felix: {felix.color_favorito}")
print(f"Color inicial de Hyunjin: {hyunjin.color_favorito}")

# Ahora, personalizamos el atributo 'color_favorito' para cada uno.
felix.color_favorito = "Azul"
hyunjin.color_favorito = "Negro"

print("\n--- Después de la personalización ---")
print(f"Nuevo color de Felix: {felix.color_favorito}")
print(f"Nuevo color de Hyunjin: {hyunjin.color_favorito}")

# También puedo añadir un atributo nuevo a un solo objeto sobre la marcha.
# Por ejemplo, la especialidad de Felix.
felix.especialidad = "Voz profunda"
print(f"Especialidad de Felix: {felix.especialidad}")
# Ojo: Hyunjin no tendrá este atributo, porque se lo añadimos solo a Felix.
# print(hyunjin.especialidad) # Esto daría un error.


# --> Llamando a los Métodos: ¡Idols en acción! <--

# Para que un idol realice una acción (llamar a un método), uso la sintaxis objeto.metodo().

print("\n--- ¡Los idols se presentan! ---")
# Felix usa su método 'presentarse'.
felix.presentarse()

# Hyunjin usa su método 'mostrar_color', que accederá a su propio color favorito.
hyunjin.mostrar_color()
