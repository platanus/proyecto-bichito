'''
Ejercicio 1: Movimiento en múltiples filas

En este ejercicio, vamos a implementar el movimiento horizontal en múltiples filas

Dado que ahora tendremos 4 filas con 4 elementos cada una, tendremos 16 variables que debemos asignar.
Para entender cómo identificar las variables que debemos utilizar, veamos el siguiente diagrama:

     _____ _____ _____ _____
    |     |     |     |     |
    |  1  |  2  |  3  |  4  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    |  5  |  6  |  7  |  8  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    |  9  | 10  | 11  | 12  |
    |_____|_____|_____|_____|
    |     |     |     |     |
    | 13  | 14  | 15  | 16  |
    |_____|_____|_____|_____|

El diagrama muestra el número de la variable asociada a cada casilla.
Así, vemos que la primera fila corresponde a las variables que hemos usado hasta ahora.
Pero agregamos 3 filas más, cada una con 4 nuevas variables.

En este ejercicio, debes implementar el movimiento horizontal en múltiples filas.
Esto quiere decir que, al recibir un input, el movimiento debe aplicarse a todas las filas.

Al hacer un movimiento hacia la derecha, cada fila debe individualmente mover sus elementos hacia la derecha.
Aprovechando las funciones de la entrega anterior, podemos usar la misma función de movimiento para aplicar el movimiento
en múltiples filas. Solo debemos cambiar los argumentos que le entregamos a la función.
Por ejemplo, si queremos mover los elementos de la primera fila hacia la derecha, debemos pasarle como argumento
la variable numero_1, numero_2, numero_3 y numero_4.
Para la segunda fila, debemos pasarle numero_5, numero_6, numero_7 y numero_8 (y así sucesivamente).

Nota, basta con que el movimiento pueda realizarse una sola vez, pero si quieres puedes integrar tu
código de las entregas anteriores para que se puedan jugar varios turnos.
'''

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 0
numero_3 = 2
numero_4 = 4
numero_5 = 4
numero_6 = 8
numero_7 = 8
numero_8 = 16
numero_9 = 2
numero_10 = 2
numero_11 = 2
numero_12 = 2
numero_13 = 128
numero_14 = 32
numero_15 = 32
numero_16 = 64

# Aquí abajo escribe tu código