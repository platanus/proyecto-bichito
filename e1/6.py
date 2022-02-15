#                                    ,__                   __
#                                    '~~****Nm_    _mZ*****~~
#                                            _8@mm@K_
#                                           W~@`  '@~W
#                                          ][][    ][][
#                                    gz    'W'W.  ,W`W`    es
#                                  ,Wf    gZ****MA****Ns    VW.
#                                 gA`   ,Wf     ][     VW.   'Ms
#                                Wf    ,@`      ][      '@.    VW
#                                M.    W`  _mm_ ][ _mm_  'W    ,A
#                                'W   ][  i@@@@i][i@@@@i  ][   W`
#                                 !b  @   !@@@@!][!@@@@!   @  d!
#                                  VWmP    ~**~ ][ ~**~    YmWf
#                                    ][         ][         ][
#                                  ,mW[         ][         ]Wm.
#                                 ,A` @  ,gms.  ][  ,gms.  @ 'M.
#                                 W`  Yi W@@@W  ][  W@@@W iP  'W
#                                d!   'W M@@@A  ][  M@@@A W`   !b
#                                @.    !b'V*f`  ][  'V*f`d!    ,@
#                                'Ms    VW.     ][     ,Wf    gA`
#                                  VW.   'Ms.   ][   ,gA`   ,Wf
#                                   'Ms    'V*mmWWmm*f`    gA`

###################################################################################################
###################################################################################################
##                                   Proyecto 2048: Entrega 1                                    ##
##                                                                                               ##
##                                 Variables y Control de Flujo                                  ##
##                                                                                               ##
###################################################################################################
###################################################################################################

# En esta primera entrega, vamos a implementar algunas funcionalidades más básicas del juego 2048.
# En este juego, las piezas pueden tomar el valor de 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048.
# Además, para ayudarnos a desarrollar el juego, vamos a asumir que una casilla vacía tiene un valor de 0.
# Para que dos piezas puedan sumarse, deben tener el mismo valor.

###################################################################################################

# Ejercicio 6: Movimiento generalizado con dos celdas
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

# Puedes modificar los valores de estas variables
numero_1 = 0
numero_2 = 64
direccion = input("Escribe izquierda o derecha: ")

### Aquí abajo escribe tu código



### Fin de tu código

# Cuando hayas terminado tu código, ejecutalo escribiendo el siguiente comando en la consola:
#
# $ python 6.py
#
# ¡Puedes ejecutarlo las veces que quieras! Así podrás ir cambiando los valores de las variables y ver que sucede.
