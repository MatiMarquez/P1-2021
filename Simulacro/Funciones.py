from random import randint
import Clases as c

def ingresar_cadena(mensaje):
    texto = str(input(mensaje))
    # No supe como poner el Try: para una cadena
    return texto

def convertir_texto_numero(mensaje, min, max):
    num = int(mensaje)
    if num < min:
        raise c.ValorMenorMin()
    if num > max:
        raise c.ValorMayorMax()
    return num

def ingresar_numero(mensaje, min, max):
    numero = 0
    while True:
        try:
            texto = input(mensaje)
            numero = convertir_texto_numero(texto, min, max)
            return numero
        except ValueError:
            print("Debe ingresar un número")
        except c.ValorMenorMin:
            print(f"El valor es menor a {min}")
        except c.ValorMayorMax:
            print(f"El valor es mayor a {max}")

def cargar_nueva_solicitud(nro_solicitud):
    solicitud = c.Solicitud(0, 0, 0, 0)
    solicitud.nro_solicitud = nro_solicitud
    solicitud.nombre = ingresar_cadena("Ingrese el nombre: ")
    solicitud.zona = ingresar_numero("Ingrese la zona (1=Pinamar, 2=Ostende, 3=Valeria, 4=Cariló): ", 1, 4)
    return solicitud

def cargar_tecnicos():
    nro_legajo = 1
    list = []
    for i in range(10):
        tecnico = c.Tecnico(0, 0)
        tecnico.nro_legajo = nro_legajo
        list.append(tecnico)
        nro_legajo += 1
    return list

def buscar_cliente_en_otra_solicitud(lista_solicitudes, solicitud):
    for i in range(len(lista_solicitudes)):
        if solicitud.nombre == solicitud[i].cliente:
            return lista_solicitudes[i].tecnico

def recorrer_solicitud(lista_solicitudes, lista_tecnicos):
    for i in range(len(lista_solicitudes)):
        if lista_solicitudes[i].tecnico != 0:
            continue
        buscar_cliente_en_otra_solicitud(lista_solicitudes, lista_solicitudes[i])