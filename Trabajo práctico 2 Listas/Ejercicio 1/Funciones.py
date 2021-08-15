import random

def cargar_lista():
    list = []
    for i in range(4):
        list.append(random.randint(10, 100))
    return list

def calcular_sumatoria(list):
    for i in range(len(list)):
        if i == 0:
            sumatoria = list[i]
        else:
            sumatoria += list[i]
    return sumatoria    

def eliminar_valores(list, eli):
    '''for i in range(4):
        if list[i] == eli:
            list.pop(i)
    return list'''
    posicion=0
    while posicion<len(list):
        if list[posicion] == eli:
            list.pop(posicion)
        else:
            posicion += 1       
    return list
    
def determinar_capicua(list):
    long = len(list)
    capicua = "si"
    for i in range(long):
        if list[i] != list[long-1]:
            capicua = "no"
            long -= 1
        long -= 1
    return capicua