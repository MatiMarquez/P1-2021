import random

def cargar_lista():
    # Carga una lista con números al azar de 4 dígitos, una cantidad de veces al azar de 2 cifras 
    list = []
    for i in range(0, random.randint(0, 99)):
        list.append(random.randint(1000, 9999))
    return list

def calcular_sumatoria(list):
    # Calcula la suma de todos los números de la lista
    for i in range(len(list)):
        if i == 0:
            sumatoria = list[i]
        else:
            sumatoria += list[i]
    return sumatoria    

def eliminar_valores(list, eli):
    # Elimina la aparición de valor específico en la lista
    posicion = 0
    while posicion < len(list):
        if list[posicion] == eli:
            list.pop(posicion)
        else:
            posicion += 1       
    return list
    
def determinar_capicua(list):
    # Determina si la lista es capicúa
    long = len(list)
    capicua = "si"
    for i in range(long):
        if list[i] != list[long-1]:
            capicua = "no"
            long -= 1
        long -= 1
    return capicua