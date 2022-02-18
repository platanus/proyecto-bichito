# Ejercicio 4: Movimiento en una fila de 2 elementos.
#
# Supongamos que tenemos dos casillas del juego 2048, una a la izquierda y una a la derecha.
#
#      _____ _____ 
#     |     |     |
#     |  2  |  2  |
#     |_____|_____|
#
# Si hiciéramos un movimiento hacia la derecha, la fila quedaría así: 
#
#      _____ _____
#     |     |     |
#     |     |  4  |
#     |_____|_____|
#
# En cambio, si desde la fila inicial hiciéramos un movimiento hacia la izquierda, la fila quedaría así:
#
#      _____ _____
#     |     |     |
#     |  4  |     |
#     |_____|_____|
#
# Vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1" y la de la derecha a la variable "numero_2".
# En este ejercicio, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion". 
# Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.
# Recuerda que si los números son distintos, no se pueden sumar, por lo que no vas a poder mover nada.
# Luego, vamos a imprimir en consola el valor de las variables "numero_1" y "numero_2".

# Deberás probar tu código con los siguientes valores para las variables "numero_1" y "numero_2":
# a)  numero_1 = 2
#     numero_2 = 2
#
# b)  numero_1 = 2
#     numero_2 = 4
#
# c)  numero_1 = 64
#     numero_2 = 64
#
# d)  numero_1 = 512
#     numero_2 = 512
#
# ¡Recuerda que tu código debe funcionar correctamente para todos los casos!

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 2
direccion = input("Escribe izquierda o derecha: ")

### Aquí abajo escribe tu código
