
# MODULO PARA GESTIONAR EL HISTORIAL

import os

ARCHIVO_HISTORIAL = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "historial.txt"
)

historial = []


def cargar_historial():
    historial.clear()

    if os.path.exists(ARCHIVO_HISTORIAL):
        try:
            with open(
                ARCHIVO_HISTORIAL, "r", encoding="utf-8"
            ) as archivo:
                for linea in archivo:
                    registro = linea.strip()

                    if registro:
                        historial.append(registro)

        except OSError:
            print("No se pudo leer el historial.")


def guardar_historial(nombre, rgb, hex_color):
    registro = (
        f"{nombre} | RGB: {rgb} | HEX: {hex_color}"
    )

    try:
        with open(
            ARCHIVO_HISTORIAL, "a", encoding="utf-8"
        ) as archivo:
            archivo.write(registro + "\n")

        historial.append(registro)
        print("Color guardado correctamente.")

    except OSError:
        print("No se pudo guardar el color.")


def ver_historial():
    print("\n========== HISTORIAL ==========")

    if not historial:
        print("Todavia no has seleccionado colores.")
    else:
        for numero, registro in enumerate(historial, start=1):
            print(f"{numero}. {registro}")

    input("\nPresiona ENTER para regresar...")
