# --> Módulo Datetime: La agenda de un Comeback de K-pop <--

# El módulo 'datetime' es como el manager de agenda de un grupo.
# Nos permite trabajar con fechas, horas y todo lo relacionado con el tiempo.
import datetime
import locale

# --> datetime.time: La hora del Showcase <--
# Crea un objeto para manejar una hora específica, sin fecha.
hora_showcase = datetime.time(18, 0, 0) # 18:00:00
print(f"La hora del showcase de comeback es a las: {hora_showcase}")

# Puedo acceder a cada parte de la hora por separado.
print(f"Hora: {hora_showcase.hour}, Minutos: {hora_showcase.minute}")


# --> datetime.date: La fecha del lanzamiento del álbum <--
# Crea un objeto para manejar una fecha, sin hora.
fecha_lanzamiento = datetime.date(2024, 10, 25)
print(f"\nLa fecha de lanzamiento del álbum es: {fecha_lanzamiento}")

# También puedo acceder a sus partes.
print(f"Año: {fecha_lanzamiento.year}, Mes: {fecha_lanzamiento.month}, Día: {fecha_lanzamiento.day}")

# Para saber la fecha de hoy, uso .today()
fecha_de_hoy = datetime.date.today()
print(f"La fecha de hoy es: {fecha_de_hoy}")


# --> datetime.datetime: El momento exacto del Comeback <--
# Este objeto combina fecha y hora. Es el más completo.
# Con .now() obtenemos el momento exacto en que se ejecuta esta línea.
momento_exacto_ahora = datetime.datetime.now()
print(f"\nEl anuncio del comeback se está haciendo en este preciso instante: {momento_exacto_ahora}")


# --> strftime(): Formateando la fecha para el póster oficial <--
# El método .strftime() nos permite convertir un objeto datetime a un string con el formato que queramos.
# Es como diseñar el texto para un póster de anuncio.

# Establecemos el idioma a español para que los nombres de los meses y días salgan correctamente.
locale.setlocale(locale.LC_ALL, "es")

# Creamos una fecha y hora para el Music Video (MV).
lanzamiento_mv = datetime.datetime(2024, 11, 1, 13, 0) # 1 de Nov de 2024 a las 13:00

# Usamos códigos de formato para diseñar la fecha.
# %A: Nombre completo del día de la semana.
# %d: Día del mes.
# %B: Nombre completo del mes.
# %Y: Año con cuatro dígitos.
# %H: Hora (formato 24h).
# %M: Minutos.
anuncio_poster = lanzamiento_mv.strftime("Gran lanzamiento: %A, %d de %B de %Y a las %H:%M").capitalize()
print("\n--- Anuncio en el Póster Oficial ---")
print(anuncio_poster)
