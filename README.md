# Proyecto Hundir la Flota

Este proyecto es un juego de Batalla Naval en Python, donde el jugador compite contra la máquina para hundir los barcos del oponente. El objetivo es acertar en todas las posiciones de los barcos antes de que lo haga la máquina.

## Archivos

### `main.py`:
- Contiene la lógica principal del juego.
- Se crean los tableros para el jugador y la máquina.
- Los barcos se colocan de forma aleatoria.
- Los turnos entre el jugador y la IA se alternan para disparar.
- El juego termina cuando uno de los dos hunde todos los barcos del otro.

### `funciones.py`:
Define varias funciones auxiliares clave para el funcionamiento del juego, como:

- **`limpiar_pantalla()`**: Limpia la pantalla.
- **`crear_tablero()`**: Crea un tablero vacío.
- **`mostrar_tablero()`**: Muestra el estado actual del tablero.
- **`colocar_barcos()`**: Coloca barcos en posiciones aleatorias en el tablero.
- **`disparar()`**: Permite al jugador disparar a la máquina.
- **`disparo_maquina()`**: La máquina dispara automáticamente en posiciones aleatorias.

### `Variables.py`:
Contiene las configuraciones clave del juego:

- Mapeo de letras a números para las columnas del tablero.
- Los tipos y tamaños de barcos.
- El número total de vidas o impactos necesarios para ganar.

## Cómo jugar

1. Ejecuta el archivo `main.py`.
2. Sigue las instrucciones en pantalla para disparar a las posiciones del tablero enemigo.
3. Gana el juego si logras hundir todos los barcos de la máquina antes de que la máquina hunda los tuyos.

