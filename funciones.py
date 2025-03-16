import random
import time 
import os
from Variables import *

# Limpiar la pantalla 
def limpiar_pantalla():
    os.system('cls')

# Crear tablero vacío
def crear_tablero():
    return [[" " for _ in range(10)] for _ in range(10)]

# Mostrar tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("    A B C D E F G H I J")
    print("   +-+-+-+-+-+-+-+-+-+-+")
    
    #Pongo numeros a la izquierda 
    for i in range(10):
        print(f"{i+1:2} |", end="")
        for j in range(10):
            if ocultar_barcos and tablero[i][j] == 'B':
                print(" |", end="")
            else:
                print(f"{tablero[i][j]}|", end="")
        print()
    print("   +-+-+-+-+-+-+-+-+-+-+")

# Colocar barcos
def colocar_barcos(tablero):
    for nombre, tamaño in barcos.items():
        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            direccion = random.choice(['N', 'S', 'E', 'O'])
            
            # Comprobar si cabe en esa dirección
            valido = True
            if direccion == 'N' and fila - tamaño + 1 >= 0:
                for i in range(tamaño):
                    if tablero[fila - i][columna] != ' ':
                        valido = False
                        break
            elif direccion == 'S' and fila + tamaño <= 10:
                for i in range(tamaño):
                    if tablero[fila + i][columna] != ' ':
                        valido = False
                        break
            elif direccion == 'E' and columna + tamaño <= 10:
                for i in range(tamaño):
                    if tablero[fila][columna + i] != ' ':
                        valido = False
                        break
            elif direccion == 'O' and columna - tamaño + 1 >= 0:
                for i in range(tamaño):
                    if tablero[fila][columna - i] != ' ':
                        valido = False
                        break
            else:
                valido = False
            
            # Colocar el barco si es válido
            if valido:
                if direccion == 'N':
                    for i in range(tamaño):
                        tablero[fila - i][columna] = 'B'
                elif direccion == 'S':
                    for i in range(tamaño):
                        tablero[fila + i][columna] = 'B'
                elif direccion == 'E':
                    for i in range(tamaño):
                        tablero[fila][columna + i] = 'B'
                else:  # Oeste
                    for i in range(tamaño):
                        tablero[fila][columna - i] = 'B'
                break

# Disparar
def disparar(tablero, contador):
    while True:
        coordenada = input("Dispara (ej: A1): ").upper()
        # Comprobar si la coordenada tiene al menos 2 caracteres y no mas de 3
        if len(coordenada) < 2 or len(coordenada) > 3:
            print("Porfavor Introduce una coordenada correcta. Usa letra (A-J) + número (1-10)")
            continue
        
        # Asignar letra y número a las variables letra y número 
        # (Columna y fila) (A1, B2, C3, etc) 
        # [0] = A, [1:] = 1

        letra = coordenada[0]
        numero = coordenada[1:] 
        
        # Comprobar si la letra y el número son válidos
        if letra not in letras or not numero.isdigit() or int(numero) < 1 or int(numero) > 10:
            print("Coordenada inválida.")
            continue
        
        # Convertir el número a un índice de fila
        #Resta 1 porque va de 0 a 9 y no de 1 a 10
        fila = int(numero) - 1
        # Convertir la letra a un índice de columna 
        columna = letras[letra]
        
        # Comprueba si ya ha disparado en esa casilla
        if tablero[fila][columna] in ['X', 'O']:
            print("Ya has disparado en esa casilla.")
            continue

        # Comprueba si ha acertado el disparo
        if tablero[fila][columna] == 'B':
            tablero[fila][columna] = 'X'
            print("¡LE HAS DADO AL BARCO!")
            contador += 1
        else:
        # Si no ha acertado el disparo
            tablero[fila][columna] = 'O'
            print("¡AL AGUAAAAAA!")
        
        return contador

def disparo_maquina(tablero, contador):
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        # Verifica si la máquina ya ha disparado en esa casilla
        if tablero[fila][columna] in ['X', 'O']:
            print(f"La máquina ya ha disparado en esta casilla.")
            continue  # Si ya se ha disparado en esa casilla, intenta con una nueva coordenada

        # Comprueba si ha acertado el disparo
        if tablero[fila][columna] == 'B':
            tablero[fila][columna] = 'X'
            print(f"¡LA MÁQUINA HA DISPARADO AL BARCO!")
            contador += 1
        else:
        # Si no ha acertado el disparo
            tablero[fila][columna] = 'O'
            print(f"¡LA MÁQUINA HA DISPARADO AL AGUAAAA!")
        
        return contador