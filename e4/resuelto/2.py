'''
Ejercicio 2: Movimiento en múltiples columnas

En este ejercicio, vamos a implementar el movimiento vertical en múltiples columnas

Usaremos el mismo nombre para las variables que en el ejercicio anterior. Aquí va el mismo diagrama:

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

En este ejercicio, debes implementar el movimiento horizontal en múltiples columnas.
Esto quiere decir que, al recibir un input, el movimiento debe aplicarse a cada columna.

Al hacer un movimiento hacia abajo, cada columna debe individualmente mover sus elementos hacia abajo.

Tip: para resolver este ejercicio, podría ser de utilidad reusar la función de movimiento horizontal, y 
adaptarla para que pueda recibir una dirección vertical (arriba o abajo).

Luego, podremos resolver este ejercicio aplicando la función y cambiando los argumentos que recibe.
Por ejemplo, si queremos mover los elementos de la primera columna hacia abajo, debemos pasarle como argumento
la variable numero_1, numero_5, numero_9, numero_13 (los elementos que están en la primera columna del diagrama).
Para la segunda columna, debemos pasarle numero_2, numero_6, numero_10, numero_14 (y así sucesivamente).

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

## Usar métodos que se encuentran en la entrega anterior
## Correr cada método con los argumentos correspondientes
## Agregar opción "arriba" o "abajo" en la dirección
## Ej: movimiento(numero_1, numero_5, numero_9, numero_13, 'abajo')
##     movimiento(numero_2, numero_6, numero_10, numero_14, 'abajo')
##     movimiento(numero_3, numero_7, numero_11, numero_15, 'abajo')
##     movimiento(numero_4, numero_8, numero_12, numero_16, 'abajo')
