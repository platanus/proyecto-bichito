from juego_base import obtener_valores, obtener_puntaje, tecla_apretada, actualizar_valores, actualizar_puntaje, iniciar
from random import randint

'''
Funciones disponibles:
    obtener_valores() -> retorna los valores en cada celda de la 0 a la 15, ordenadas de derecha a
                         izquierda arriba a abajo.
                         Ejemplo:
                            valores = obtener_valores()
                            valores[5] # es la 2da celda de la 2da fila.
    obtener_puntaje() -> retorna el puntaje actual que se muestra en el tablero.
    actualizar_valores(valores) -> recibe una lista con los valores que van a ir ahora en cada celda,
                                   luego los cambia y muestra en el tablero.
    actualizar_puntaje(puntaje) -> recibe un valor correspondiente al puntaje y lo cambia en el tablero.
    tecla_apretada() -> retorna la tecla que se haya presionado. Notar que los valores útiles son
                        'up', 'down', 'right', 'left'.
    iniciar(funcion) -> recibe la función que va a ejecutar para cada turno y muestra la interfaz.
'''


def turno():
    valores_actuales = obtener_valores()
    puntaje_actual = obtener_puntaje()
    tecla = tecla_apretada()
    print(tecla, puntaje_actual, valores_actuales)

    nuevos_valores = []
    if tecla == 'up':
        nuevos_valores = [2, 32, 512, 2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif tecla == 'down':
        nuevos_valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 256, 4096, 65536]
    elif tecla == 'right':
        nuevos_valores = [0, 0, 0, 32768, 0, 0, 0, 128, 0, 0, 0, 64, 64, 0, 0, 8]
    elif tecla == 'left':
        nuevos_valores = [4, 0, 0, 0, 64, 0, 0, 0, 1024, 0, 0, 0, 16384, 0, 0, 0]

    actualizar_valores(nuevos_valores)


# veamos un ejemplo:
# partimos con puntaje 0
actualizar_puntaje(0)
# partimos con un tablero cualquiera (debería ser aleatorio)
actualizar_valores([0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0])
# le decimos al juego que parta con nuestra función para el turno
iniciar(turno)
