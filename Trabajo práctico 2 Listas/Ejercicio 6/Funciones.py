def ingresar_lista():
    list1 = ['Perico', 'Mauricio', 'Liliana', 'Carlos', 'Pepe', 'Juana']
    list2 = ['Tomas', 'Miguel', 'Pepe', 'Lucas', 'Carlos','Perico']
    return list1, list2

def eliminar_palabras_lista(list, delete):
    list_new = []
    for nombre in list:
        coincidir = False
        for i in range(len(delete)):
            if nombre == delete[i]:
                coincidir = True
                break
        if not coincidir:
            list_new.append(nombre)
    return list_new