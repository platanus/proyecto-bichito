# Ejercicio 7: Movimiento en una fila de 3 elementos.
#
# Supongamos que tenemos tres casillas del juego 2048, una a la izquierda, una al centro y una a la derecha medio.
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |  2  |  2  |
#     |_____|_____|_____|
#
# Si hiciéramos un movimiento hacia la derecha, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |     |  2  |  4  |
#     |_____|_____|_____|
#
# Esto es porque los dos elementos a la derecha se suman, y el elemento de la izquierda ocupa el lugar vacío que queda en el centro.
#
# En cambio, si desde la fila inicial hiciéramos un movimiento hacia la izquierda, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  4  |  2  |     |
#     |_____|_____|_____|
#
# Siguiendo la misma lógica, los dos elementos a la izquierda se suman, y el elemento de la derecha ocupa el lugar vacío que queda en el centro.
#
#
#
# Veamos otro ejemplo:
# Supongamos que tenemos esta fila:
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |  4  |     |
#     |_____|_____|_____|
#
# Si hiciéramos un movimiento hacia la derecha, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |     |  2  |  4  |
#     |_____|_____|_____|
#
# Vemos que, si bien no hay variables que se sumen, los elementos de la fila se mueven de todas formas.
# Ahora bien, si desde la fila original hiciéramos un movimiento hacia la izquierda, la fila quedaría igual que al inicio, así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |  4  |     |
#     |_____|_____|_____|
#
# Esto es porque no hay más espacio hacia la izquierda para que se muevan los elementos, y tampoco pueden sumarse.

# Para este ejercicio, vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1", la del centro a la variable "numero_2" y la de la derecha a la variable "numero_3".
# En este ejercicio, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
# Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.
# Recuerda que si dos números son distintos, no se pueden sumar, pero la fila aun puede moverse.
# Luego, vamos a imprimir en consola el valor de las variables "numero_1", "numero_2" y "numero_3".

# Deberás probar tu código con los siguientes valores para las variables "numero_1", "numero_2" y "numero_3":
# a)  numero_1 = 2
#     numero_2 = 2
#     numero_3 = 2
#
# b)  numero_1 = 2
#     numero_2 = 4
#     numero_3 = 0
#
# c)  numero_1 = 0
#     numero_2 = 128
#     numero_3 = 64
#
# d)  numero_1 = 32
#     numero_2 = 0
#     numero_3 = 32
#
# e)  numero_1 = 1024
#     numero_2 = 1024
#     numero_3 = 256
#
# f)  numero_1 = 16
#     numero_2 = 32
#     numero_3 = 32
#
# g)  numero_1 = 512
#     numero_2 = 1024
#     numero_3 = 512
#
# h)  numero_1 = 0
#     numero_2 = 0
#     numero_3 = 4
#
# i)  numero_1 = 64
#     numero_2 = 0
#     numero_3 = 0
#
# j)  numero_1 = 0
#     numero_2 = 1024
#     numero_3 = 0
#
# k)  numero_1 = 512
#     numero_2 = 8
#     numero_3 = 2
#
# ¡Recuerda que tu código debe funcionar correctamente para todos los casos!

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 2
numero_3 = 2
direccion = input("Escribe izquierda o derecha: ")

### Aquí abajo escribe tu código
