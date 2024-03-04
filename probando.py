

movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for movimiento in movimientos:
    nueva_fila = fila + movimiento[0]
    nueva_columna = columna + movimiento[1]
    print(movimiento)

def obtener_vecinos(posicion, laberinto):
    fila, columna = posicion
    filas = len(laberinto)
    columnas = len(laberinto[0])
    vecinos = []

    # Coordenadas de los movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        # Verificar si la nueva posición está dentro del laberinto y es un pasillo
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] == 1:
            vecinos.append((nueva_fila, nueva_columna))

    return vecinos

def resolver_laberinto(laberinto, entrada, salida):
    cola = deque([entrada])
    padres = {entrada: None}

    while cola:
        actual = cola.popleft()
        if actual == salida:
            break
        for vecino in obtener_vecinos(actual,laberinto):
            if vecino not in padres:
                cola.append(vecino)
                padres[vecino] = actual

    # Reconstruir el camino desde la salida hasta la entrada
    camino = []
    actual = salida
    while actual:
        camino.append(actual)
        actual = padres[actual]

    return list(reversed(camino))    