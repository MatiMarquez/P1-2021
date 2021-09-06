INDICE_NUMERO_AMBULANCIA = 0
INDICE_DIA_AMBULANCIA = 1
INDICE_SERVICIO_AMBULANCIA = 2
INDICE_KILOMETRO_AMBULANCIA = 3

class ErrorValorMinimo(Exception):
    pass
class ErrorValorMaximo(Exception):
    pass

def inicializar_vector(vector, cantidad, valor_inicial):
    for i in range(cantidad):
        vector.append(valor_inicial)

def cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros):
    for ambulancia in ambulancias:
        if ambulancia[INDICE_NUMERO_AMBULANCIA] not in ambulancias_numeros:
            ambulancias_numeros.append(ambulancia[INDICE_NUMERO_AMBULANCIA])

    tamanio = len(ambulancias_numeros)
    inicializar_vector(ambulancias_kilometros, tamanio, 0)
    inicializar_vector(ambulancias_servicios, tamanio, 0)


    for j in range(len(ambulancias_numeros)):
        for ambulancia in ambulancias:
            if ambulancias[INDICE_NUMERO_AMBULANCIA] == ambulancias_numeros[j]:
                ambulancias_servicios[j] += ambulancia[INDICE_SERVICIO_AMBULANCIA]
                ambulancias_kilometros[j] += ambulancia[INDICE_KILOMETRO_AMBULANCIA]

def buscar_indice_ambulancia(ambulancias):
    indice_mayor = 0 
    for i in range(len(ambulancias)):
        promedio_i = ambulancias[i][INDICE_KILOMETRO_AMBULANCIA]/ambulancias[i][INDICE_SERVICIO_AMBULANCIA] 
        promedio_mayor = ambulancias[indice_mayor][INDICE_KILOMETRO_AMBULANCIA]/ambulancias[indice_mayor][INDICE_SERVICIO_AMBULANCIA]
        if promedio_i > promedio_mayor:
            indice_mayor = i
            promedio_mayor = promedio_i
    return indice_mayor

def ingresar_numero(mensaje, valmin, valmax):
    ingreso_usuario = int(input(mensaje))
    if ingreso_usuario < valmin:
        raise ErrorValorMinimo
    elif ingreso_usuario > valmax:
        raise ErrorValorMaximo
    return ingreso_usuario

def ingresar_dia():
    while True:
        try:
            dia = ingresar_numero(("Ingrese el número de día: "), 0, 31)
            return dia
        except ValueError:
            print("Debe ingresar un número entero")
        except ErrorValorMinimo:
            return 1
        except ErrorValorMaximo:
            print("Debe ingresar un número día válido")

def informar_ambulancia_mayor_servicio(dia, ambulancias):
    mayor_i = -1
    for i in range(len(ambulancias)):
        if dia == ambulancias[i][INDICE_DIA_AMBULANCIA]:
            if mayor_i == -1:
                mayor_i = i
            if ambulancias[i][INDICE_SERVICIO_AMBULANCIA] > ambulancias[mayor_i[INDICE_SERVICIO_AMBULANCIA]]:
                 mayor_i = i
    print("El movil de mayor cantidad de servicios es,", ambulancias[mayor_i][INDICE_NUMERO_AMBULANCIA])
