
# PROGRAMA PRINCIPAL DE COLORSENSE

from detector import detectar_color
from historial import cargar_historial, ver_historial
from juegos import menu_juegos


def pantalla_inicio():
    print("\n" + "=" * 36)
    print("             COLORSENSE")
    print("=" * 36)
    print("       Aprende los colores")
    print()
    print("1. Detectar el color")
    print("2. Historial")
    print("3. Minijuegos")
    print("4. Salir")
    print("=" * 36)


def menu_principal():
    while True:
        pantalla_inicio()

        opcion = input(
            "\nSelecciona una opcion: "
        ).strip()

        if opcion == "1":
            detectar_color()

        elif opcion == "2":
            ver_historial()

        elif opcion == "3":
            menu_juegos()

        elif opcion == "4":
            print("\nGracias por utilizar Color Sense.")
            print("Hasta la proxima.")
            break

        else:
            print("Opcion invalida. Intenta nuevamente.")


if __name__ == "__main__":
    cargar_historial()
    menu_principal()
