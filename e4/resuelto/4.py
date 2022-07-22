'''
Ejercicio 4: Obteniendo las filas y columnas de la grilla

En este ejercicio, vamos a implementar una función que nos permita obtener las filas o columnas de la grilla.
Nuevamente, usaremos la variable 'grilla' para representar los elementos del juego, en base al diagrama:
     _____ _____ _____ _____
    |     |     |     |     |
    |  0  |  1  |  2  |  3  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    |  4  |  5  |  6  |  7  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    |  8  |  9  | 10  | 11  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    | 12  | 13  | 14  | 15  |
    |_____|_____|_____|_____|

En este ejercicio, debes implementar una función llamada 'imprimir_filas', que reciba la grilla y luego imprima
cada fila de la grilla de forma ordenada de la siguiente forma:

"fila 1: 0 2 4 8"
"fila 2: 16 32 64 128"
"fila 3: 256 512 1024 2048"
"fila 4: 0 2 4 8"

También debes implementar una función llamada 'imprimir_columnas', que reciba la grilla y luego imprima
cada columna de la grilla de forma ordenada de la siguiente forma:

"columna 1: 0 16 256 0"
"columna 2: 2 32 512 2"
"columna 3: 4 64 1024 4"
"columna 4: 8 128 2048 8"

Recuerda que el primer elemento de la lista está representado por el índice 0, y el último por el índice 15.
'''

grilla = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 0, 2, 4, 8]

# Aquí abajo escribe tu código
def imprimir_filas(grilla):
    print("fila 1:", grilla[0], grilla[1], grilla[2], grilla[3])
    print("fila 2:", grilla[4], grilla[5], grilla[6], grilla[7])
    print("fila 3:", grilla[8], grilla[9], grilla[10], grilla[11])
    print("fila 4:", grilla[12], grilla[13], grilla[14], grilla[15])

def imprimir_columnas(grilla):
    print("columna 1:", grilla[0], grilla[4], grilla[8], grilla[12])
    print("columna 2:", grilla[1], grilla[5], grilla[9], grilla[13])
    print("columna 3:", grilla[2], grilla[6], grilla[10], grilla[14])
    print("columna 4:", grilla[3], grilla[7], grilla[11], grilla[15])
# Hasta aquí tu código

imprimir_filas(grilla)
imprimir_columnas(grilla)