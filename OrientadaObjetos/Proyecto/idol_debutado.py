# Descripción: Hereda de Trainee y extiende su funcionalidad.

# Importa la clase padre del módulo 'trainee'.
import trainee

class IdolDebutado(trainee.Trainee):
    """Un Trainee que ha debutado. Hereda de Trainee y añade nuevas características."""
    rol = "Idol Debutado"

    def __init__(self, nombre, agencia, grupo):
        # Llama al __init__ del padre para establecer nombre y agencia.
        super().__init__(nombre, agencia)
        # Añade un nuevo atributo.
        self.grupo = grupo

    def presentarse(self):
        """
        Sobrescribe el método del padre para añadir más información.
        """
        # 1. Llama al método .presentarse() original del padre con super().
        super().presentarse()
        # 2. Añade la nueva información específica de esta clase.
        print(f"He debutado en el grupo: {self.grupo}.")

