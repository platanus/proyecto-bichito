# Ejercicio 5: Movimiento con celdas vacías.
#
# Supongamos que tenemos dos casillas del juego 2048, una a la izquierda y una a la derecha, pero una de ellas está vacía
#
#      _____ _____
#     |     |     |
#     |  2  |     |
#     |_____|_____|
#
# Si hiciéramos un movimiento hacia la derecha, la fila quedaría así:
#
#      _____ _____
#     |     |     |
#     |     |  2  |
#     |_____|_____|
#
# Como hay un espacio vacío en la fila, aunque no haya elementos que puedan sumarse, sí pueden moverse.
#
# En cambio, si desde la fila inicial hiciéramos un movimiento hacia la izquierda, la fila quedaría así, igual que al inicio:
#
#      _____ _____
#     |     |     |
#     |  2  |     |
#     |_____|_____|
#
# Esto es porque no hay un espacio donde mover el elemento 2
#
# Vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1" y la de la derecha a la variable "numero_2".
# En este ejercicio, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
# Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.
# Vamos a tener espacios vacíos, y dependiendo de eso vamos a "mover" o reasignar las variables de la fila, como corresponda.
#
# Recuerda que los espacios vacíos los representamos con un 0.

# Deberás probar tu código con los siguientes valores para las variables "numero_1" y "numero_2":
# a)  numero_1 = 2
#     numero_2 = 0
#
# b)  numero_1 = 0
#     numero_2 = 4
#
# c)  numero_1 = 512
#     numero_2 = 0
#
# d)  numero_1 = 0
#     numero_2 = 64
#
# ¡Recuerda que tu código debe funcionar correctamente para todos los casos!

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 0
direccion = input("Escribe izquierda o derecha: ")

### Aquí abajo escribe tu código
