def verificar_ordenamiento(list):
    menor = list[0]
    verificacion = True
    for i in range(1, len(list)):
        if menor < list[i]:
            menor = list[i]
        else:
            verificacion = False
            break
    return verificacion




