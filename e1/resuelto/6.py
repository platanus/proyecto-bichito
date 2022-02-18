# Ejercicio 6: Movimiento generalizado con dos celdas
#
# En este ejercicio vamos a mezclar la solución de los dos ejercicios anteriores. Es decir, vamos a tener algunos
# casos en que habrá una celda vacía, vamos a tener algunos casos en que dos celdas pueden sumarse, y vamos a tener
# algunos casos en que no se pueden sumar.
#
# Vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1" y la de la derecha a la variable "numero_2".
# En este ejercicio, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
# Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.
# Vamos a tener espacios vacíos, y dependiendo de eso vamos a "mover" o reasignar las variables de la fila, como corresponda.
# Luego, vamos a imprimir en consola el valor de las variables "numero_1" y "numero_2".
#
# Recuerda que los espacios vacíos los representamos con un 0.

# Deberás probar tu código con los siguientes valores para las variables "numero_1" y "numero_2":
# a)  numero_1 = 2
#     numero_2 = 0
#
# b)  numero_1 = 8
#     numero_2 = 4
#
# c)  numero_1 = 512
#     numero_2 = 512
#
# d)  numero_1 = 0
#     numero_2 = 64
#
# ¡Recuerda que tu código debe funcionar correctamente para todos los casos!

numero_1 = 0
numero_2 = 64
direccion = input("Escribe izquierda o derecha: ")

### Aquí abajo escribe tu código
if numero_1 == numero_2:
  if direccion == "izquierda":
    numero_1 = numero_1 + numero_2
    numero_2 = 0
  elif direccion == "derecha":
    numero_2 = numero_1 + numero_2
    numero_1 = 0
else:
  if direccion == "izquierda":
    if numero_1 == 0:
      numero_1 = numero_2
      numero_2 = 0
  elif direccion == "derecha":
    if numero_2 == 0:
      numero_2 = numero_1
      numero_1 = 0
print(str(numero_1) + " " + str(numero_2))
