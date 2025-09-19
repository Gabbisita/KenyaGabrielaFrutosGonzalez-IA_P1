# --> Ámbito de Variables (Scope): Niveles de gestión en una agencia de K-pop <--

# Python tiene diferentes "ámbitos" o "niveles" donde una variable puede existir.
# Imagina que son como los diferentes niveles de gestión en una agencia de entretenimiento.

# --> 1. Ámbito Global: El nivel de la Agencia <--
# Una variable creada aquí es 'global'. Es como el nombre de la agencia, conocido en todo el "edificio".
agencia = "JYP Entertainment"
grupo_principal = "Stray Kids"

def presentar_agencia():
    # Esta función puede LEER la variable global 'agencia' sin problemas.
    print(f"Somos de la agencia {agencia}.")

print("--> Nivel Global (Agencia) <--")
presentar_agencia()
print(f"El grupo principal de la agencia es: {grupo_principal}")


# --> 2. Ámbito Local: El nivel de la Sub-Unidad (Función) <--
# Una variable creada DENTRO de una función es 'local'. Solo existe dentro de esa función.
# Es como el nombre de un proyecto secreto de una sub-unidad.

def proyecto_sub_unidad():
    nombre_proyecto = "3RACHA - Zone" # 'nombre_proyecto' es una variable local.
    print(f"Dentro de la función, el proyecto es: {nombre_proyecto}")

    # Python siempre prioriza la variable local si hay un conflicto de nombres.
    grupo_principal = "3RACHA" # Esta variable local "oculta" a la global con el mismo nombre.
    print(f"El grupo a cargo de este proyecto es: {grupo_principal}")

print("\n--- Nivel Local (Sub-Unidad) ---")
proyecto_sub_unidad()

# Intentar acceder a 'nombre_proyecto' desde fuera de la función dará un error.
# print(nombre_proyecto) # NameError: name 'nombre_proyecto' is not defined.

# La variable global 'grupo_principal' no fue afectada por la local.
print(f"Fuera de la función, el grupo principal sigue siendo: {grupo_principal}")


# --> 3. La palabra clave 'global': Modificando desde adentro <--
# Si una función necesita MODIFICAR una variable global, debe declararlo explícitamente.

def cambiar_nombre_agencia():
    global agencia # Aviso: "Voy a modificar la variable global 'agencia'".
    agencia = "Stray Kids Entertainment" # Ahora sí se modifica la variable global.
    print(f"Dentro de la función, la agencia ahora es: {agencia}")

print("\n--> Modificando el Nivel Global <--")
cambiar_nombre_agencia()
print(f"Después de la función, el nombre global de la agencia ha cambiado a: {agencia}")


# --> 4. Ámbito Encerrado (Nonlocal): Gestión entre funciones anidadas <--
# Ocurre cuando tienes una función dentro de otra.
# La función interna puede acceder a las variables de la función externa.

def manager_general():
    decision_manager = "Comeback en otoño" # Variable en el ámbito "encerrado".

    def lider_del_grupo():
        # La función interna puede LEER la variable de la función externa.
        print(f"  Líder: 'El manager ha decidido: {decision_manager}'")

        # Si quisiera MODIFICARLA, usaría 'nonlocal'.
        nonlocal decision_manager
        decision_manager = "Comeback en verano, ¡sorpresa!"
        print(f"  Líder: '¡Cambio de planes! Ahora el comeback es en: {decision_manager}'")

    print("Manager General: 'He tomado una decisión.'")
    lider_del_grupo()
    print(f"Manager General: 'La decisión final es: {decision_manager}'")

print("\n--> Nivel Encerrado (Nonlocal) <--")
manager_general()


# --> 5. Ámbito Incorporado (Built-in): Las herramientas de Python <--
# Es el nivel más alto. Contiene todas las funciones y excepciones que vienen con Python por defecto.
# Por ejemplo: print(), len(), str(), int(), etc.
# Siempre están disponibles, no necesitas importar nada para usarlas.

print("\n--> Nivel Incorporado (Built-in) <--")
print("La función 'print' y 'len' son parte del ámbito incorporado.")
print(f"La longitud de '{grupo_principal}' es {len(grupo_principal)}.")
