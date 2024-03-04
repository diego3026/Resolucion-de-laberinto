from collections import deque

laberinto = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

entrada = (0, 1)
salida = (6, 12)

def imprimir_laberinto(laberinto, entrada, salida):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if (i, j) == entrada:
                print(" E ", end="")
            elif (i, j) == salida:
                print(" S ", end="")
            elif laberinto[i][j] == 1:
                print("   ", end="")
            else:
                print("###", end="")
        print()

def obtener_vecinos(posicion, laberinto):
    fila, columna = posicion
    filas = len(laberinto)
    columnas = len(laberinto[0])
    vecinos = []

    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] == 1:
            vecinos.append((nueva_fila, nueva_columna))

    return vecinos

def resolver_laberinto(laberinto, entrada, salida):
    cola = deque([entrada])
    rastro = {entrada: None}

    while cola:
        actual = cola.popleft()
        if actual == salida:
            break
        for vecino in obtener_vecinos(actual,laberinto):
            if vecino not in rastro:
                cola.append(vecino)
                rastro[vecino] = actual

    camino = []
    actual = salida
    while actual:
        camino.append(actual)
        actual = rastro[actual]

    return list(reversed(camino))

camino_solucion = resolver_laberinto(laberinto, entrada, salida)

if camino_solucion:
    print("Se encontró una solución:")
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) == entrada:
                print(" E ", end="")
            elif (fila, columna) == salida:
                print(" S ", end="")
            else:
                if (fila, columna) in camino_solucion:
                    print(" X ", end="")
                elif laberinto[fila][columna] == 1:
                    print("   ", end="")
                else:
                    print("###", end="")
        print()
else:
    print("No se encontró una solución para el laberinto.")
