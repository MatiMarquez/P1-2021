import random

def cargar_lista():
    list = []
    for i in range(50):
        list.append(random.randint(1, 10))
    print(list)
    return list

def imprimir_cantidad_numeros(list):
    suma = 0
    for nume in list:
        if nume == 5:
            suma += 1
    if suma == 0:
        print("No se encontró ningún 5")
    else:
        print("La cantidad de 5 es:", suma)

def imprimir_indice_numeros(lista):
    indices = []
    for i in range(len(lista)):
        if lista[i] == 3:
            indices.append(i)
    if len(indices) == 0:
        print("No se encontró ningún 3")
    else:
        print("Los indices encontrados de los números 3 es: ", indices)

def borrar_numeros(lista):
    largo = len(lista)
    for i in range(largo -1, -1, -1):
        if lista[i] >= 8:
            lista.pop(i)
            largo -= 1
    print("La lista quedaría así: ", lista, "y tiene", len(lista), "números" )

def main():
    lista = cargar_lista()
    imprimir_cantidad_numeros(lista)
    imprimir_indice_numeros(lista)
    borrar_numeros(lista)

main()
