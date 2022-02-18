# Ejercicio 3: Transformando una variable
#
# En este ejercicio, vamos a comparar dos variables, y transformar una de ellas si son iguales
# Te entregamos dos variables que tienen un valor ya asignado, y te pedimos que las compares
# Si son iguales, tienes que sumarlas, y asignar el resultado a la variable "numero_2", y asignar un 0 a la variable "numero_1". Luego, imprime el valor de la variable "numero_2".
# Si son diferentes, tienes que imprimir en consola "Son diferentes, no se pueden sumar!"

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

numero_1 = 2
numero_2 = 2

### Aquí abajo escribe tu código
if numero_1 == numero_2:
  numero_2 = numero_1 + numero_2
  numero_1 = 0
  print(numero_2)
else:
  print("Son diferentes, no se pueden sumar!")
