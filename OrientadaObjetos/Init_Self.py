# --> Atributos de Clase vs. Atributos de Instancia <--
# --> El estándar de la agencia vs. el perfil de cada Idol <--

# --> 1. Atributos de Clase: El estándar de la agencia <--
# Estos son valores por defecto que se aplican a CUALQUIER idol que se cree a partir de este molde.
# Son como las expectativas base de la agencia para todos sus artistas.

class IdolEstandar:
    """Molde con estadísticas base definidas por la agencia."""
    # Atributos de Clase
    energia_base = 100
    periodo_trainee_años = 3
    rol_principal = "Artista Polivalente"

    def fin_del_contrato(self):
        print("El contrato ha finalizado.")

# Creamos dos idols con este molde.
idol_A = IdolEstandar()
idol_B = IdolEstandar()

# Al principio, ambos tienen las mismas estadísticas base de la agencia.
print(f"Rol inicial de Idol A: {idol_A.rol_principal}")
print(f"Rol inicial de Idol B: {idol_B.rol_principal}")

# Si modificamos el rol de Idol B, solo cambia para él.
# Python crea un 'atributo de instancia' para Idol B que "oculta" el atributo de clase.
print("\n...Idol B se especializa en baile...")
idol_B.rol_principal = "Bailarín Principal"

print(f"Nuevo rol de Idol B: {idol_B.rol_principal}")
print(f"El rol de Idol A sigue siendo el estándar: {idol_A.rol_principal}")


# --> 2. Atributos de Instancia con __init__: Debut personalizado <--
# Este es el método preferido. El constructor `__init__` nos obliga a definir
# las características de CADA idol en el momento de su creación.
# Cada idol tiene su propio conjunto de atributos desde el debut.

class IdolProfesional:
    """Molde que crea idols con perfiles personalizados desde el debut."""
    def __init__(self, nombre, rol, energia):
        # Atributos de Instancia (únicos para cada objeto)
        self.nombre = nombre
        self.rol = rol
        self.energia = energia

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, ¡{self.rol} del grupo!")

# Al crear el objeto, DEBEMOS pasar los argumentos para sus atributos de instancia.
felix = IdolProfesional("Felix", "Rapero y Bailarín", 120)
seungmin = IdolProfesional("Seungmin", "Vocalista Principal", 90)

print("\n--- Perfiles de debut personalizados ---")
felix.presentarse()
print(f"  -> Energía de performance: {felix.energia}")

seungmin.presentarse()
print(f"  -> Energía de performance: {seungmin.energia}")

# También puedo añadir un atributo nuevo a una instancia específica después de su creación.
print("\n...Felix aprende a producir música...")
felix.habilidad_extra = "Producción Musical"
print(f"Habilidad adicional de Felix: {felix.habilidad_extra}")
# seungmin no tendría este atributo.
