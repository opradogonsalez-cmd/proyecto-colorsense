
# MODULO PARA DETECTAR Y CONSULTAR COLORES

from colores import colores, mostrar_colores
from historial import guardar_historial


def detectar_color():
    print("\n===== DETECTAR EL COLOR =====")
    print("Selecciona el color que deseas consultar.")

    mostrar_colores()

    try:
        opcion = int(input("\nSelecciona un color: "))

        if 1 <= opcion <= len(colores):
            color = colores[opcion - 1]

            print("\n===== INFORMACION DEL COLOR =====")
            print("Nombre:", color[0])
            print("Codigo RGB:", color[1])
            print("Codigo HEX:", color[2])

            guardar_historial(
                color[0], color[1], color[2]
            )

        else:
            print("Opcion fuera de rango.")

    except ValueError:
        print("Debes ingresar un numero valido.")

    input("\nPresiona ENTER para regresar...")
