import Clases as c

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

def cargar_tecnicos(lista_tecnicos, CANT_TECN):
    for i in range(CANT_TECN):
        t1 = c.Tecnico(0, 0, 0)
        t1.legajo = 1 + i
        lista_tecnicos.append(t1)
    print("Se asignó los técnicos con éxito\n")

def cargar_solicitud(lista_solicitudes, num_solicitud):
    s1 = c.Solicitud(0,'', 0, 0)
    s1.nro_solicitud = num_solicitud
    s1.nombre = input("Ingrese el nombre: ")
    s1.zona = ingresar_numero("Ingrese la zona (1=Pinamar, 2=Ostende, 3=Valeria, 4=Cariló): ", 1, 4)
    lista_solicitudes.append(s1)
    print("Se asignó la nueva solicitud con éxito\n")

def verificar_solicitud(solicitud, lista_solicitudes, tecnico):
    for i in range(len(lista_solicitudes)):
        if solicitud.nombre == lista_solicitudes[i].nombre and lista_solicitudes[i].tecnico != 0 and tecnico.cant_servicios <= 3:
            solicitud.tecnico = lista_solicitudes[i].tecnico
            tecnico.cant_servicios += 1
            return True
    return False

def verificar_localidad_tecnico(solicitud, tecnico):
    if tecnico.cant_servicios == 1:
        if tecnico.localidad_dia == solicitud.zona:
            solicitud.tecnico = tecnico.legajo
            tecnico.cant_servicios += 1
    else:
        solicitud.tecnico = tecnico.legajo
        tecnico.cant_servicios += 1

def asignar_tecnicos(lista_solicitudes, lista_tecnicos, CANT_TECN):
    for tecnico in lista_tecnicos:
        for solicitud in lista_solicitudes:
            if solicitud.tecnico != 0:
                continue
            elif solicitud.tecnico == 0 and tecnico.cant_servicios <= 3:
                verificacion = verificar_solicitud(solicitud, lista_solicitudes, tecnico)
                if verificacion:
                    continue
                else:
                    verificar_localidad_tecnico(solicitud, tecnico)
    verificar_cargados(lista_solicitudes)

def verificar_cargados(lista_solicitudes):
    cargado = True
    for solicitud in lista_solicitudes:
        if solicitud.tecnico == 0:
            cargado = False
    if cargado:
        print("Se ha asignado correctamente los técnicos a", solicitud.nro_solicitud ,"servcio/s\n")
    else:            
        print("No se pudo cargar uno o más técnicos a los servicios\n")

def asociar_localidad(solicitud):
    if solicitud.zona == 1:
        print("* Zona = Pinamar")
    elif solicitud.zona == 2:
        print("* Zona = Ostende")
    elif solicitud.zona == 3:
        print("* Zona = Valeria del Mar")
    else:
        print("* Zona = Cariló")

def emitir_listado(lista_solicitudes):
    if len(lista_solicitudes) != 0:
        print("El Listado de Órdenes queda de esta manera:")
        for solicitud in lista_solicitudes:
            print("-" * 30)
            print("* Nro. de Solicitud =",solicitud.nro_solicitud)
            print("* Nombre del Cliente =",solicitud.nombre)
            asociar_localidad(solicitud)
            print("* Nro. de Técnico signado =",solicitud.tecnico)
            print("-" * 30)
    else:
        print("No hay solicitudes a mostrar\n")

def menu():
    CANTIDAD_TECNICOS = 2
    oper = 0
    nro_solicitud = 0
    lista_solicitudes = []
    lista_tecnicos = []
    cargar_tecnicos(lista_tecnicos, CANTIDAD_TECNICOS)
    while oper!= 6:
        print("Menú de selección")
        print("  1- Cargar una nueva solicitud")
        print("  2- Asignar técnicos a las solicitudes")
        print("  3- Emitir listado de Ordenes de Trabajo")
        print("  4- Salir del programa")  
        oper = ingresar_numero("Elija una opción para continuar: ", 1, 4)
        if oper == 4:
            print("Fin del programa")
            break
        elif oper == 1:
            nro_solicitud += 1
            cargar_solicitud(lista_solicitudes, nro_solicitud)
        elif oper == 2:
            asignar_tecnicos(lista_solicitudes, lista_tecnicos, CANTIDAD_TECNICOS)
        elif oper == 3:
            emitir_listado(lista_solicitudes)
        else:
            print("Opción incorrecta, vuelva a intentar \n")