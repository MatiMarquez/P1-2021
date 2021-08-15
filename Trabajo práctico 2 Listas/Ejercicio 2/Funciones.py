import random

def generar_lista():
    list = []
    for i in range(50):
        list.append(random.randint(1, 101))
    return list

def verificar_repetidos(list):
    list2 = set(list)
    if len(list) != len(list2):
        bol = True
    else:
        bol = False
    return bol

def clasificar_elementos_unicos(list):
    lista2 = set(list)
    return lista2