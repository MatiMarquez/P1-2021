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

def verificar_estado(estado):
    if estado == 1:
        new_estado = 'Libre'
    elif estado == 2:
        new_estado = 'Reservado'
    else:
        new_estado = 'Vendido'
    return new_estado

def ingresar_departamento(lista_departamentos, nro_unidad):
    dpto = c.Departamento(0, "", 0, 0, 0.0)
    dpto.nro_unidad = nro_unidad
    dpto.descripcion = input("\nIngrese la descripción: ")
    dpto.mt_cuadrados = ingresar_numero("Ingrese la cantidad de Mts cuadrados: ", 0, 1000)
    estado = ingresar_numero("Ingrese el estado (1-Libre, 2-Reservado, 3-Vendido): ", 1, 3)
    dpto.estado = verificar_estado(estado)
    dpto.precio_venta = ingresar_numero("Ingrese el precio de venta: ", 0.0, 1000000.0)
    lista_departamentos.append(dpto)
    print("El departamento se guardó con éxito\n")

def ordenar_vector_ascendente(lista_departamentos):
    cambios = True
    while cambios:
        cambios = False
        for i in range(len(lista_departamentos)-1):
            if lista_departamentos[i].descripcion > lista_departamentos[i + 1].descripcion:
                cambios = True
                aux = lista_departamentos[i]
                lista_departamentos[i] = lista_departamentos[i + 1]
                lista_departamentos[i + 1] = aux
    return lista_departamentos

def emitir_listado_libre(lista_departamentos):
    lista_departamentos_ordenada = ordenar_vector_ascendente(lista_departamentos)
    lista_dpto_libres = []
    for dpto in lista_departamentos_ordenada:
        if dpto.estado == 'Libre':
            lista_dpto_libres.append(dpto)
    if len(lista_dpto_libres) > 0:
        print("El listado de departamentos libres es:\n", lista_dpto_libres,"\n")
    else:
        print("No hay ningún departamento libre para mostrar\n")

def informar_estado(lista_departamentos):
    cant_libre = 0
    cant_reservado = 0
    cant_vendido = 0
    for dpto in lista_departamentos:
        if dpto.estado == 'Libre':
            cant_libre += 1
        elif dpto.estado == 'Reservado':
            cant_reservado += 1
        else:
            cant_vendido += 1
    print("Los departamentos en cada estado son:")
    print(f'Libres: {cant_libre}\nReservados: {cant_reservado}\nVendidos: {cant_vendido}\n')

def calcular_ponderacion_tamanio(lista_departamentos, num_depto):
    ponderacion_tamanio = 0
    for dpto in lista_departamentos:
        if dpto.nro_unidad == num_depto:
            if dpto.mt_cuadrados < 100:
                ponderacion_tamanio = 10
            elif dpto.mt_cuadrados >= 100 and dpto.mt_cuadrados <= 200:
                ponderacion_tamanio = 8
            else:
                ponderacion_tamanio = 5
    return ponderacion_tamanio

def confirmar_reserva(lista_departamentos, num_depto, precio_pactado, valor_m2_minimo):
    for dpto in lista_departamentos:
        if dpto.nro_unidad == num_depto:
            if dpto.estado != 'Libre':
                if precio_pactado > valor_m2_minimo:
                    dpto.estado = 'Reservado'
                    print("Se ha reservado correctamente\n")
                    break
                else:
                    print("El precio pactado es menor al valor m2 mínimo\n")
                    break
            else:
                print("El departamento no se encuentra libre\n")
                break
    print("No se encontró el departamento seleccionado\n")

def reservar_departamento(lista_departamentos):
    num_depto = ingresar_numero("Ingrese el número del departamento a reservar: ", 0, 100)
    ponderacion_tamanio = calcular_ponderacion_tamanio(lista_departamentos,num_depto)
    ponderacion_disponibilidad = 0
    valor_m2_minimo = 1500 + 100 * ponderacion_tamanio + 200 * ponderacion_disponibilidad
    precio_pactado = ingresar_numero("Ingrese el importe de venta pactado: ", 0, 1000000000000000)
    confirmar_reserva(lista_departamentos, num_depto, precio_pactado, valor_m2_minimo)

def menu():
    lista_departamentos = []
    nro_unidad = 0
    oper = 1
    while oper != 0:
        print("MENU DE SELECCION")
        print("1- Cargar nuevo departamento")
        print("2- Emitir listado de departamentos 'Libres'")
        print("3- Mostrar cantidad de departamentos en cada estado")
        print("4- Reservar departamento")
        print("0- Salir del programa")
        oper = ingresar_numero("Ingrese una opción: ", 0, 4)
        if oper == 0:
            print("Fin programa")
            break
        elif oper == 1:
            nro_unidad += 1
            ingresar_departamento(lista_departamentos, nro_unidad)
        elif oper == 2:
            emitir_listado_libre(lista_departamentos)
        elif oper == 3:
            informar_estado(lista_departamentos)
        elif oper == 4:
            reservar_departamento(lista_departamentos)
