
# MODULO DE COLORES DE COLORSENSE

colores = [
    ["Rojo", (255, 0, 0), "#FF0000"],
    ["Azul", (0, 0, 255), "#0000FF"],
    ["Verde", (0, 180, 0), "#00B400"],
    ["Amarillo", (255, 255, 0), "#FFFF00"],
    ["Naranja", (255, 165, 0), "#FFA500"],
    ["Morado", (128, 0, 128), "#800080"],
    ["Rosa", (255, 192, 203), "#FFC0CB"],
    ["Cafe", (139, 69, 19), "#8B4513"],
    ["Blanco", (255, 255, 255), "#FFFFFF"],
    ["Negro", (0, 0, 0), "#000000"]
]

# Puntuacion de cada juego
puntos = [0, 0]


def mostrar_colores():
    print("\n===== COLORES DISPONIBLES =====")

    for numero, color in enumerate(colores, start=1):
        print(f"{numero}. {color[0]}")
