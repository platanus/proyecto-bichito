'''
Ejercicio 1: Turnos o movimientos válidos

En este ejercicio, vamos a incorporar código para verificar si un turno/movimiento es válido.

Un movimiento es válido si cambia alguna casilla de la tabla de juego.

Para entender la necesidad de esto, vamos a ver un ejemplo:

Supongamos que tenemos la siguiente fila de 3 elementos:
     _____ _____ _____
    |     |     |     |
    |  2  |  4  |     |
    |_____|_____|_____|

Si el jugador realiza un movimiento hacia la derecha, la fila quedaría así:
     _____ _____ _____
    |     |     |     |
    |     |  2  |  4  |
    |_____|_____|_____|

Lo cual es un movimiento válido, porque los elementos cambiaron de posición.

Ahora bien, si desde la fila inicial, el jugador realiza un movimiento hacia la izquierda,
la fila quedaría así:
     _____ _____ _____
    |     |     |     |
    |  2  |  4  |     |
    |_____|_____|_____|

Lo cual no es un movimiento válido, porque ningún elemento cambió de posición.
Es decir, ¡la fila quedó igual!

Para resolver este ejercicio, vamos a tomar como base lo realizado en el ejercicio 7 de la entrega 1.
Además, vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1", la del centro a la variable "numero_2" y la de la derecha a la variable "numero_3".
Junto con esto, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.

Recuerda que si dos números son distintos, no se pueden sumar, pero la fila aun puede moverse.
Si luego de intentar realizar el movimiento, la fila se mantiene igual, entonces debes imprimir en consola "Movimiento inválido".
Si la fila cambia, entonces debes imprimir en consola "Movimiento válido" y luego imprimir en consola el valor de las variables "numero_1", "numero_2" y "numero_3".

Deberás probar tu código con los siguientes valores para las variables "numero_1", "numero_2" y "numero_3":

a)  numero_1 = 2
    numero_2 = 4
    numero_3 = 0

b)  numero_1 = 4
    numero_2 = 2
    numero_3 = 8

c)  numero_1 = 32
    numero_2 = 0
    numero_3 = 32

d)  numero_1 = 0
    numero_2 = 16
    numero_3 = 64

e)  numero_1 = 2
    numero_2 = 0
    numero_3 = 64

¡Recuerda que tu código debe funcionar correctamente para todos los casos!
'''

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 0
numero_3 = 64
direccion = input("Escribe izquierda o derecha: ")

# Aquí abajo escribe tu código
numero_1_anterior = numero_1
numero_2_anterior = numero_2
numero_3_anterior = numero_3

if direccion == "izquierda":
    if numero_1 != 0:
        if numero_1 == numero_2:
            numero_1 = numero_1 + numero_2
            numero_2 = numero_3
            numero_3 = 0
        elif numero_1 == numero_3 and numero_2 == 0:
            numero_1 = numero_1 + numero_3
            numero_3 = 0
        elif numero_2 == numero_3 and numero_2 != 0:
            numero_2 = numero_2 + numero_3
            numero_3 = 0
        elif numero_2 == 0:
            numero_2 = numero_3
            numero_3 = 0
    elif numero_2 != 0:
        if numero_2 == numero_3:
            numero_1 = numero_2 + numero_3
            numero_2 = 0
            numero_3 = 0
        else:
            numero_1 = numero_2
            numero_2 = numero_3
            numero_3 = 0
    elif numero_3 != 0:
        numero_1 = numero_3
        numero_2 = 0
        numero_3 = 0
elif direccion == "derecha":
    if numero_3 != 0:
        if numero_3 == numero_2:
            numero_3 = numero_3 + numero_2
            numero_2 = numero_1
            numero_1 = 0
        elif numero_1 == numero_3 and numero_2 == 0:
            numero_3 = numero_1 + numero_3
            numero_1 = 0
        elif numero_1 == numero_2 and numero_2 != 0:
            numero_2 = numero_1 + numero_2
            numero_1 = 0
        elif numero_2 == 0:
            numero_2 = numero_1
            numero_1 = 0
    elif numero_2 != 0:
        if numero_2 == numero_1:
            numero_3 = numero_2 + numero_1
            numero_2 = 0
            numero_1 = 0
        else:
            numero_3 = numero_2
            numero_2 = numero_1
            numero_1 = 0
    elif numero_1 != 0:
        numero_3 = numero_1
        numero_2 = 0
        numero_1 = 0

if (numero_1 == numero_1_anterior and numero_2 == numero_2_anterior and numero_3 == numero_3_anterior):
    print("Movimiento inválido")
else:
    print("Movimiento válido")
    print(str(numero_1) + " " + str(numero_2) + " " + str(numero_3))
