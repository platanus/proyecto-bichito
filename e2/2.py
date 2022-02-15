#                                    eed*"""""""""**be,
#                                 .d"                  "b.
#                               .d                        b.
#                             ."         ..eeeeee..         ".
#                            P        z$*"        "*e.        9.
#                           A       d"                "b       A
#                          J       J    .e*""""""%c     A       L
#                         A       A    d"          $     L      A
#                         #       %   d      d**y  'L    %      #
#                         #       %   $     $ ,, Y  .$   %      #       _ _ 
#                         #       %   $     *  """   F   %      #      (@)@)
#                         #       V    4.    $.   .e"    Y      #        % %
#                         #        $    *.    """"     .Y      V         $ $
#                         #        'b     "b.      ..e*       Y         .eeee
#                         V         '$      ""eeee""        eP         A     %
#                          Y         eb                ..d*"         _#    O %
#                          I    _e%*""""*$ee......ee$*"eeeeeeeezee$**"       $
#                           V ,"                                            B
#                           J'                                        _,e=""
#                         .'#######################################DWB''

###################################################################################################
###################################################################################################
##                                   Proyecto 2048: Entrega 2                                    ##
##                                                                                               ##
##                                     Loops (While y For)                                       ##
##                                                                                               ##
###################################################################################################
###################################################################################################

# En esta segunda entrega vamos a implementar el ciclo de juego.
# En 2048, cuando el jugador realiza un movimiento ocurren las siguientes acciones:
#   1. Se actualiza la tabla de juego según el movimiento realizado. Si el movimiento es válido, se sigue con el punto 2.
#   2. Se crea un 2 o un 4 en una posición aleatoria (vacía) de la tabla de juego.
#   3. Se actualiza el puntaje del jugador.
#   4. Se verifica si el juego terminó.

###################################################################################################

# Ejercicio 2: Ciclo de juego: 2 turnos
#
# En este ejercicio debes permitir que el jugador realice dos movimientos en una fila de 3 elementos de la tabla del juego.
# Para este primer ejercicio, haremos que luego del primer movimiento, aparezca un 2 en la primera posición vacía disponible de izquierda a derecha.
# Veamos un ejemplo:
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
# Luego, antes de que el jugador pueda realizar otro movimiento, debemos hacer aparecer un 2 en el primer espacio vacío (el de la izquierda).
# Así, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |  2  |  4  |
#     |_____|_____|_____|
#
#
# En cambio, si desde la fila inicial hiciéramos un movimiento hacia la izquierda, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  4  |  2  |     |
#     |_____|_____|_____|
#
# Siguiendo la misma lógica, los dos elementos a la izquierda se suman, y el elemento de la derecha ocupa el lugar vacío que queda en el centro.
# Luego, antes de que el jugador pueda realizar otro movimiento, debemos hacer aparecer un 2 en el primer espacio vacío (el de la derecha).
# Así, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  4  |  2  |  2  |
#     |_____|_____|_____|
#
#
# Veamos otro ejemplo:
# Supongamos que tenemos una fila de 3 espacios pero solo uno de ellos contiene un número.
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |     |     |
#     |_____|_____|_____|
#
# Si hiciéramos un movimiento hacia la derecha, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |     |     |  2  |
#     |_____|_____|_____|
#
# El elemento de la izquierda se mueve hacia la derecha, y quedan dos espacios vacíos.
# Luego, debemos llenar el primer espacio vacío con un 2.
# Así, la fila quedaría así:
#
#      _____ _____ _____
#     |     |     |     |
#     |  2  |     |  2  |
#     |_____|_____|_____|
#
# Por otra parte, si desde la fila inicial hiciéramos un movimiento hacia la izquierda,
# este no sería válido, por lo que el turno no debería terminar, y habría que esperar 
# a que el jugador realice otro movimiento.


# Para resolver este ejercicio, vamos a tomar como base lo realizado en el ejercicio anterior
# Para este ejercicio, vamos a suponer que la casilla de la izquierda corresponde a la variable "numero_1", la del centro a la variable "numero_2" y la de la derecha a la variable "numero_3".
# En este ejercicio, vamos a recibir un input de la consola, y almacenarlo en la variable "direccion".
# Si direccion es "izquierda", vamos a tratar de mover la fila a la izquierda, y si es "derecha", vamos a tratar de mover la fila a la derecha.
# Recuerda que si dos números son distintos, no se pueden sumar, pero la fila aun puede moverse.
# Si luego de intentar realizar el movimiento, la fila se mantiene igual, entonces debemos solicitar nuevamente el input del usuario, pero no avanzar el turno.
# Si la fila cambia, entonces debes crear un número 2 en el primer espacio disponible, y luego 
# imprimir en consola el valor de las variables "numero_1", "numero_2" y "numero_3".
# Después de esto debes pedir nuevamente el input del usuario.
# En este ejercicio vamos a realizar solamente dos turnos.


# Deberás probar tu código con los siguientes valores para las variables "numero_1", "numero_2" y "numero_3":
# a)  numero_1 = 2
#     numero_2 = 0
#     numero_3 = 0
#
# b)  numero_1 = 2
#     numero_2 = 4
#     numero_3 = 0
#
# c)  numero_1 = 32
#     numero_2 = 0
#     numero_3 = 32
#
# d)  numero_1 = 32
#     numero_2 = 32
#     numero_3 = 64
#
# ¡Recuerda que tu código debe funcionar correctamente para todos los casos!

# Puedes modificar los valores de estas variables
numero_1 = 2
numero_2 = 4
numero_3 = 0
direccion = input("Escribe izquierda o derecha: ")


### Aquí abajo escribe tu código



### Fin de tu código

# Cuando hayas terminado tu código, ejecutalo escribiendo el siguiente comando en la consola:
#
# $ python 2.py
#
# ¡Puedes ejecutarlo las veces que quieras! Así podrás ir cambiando los valores de las variables y ver que sucede.
