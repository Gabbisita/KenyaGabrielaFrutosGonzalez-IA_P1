# --> PIP y Entornos Virtuales: Equipando el estudio de producción <--

# 'pip' es el manager de equipamiento de Python. Es la herramienta que usamos para instalar,
# actualizar y desinstalar "paquetes" o "librerías" de terceros, que son como
# sintetizadores, mesas de mezclas o software especializado que no vienen de serie con Python.

# --> Comandos básicos de PIP (para usar en la terminal) <--

# 1. `pip install <nombre_paquete>`
# El comando para instalar nuevo equipamiento.
# Ejemplo: Vamos a instalar 'numpy', una potente calculadora para manejar datos numéricos.
# > pip install numpy
# (Salida: Successfully installed numpy-X.X.X)

# 2. `pip freeze`
# Muestra una lista de todo el equipamiento (paquetes) que tenemos instalado en nuestro estudio.
# Es como hacer un inventario.
# > pip freeze
# (Salida: numpy==1.26.4)

# 3. `pip install <nombre_paquete> --upgrade`
# Actualiza un equipo a su última versión.
# > pip install numpy --upgrade

# 4. `pip uninstall <nombre_paquete>`
# Desinstala o elimina un equipo que ya no necesitamos.
# > pip uninstall numpy


# --> Entornos Virtuales (venv): Creando un estudio de grabación privado <--

# Imagina que Stray Kids y ITZY trabajan en la misma agencia (tu ordenador),
# pero cada grupo necesita una configuración de estudio diferente para su comeback.
# No quieres que los sintetizadores de SKZ interfieran con los de ITZY.

# Un 'entorno virtual' es un estudio de grabación aislado y privado para un proyecto específico.
# Cada entorno tiene su propio equipamiento (paquetes) y no afecta a los demás.

# --> Comandos de venv (para usar en la terminal) <--

# 1. `python -m venv <nombre_del_entorno>`
# Crea una nueva carpeta que será nuestro estudio privado.
# Vamos a crear un estudio para el comeback de Stray Kids.
# > python -m venv estudio_skz

# 2. `source estudio_skz/bin/activate` (en Mac/Linux)
#    `estudio_skz\Scripts\activate` (en Windows)
# Este comando "activa" el estudio. Es como encender las luces y la mesa de mezclas.
# Verás que el nombre del estudio aparece entre paréntesis en tu terminal: (estudio_skz)

# 3. Ahora, dentro del estudio, instalamos el equipamiento que solo Stray Kids necesita.
# (estudio_skz) > pip install pygame  # (Una librería para hacer juegos, ¡quizás para un MV interactivo!)

# 4. Si hacemos un inventario ahora, solo veremos el equipo de este estudio.
# (estudio_skz) > pip freeze
# (Salida: pygame==2.5.2)
# ¡Numpy no está aquí, porque lo instalamos fuera, en el estudio "global"!

# 5. `deactivate`
# Apaga y sale del estudio privado, volviendo al estudio principal de la agencia.
# (estudio_skz) > deactivate
# > (La terminal vuelve a la normalidad)


# --> Usando el equipamiento instalado en nuestro código <--

# Una vez que un paquete está instalado (en el entorno global o en el virtual activado),
# podemos importarlo en nuestro código Python como cualquier otro módulo.

import numpy as np

# Creamos un "array" de numpy, una estructura de datos súper eficiente.
# Es como una lista de reproducción optimizada.
setlist_principal = np.array(["God's Menu", "Maniac", "LALALALA"])

print("--> Setlist principal del concierto usando un array de NumPy <--")
print(setlist_principal)
