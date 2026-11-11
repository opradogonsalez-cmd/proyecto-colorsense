
# MODULO DE JUEGOS EDUCATIVOS

import random
from colores import colores, puntos


def adivina_color():
    print("\n===== ADIVINA EL COLOR =====")

    secreto = random.choice(colores)

    opciones = random.sample(
        [color for color in colores if color != secreto],
        3
    )

    opciones.append(secreto)
    random.shuffle(opciones)

    print("\n¿Que color corresponde a este codigo?")
    print("RGB:", secreto[1])

    for numero, color in enumerate(opciones, start=1):
        print(f"{numero}. {color[0]}")

    try:
        respuesta = int(input("\nTu respuesta: "))

        if 1 <= respuesta <= 4:
            if opciones[respuesta - 1] == secreto:
                print("Correcto. Ganaste un punto.")
                puntos[0] += 1
            else:
                print("Respuesta incorrecta.")

            print("El color correcto era:", secreto[0])
        else:
            print("Selecciona un numero del 1 al 4.")

    except ValueError:
        print("Debes ingresar un numero valido.")

    print("Puntuacion acumulada:", puntos[0])
    input("\nPresiona ENTER para continuar...")



def memoriza_colores():
    print("\n===== MEMORIZA LOS COLORES =====")

    seleccionados = random.sample(colores, 4)

    print("\nMemoriza estos cuatro colores y sus códigos HEX:\n")

    for color in seleccionados:
        print(f"- {color[0]}  |  HEX: {color[2]}")

    input("\nCuando estes listo, presiona ENTER...")

    print("\n" * 30)

    print("Escribe el codigo HEX de cada color.")

    aciertos = 0

    for color in seleccionados:
        respuesta = input(
            f"\nCodigo HEX de {color[0]}: "
        ).strip().upper()

        if respuesta == color[2]:
            print("Correcto.")
            aciertos += 1
        else:
            print("Incorrecto. El codigo era:", color[2])

    puntos[1] += aciertos

    print("\n===== RESULTADOS =====")
    print(f"Aciertos de esta ronda: {aciertos}/4")
    print("Puntuacion acumulada:", puntos[1])

    input("\nPresiona ENTER para continuar...")


def ver_puntuaciones():
    print("\n===== PUNTUACIONES =====")
    print("Adivina el color:", puntos[0])
    print("Memoriza los colores:", puntos[1])

    input("\nPresiona ENTER para regresar...")


def menu_juegos():
    while True:
        print("\n========== MINIJUEGOS ==========")
        print("1. Memoriza el color")
        print("2. Adivina el color")
        print("3. Ver puntuaciones")
        print("4. Regresar al inicio")

        opcion = input("\nSelecciona una opcion: ").strip()

        if opcion == "1":
            memoriza_colores()

        elif opcion == "2":
            adivina_color()

        elif opcion == "3":
            ver_puntuaciones()

        elif opcion == "4":
            break

        else:
            print("Opcion invalida. Intenta nuevamente.")
