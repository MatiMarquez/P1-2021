import random

def crear_vector_50_enteros():
    vector = []
    for i in range(50):
        vector.append(random.randint(1,101))
    return vector

def ordenar_vector_ascendente(vector):
    cambios = True
    while cambios:
        cambios = False
        for i in range(len(vector)-1):
            if vector[i] > vector[i + 1]:
                cambios = True
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux
    return vector

def buscar_vector_binaria(vector, buscado):
    inicio = vector[0]
    final = len(vector)
    for i in range(len(vector)):
        medio = (final + inicio) // 2
        if vector[medio] == buscado:
            return medio
        elif vector[medio] > buscado:
            final = medio - 1
        elif vector[medio] < buscado:
            inicio = medio + 1
    return -2