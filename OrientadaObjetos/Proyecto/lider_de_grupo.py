# Descripción: Hereda de IdolDebutado y vuelve a extender.

# Importa la clase padre del módulo 'idol_debutado'.
import idol_debutado

class LiderDeGrupo(idol_debutado.IdolDebutado):
    """Un Idol Debutado con el rol de líder."""
    rol = "Líder de Grupo"

    def __init__(self, nombre, agencia, grupo, años_liderazgo):
        super().__init__(nombre, agencia, grupo)
        self.años_liderazgo = años_liderazgo

    def presentarse(self):
        """
        Vuelve a sobrescribir el método para añadir la información de liderazgo.
        """
        # 1. Llama al método .presentarse() de su padre (IdolDebutado).
        super().presentarse()
        # 2. Añade su propia información.
        print(f"Llevo {self.años_liderazgo} años liderando al grupo.")

