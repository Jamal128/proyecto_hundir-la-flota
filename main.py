import random
import time 
import os
from funciones import *
from Variables import *


# Juego principal
def jugar():
    print("¡EMPIEZA LA BATALLA NAVAL!")
    # Crear tableros para el jugador y la máquina
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    # Colocar barcos en los tableros
    print("Colocando barcos...")
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    #El jugador y maquina empiezan con 0 puntos
    puntos_jugador = 0
    puntos_maquina = 0
    
    # Bucle principal del juego
    while puntos_jugador < vidas and puntos_maquina < vidas:
        #Espera 2 segundos antes de limpiar la pantalla
        time.sleep(2)
        limpiar_pantalla()

        #Muestra la tabla del jugador y de la maquina
        print("Tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("Tablero de la máquina:")
        #Cambiar ocultar_barcos a True para ocultar los barcos de la maquina
        mostrar_tablero(tablero_maquina, ocultar_barcos=False)
        
        
        print("Es tu turno:")
        #Jugador dispara al tablero de la maquina
        puntos_jugador = disparar(tablero_maquina, puntos_jugador)
        #Si puntos del jugador es igual a vidas, el jugador ha ganado
        if puntos_jugador == vidas:
            print("¡Has hundido todos los barcos de la maquina! ¡HAS GANADO!")
            break
            
        print("Es el turno de la máquina:")
        puntos_maquina = disparo_maquina(tablero_jugador, puntos_maquina)
        if puntos_maquina == vidas:
            print("La máquina ha hundido todos tus barcos. ¡HAS PERDIDO!")
            break

# Iniciar juego
jugar()