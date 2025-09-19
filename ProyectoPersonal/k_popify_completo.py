import pygame
import time
import os

# ---------------- CLASES ----------------
class Cancion:
    def __init__(self, titulo, duracion, archivo):
        self.titulo = titulo
        self.duracion = duracion  # en segundos (aprox)
        self.archivo = archivo    # ruta al mp3

    def __str__(self):
        minutos, segundos = divmod(self.duracion, 60)
        return f"{self.titulo} - {minutos:02d}:{segundos:02d}"

    def reproducir(self):
        if not os.path.exists(self.archivo):
            print(f"❌ No se encontró el archivo: {self.archivo}")
            return
        print(f"\n▶ Reproduciendo: {self.titulo}")
        try:
            pygame.mixer.music.load(self.archivo)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            print(f"\n✔ Canción terminada: {self.titulo}")
        except pygame.error as e:
            print(f"⚠ Error al reproducir '{self.titulo}': {e}")


class Album:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)


class Artista:
    def __init__(self, nombre, agencia):
        self.nombre = nombre
        self.agencia = agencia
        self.albums = []

    def agregar_album(self, album):
        self.albums.append(album)


# ---------------- CATÁLOGO ----------------
def cargar_catalogo():
    catalogo = []

    bts = Artista("BTS", "HYBE")
    album_her = Album("Love Yourself: Her", 2017)
    album_her.agregar_cancion(Cancion("DNA", 223, "musica/dna.mp3"))
    album_her.agregar_cancion(Cancion("Best Of Me", 227, "musica/best_of_me.mp3"))
    album_her.agregar_cancion(Cancion("MIC Drop", 238, "musica/mic_drop.mp3"))  # <-- AQUÍ ESTA TU ARCHIVO
    bts.agregar_album(album_her)
    catalogo.append(bts)

    lsf = Artista("LE SSERAFIM", "Source Music")
    album_unforgiven = Album("UNFORGIVEN", 2023)
    album_unforgiven.agregar_cancion(Cancion("UNFORGIVEN (feat. Nile Rodgers)", 182, "musica/unforgiven.mp3"))
    lsf.agregar_album(album_unforgiven)
    catalogo.append(lsf)

    return catalogo


# ---------------- MENÚ ----------------
def main():
    pygame.mixer.init()
    catalogo = cargar_catalogo()

    while True:
        print("\n===== K-Popify =====")
        print("1. Ver artistas y elegir")
        print("2. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            print("\n--- ARTISTAS ---")
            for i, artista in enumerate(catalogo, 1):
                print(f"{i}. {artista.nombre} ({artista.agencia})")

            entrada = input("Elige número o nombre del artista: ").strip()
            artista = None

            if entrada.isdigit():
                idx = int(entrada) - 1
                if 0 <= idx < len(catalogo):
                    artista = catalogo[idx]
            else:
                for a in catalogo:
                    if a.nombre.lower() == entrada.lower():
                        artista = a
                        break

            if not artista:
                print("❌ Artista inválido.")
                continue

            print(f"\n🎤 {artista.nombre} - Discografía")
            for j, album in enumerate(artista.albums, 1):
                print(f"{j}. {album.titulo} ({album.anio})")

            entrada_album = input("Elige número del álbum: ").strip()
            if not entrada_album.isdigit():
                print("❌ Álbum inválido.")
                continue
            idx_album = int(entrada_album) - 1
            if not (0 <= idx_album < len(artista.albums)):
                print("❌ Álbum inválido.")
                continue
            album = artista.albums[idx_album]

            print(f"\n💿 {album.titulo} - Canciones")
            for k, cancion in enumerate(album.canciones, 1):
                print(f"{k}. {cancion}")

            entrada_cancion = input("Elige número de la canción: ").strip()
            if not entrada_cancion.isdigit():
                print("❌ Canción inválida.")
                continue
            idx_cancion = int(entrada_cancion) - 1
            if not (0 <= idx_cancion < len(album.canciones)):
                print("❌ Canción inválida.")
                continue
            cancion = album.canciones[idx_cancion]
            cancion.reproducir()

        elif opcion == "2":
            print("👋 Gracias por usar K-Popify")
            break
        else:
            print("❌ Opción inválida.")

    pygame.mixer.quit()


if __name__ == "__main__":
    main()
