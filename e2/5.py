'''
Ejercicio 5: Ciclo de juego: Terminar el juego

A partir de lo realizado en el ejercicio 4, en este ejercicio se debe poder terminar el juego una vez que no hayan movimientos disponibles.

Para resolver este ejercicio, vamos a tomar como base lo realizado en el ejercicio 4 anterior.

Para este ejercicio, vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1", la del centro a la variable "numero_2" y la de la derecha a la variable "numero_3".
Además, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.

Recuerda que si dos números son distintos, no se pueden sumar, pero la fila aun puede moverse.
Si luego de intentar realizar el movimiento, la fila se mantiene igual, entonces debemos solicitar nuevamente el input del usuario, pero no avanzar el turno.
Si la fila cambia, entonces debes crear un número 2 en el primer espacio disponible, y luego
imprimir en consola el valor de las variables "numero_1", "numero_2" y "numero_3".
Además, se debe imprimir el puntaje actual en cada turno.
Después de esto debes pedir nuevamente el input del usuario.

En este ejercicio vamos a realizar varios turnos y una vez que no se puedan hacer movimientos, se debe terminar el juego e imprimir
'El juego ha terminado! Ya no hay movimientos posibles'


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
direccion = input("Escribe izquierda o derecha: ")
puntaje = 0


# Aquí abajo escribe tu código
