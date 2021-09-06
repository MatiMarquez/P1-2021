import Funciones as f

def main():
    vector = f.crear_vector_50_enteros()
    print("El vector es:", vector,"\n")
    vector_ordenado = f.ordenar_vector_ascendente(vector)
    print("El vector ordenado es:", vector_ordenado,"\n")
    nume = int(input("Ingrese un número a buscar: "))
    indice = f.buscar_vector_binaria(vector, nume)
    print(f"La posición en donde está el número {nume} es: {indice+1}")

if __name__ == '__main__':
    main()