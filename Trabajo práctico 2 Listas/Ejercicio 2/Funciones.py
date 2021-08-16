import random

def generar_lista():
    # Genera una lista con 50 números aleatorios del 1 al 100
    list = []
    for i in range(50):
        list.append(random.randint(1, 101))
    return list

def verificar_repetidos(list):
    # Verifica si hay algún valor repetido en la lista 
    list2 = set(list) # Uso la función Set(), no pude resolverlo sin ella
    if len(list) != len(list2):
        bol = True
    else:
        bol = False
    return bol

def clasificar_elementos_unicos(list):
    # Devuelve solamente los elementos únicos. Vuelvo a usar la función Set()
    lista2 = set(list)
    return lista2