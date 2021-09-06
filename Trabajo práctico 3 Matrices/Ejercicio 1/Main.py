import Funciones as f

def main():     
    datos = f.cargar_enteros_matriz()
    matriz, filas, columnas = datos[0], datos[1], datos[2] 
    print(matriz)
    # filas_ordenadas = f.ordenar_filas_matriz(matriz, filas)
    # print(matriz, filas, columnas)

if __name__ == '__main__':
    main()