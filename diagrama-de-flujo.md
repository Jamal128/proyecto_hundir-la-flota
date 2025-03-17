```mermaid
flowchart TD
    A[Inicio] --> B[Importar bibliotecas]
    B --> C[Definir funciones]
    
    subgraph Funciones["Funciones"]
        C1[limpiar_pantalla]
        C2[crear_tablero]
        C3[mostrar_tablero]
        C4[colocar_barcos]
        C5[disparar]
        C6[disparo_maquina]
    end
    
    C --> C1
    C1 --> C1_1[Ejecutar os.system'cls']
    
    C2 --> C2_1[Crear matriz 10x10 con espacios]
    C2_1 --> C2_2[Retornar tablero vacío]
    
    C --> C3
    C3 --> C3_1[Mostrar cabecera A-J]
    C3_1 --> C3_2[Recorrer filas y columnas]
    C3_2 --> C3_3{ocultar_barcos?}
    C3_3 -->|Sí| C3_4[Ocultar B mostrando espacio]
    C3_3 -->|No| C3_5[Mostrar contenido real]
    C3_4 --> C3_6[Mostrar línea inferior]
    C3_5 --> C3_6
    
    C --> C4
    C4 --> C4_1[Recorrer tipos de barcos]
    C4_1 --> C4_2[Generar posición aleatoria]
    C4_2 --> C4_3[Generar dirección aleatoria]
    C4_3 --> C4_4{Dirección?}
    C4_4 -->|Norte| C4_5[Verificar límites y colisiones]
    C4_4 -->|Sur| C4_6[Verificar límites y colisiones]
    C4_4 -->|Este| C4_7[Verificar límites y colisiones]
    C4_4 -->|Oeste| C4_8[Verificar límites y colisiones]
    C4_5 --> C4_9{Posición válida?}
    C4_6 --> C4_9
    C4_7 --> C4_9
    C4_8 --> C4_9
    C4_9 -->|No| C4_2
    C4_9 -->|Sí| C4_10[Colocar barco en tablero]
    C4_10 --> C4_11{Más barcos?}
    C4_11 -->|Sí| C4_1
    C4_11 -->|No| C4_12[Fin colocación]
    
    C --> C5
    C5 --> C5_1[Solicitar coordenadas]
    C5_1 --> C5_2{Formato válido?}
    C5_2 -->|No| C5_1
    C5_2 -->|Sí| C5_3[Extraer letra y número]
    C5_3 --> C5_4{Coordenadas válidas?}
    C5_4 -->|No| C5_1
    C5_4 -->|Sí| C5_5[Convertir a índices]
    C5_5 --> C5_6{Ya disparado?}
    C5_6 -->|Sí| C5_1
    C5_6 -->|No| C5_7{Acierto?}
    C5_7 -->|Sí| C5_8[Marcar X y sumar contador]
    C5_7 -->|No| C5_9[Marcar O]
    C5_8 --> C5_10[Retornar contador]
    C5_9 --> C5_10
    
    C --> C6
    C6 --> C6_1[Generar coordenadas aleatorias]
    C6_1 --> C6_2{Ya disparado?}
    C6_2 -->|Sí| C6_1
    C6_2 -->|No| C6_3{Acierto?}
    C6_3 -->|Sí| C6_4[Marcar X y sumar contador]
    C6_3 -->|No| C6_5[Marcar O]
    C6_4 --> C6_6[Retornar contador]
    C6_5 --> C6_6