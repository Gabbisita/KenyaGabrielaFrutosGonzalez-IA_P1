# Descripción: Programa principal que crea y presenta a los artistas.

# Importa los módulos que contienen nuestras clases.
import trainee
import idol_debutado
import lider_de_grupo

# Creamos un objeto de cada nivel de la jerarquía.
trainee_nuevo = trainee.Trainee("Haruto", "YG")
idol_principal = idol_debutado.IdolDebutado("Felix", "JYP", "Stray Kids")
lider = lider_de_grupo.LiderDeGrupo("Bang Chan", "JYP", "Stray Kids", 5)

# --- ¡Comienzan las presentaciones! ---

print("--- Presentación del Trainee ---")
trainee_nuevo.presentarse()

print("\n--- Presentación del Idol Debutado ---")
idol_principal.presentarse()

print("\n--- Presentación del Líder de Grupo ---")
lider.presentarse()
