'''
Ejercicio 4: Ciclo de juego: Agregar más turnos

A partir de lo realizado en el ejercicio 3, en este ejercicio se debe poder jugar una cantidad indefinida de turnos.

Para resolver este ejercicio, vamos a tomar como base lo realizado en el ejercicio 3 anterior.

Para este ejercicio, vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1", la del centro a la variable "numero_2" y la de la derecha a la variable "numero_3".
Además, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.

Recuerda que si dos números son distintos, no se pueden sumar, pero la fila aun puede moverse.
Si luego de intentar realizar el movimiento, la fila se mantiene igual, entonces debemos solicitar nuevamente el input del usuario, pero no avanzar el turno.
Si la fila cambia, entonces debes crear un número 2 en el primer espacio disponible, y luego
imprimir en consola el valor de las variables "numero_1", "numero_2" y "numero_3".
Además, se debe imprimir el puntaje actual en cada turno.
Después de esto debes pedir nuevamente el input del usuario.
En este ejercicio vamos a realizar varios turnos y se debe poder jugar hasta que lleguemos a que todos los movimientos son inválidos.


Deberás probar tu código con los siguientes valores para las variables "numero_1", "numero_2" y "numero_3":
a)  numero_1 = 2
    numero_2 = 0
    numero_3 = 0

b)  numero_1 = 2
    numero_2 = 4
    numero_3 = 0

c)  numero_1 = 32
    numero_2 = 0
    numero_3 = 32

d)  numero_1 = 32
    numero_2 = 32
    numero_3 = 64

e)  numero_1 = 2
    numero_2 = 0
    numero_3 = 64

¡Recuerda que tu código debe funcionar correctamente para todos los casos!
'''

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 4
numero_3 = 0
print("Estado Inicial: " + str(numero_1) +
      " " + str(numero_2) + " " + str(numero_3))
puntaje = 0


# Aquí abajo escribe tu código

nuevo_numero = 2

while True:
    numero_1_anterior = numero_1
    numero_2_anterior = numero_2
    numero_3_anterior = numero_3

    direccion = input("Escribe izquierda o derecha: ")

    if direccion == "izquierda":
        if numero_1 != 0:
            if numero_1 == numero_2:
                numero_1 = numero_1 + numero_2
                puntaje = puntaje + numero_1
                numero_2 = numero_3
                numero_3 = 0
            elif numero_1 == numero_3 and numero_2 == 0:
                numero_1 = numero_1 + numero_3
                puntaje = puntaje + numero_1
                numero_3 = 0
            elif numero_2 == numero_3 and numero_2 != 0:
                numero_2 = numero_2 + numero_3
                puntaje = puntaje + numero_2
                numero_3 = 0
            elif numero_2 == 0:
                numero_2 = numero_3
                numero_3 = 0
        elif numero_2 != 0:
            if numero_2 == numero_3:
                numero_1 = numero_2 + numero_3
                puntaje = puntaje + numero_1
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
                puntaje = puntaje + numero_3
                numero_2 = numero_1
                numero_1 = 0
            elif numero_1 == numero_3 and numero_2 == 0:
                numero_3 = numero_1 + numero_3
                puntaje = puntaje + numero_3
                numero_1 = 0
            elif numero_1 == numero_2 and numero_2 != 0:
                numero_2 = numero_1 + numero_2
                puntaje = puntaje + numero_2
                numero_1 = 0
            elif numero_2 == 0:
                numero_2 = numero_1
                numero_1 = 0
        elif numero_2 != 0:
            if numero_2 == numero_1:
                numero_3 = numero_2 + numero_1
                puntaje = puntaje + numero_3
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
        continue
    else:
        print("Movimiento válido")
        # Agregamos el nuevo valor 2
        if numero_1 == 0:
            numero_1 = 2
        elif numero_2 == 0:
            numero_2 = 2
        elif numero_3 == 0:
            numero_3 = 2

        # Imprimimos resultado
        print(str(numero_1) + " " + str(numero_2) + " " + str(numero_3))

        # Imprimimos puntaje actual
        print("Puntaje Actual: " + str(puntaje))
