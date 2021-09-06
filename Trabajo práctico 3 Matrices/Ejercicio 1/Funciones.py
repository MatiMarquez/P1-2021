def cargar_enteros_matriz():
    matriz = []
    columna = int(input("Ingrese la cantidad de columas para la matriz "))
    fila = int(input("Ingrese la cantidad de filas para la matriz "))
    for i in range(columna):
        matriz.append([])
        for j in range(fila):
            num = int(input("Ingrese un número para cargar: "))
            matriz[i].append(num)
    return (matriz, fila, columna)
'''
def ordenar_filas_matriz(matriz, fila):
    mayor = matriz[0][0]
    print(mayor)
    for i in range(1, fila-1):
        if matriz[i][0] < mayor:
            aux = []
            for j in range(fila):
                aux[i].append(matriz[i + 1][j])
            for x in range(fila):
                pass

    return mayor 
'''
