'''
Ejercicio 3: Representando el juego en una lista

En este ejercicio, vamos a experimentar usando una lista para representar el juego.

En vez de usar 16 variables para representar el juego, vamos a usar una lista de 16 elementos.
Como vimos en clases, el primer elemento de la lista está representado por el índice 0,
por lo que nuestro diagrama cambiará un poco, de la siguiente forma:
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

La lista estará representada por la variable 'grilla'.
En este ejercicio, debes simplemente acceder al valor contenido en una posición determinada de la lista,
según lo que muestra el diagrama.

Tu código debe imprimir el valor contenido en la posición indicada por el argumento 'posicion'.
Recuerda que el primer elemento de la lista está representado por el índice 0, y el último por el índice 15.
'''

grilla = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 0, 2, 4, 8]

# Puedes modificar el valor de la siguiente variable
posicion = 8

# Aquí abajo escribe tu código