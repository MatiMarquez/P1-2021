from dataclasses import dataclass
@dataclass
class Maquina:
    codigo : int
    hora : int
    produccion : int

def leer_archivo(nombre):
    lista  = []
    primera_vuelta = True
    with open(nombre, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if primera_vuelta:
                primera_vuelta = False
                continue
            campo = linea[:-1].split(';')
            m = Maquina(campo[0], campo[1], int(campo[2]))
            lista.append(m)
    return lista

def calcular_porcentaje(maquina, maquina_defecto):
    produccion = maquina.produccion
    defectos = maquina_defecto.produccion
    porcentaje = 100 - (((produccion - defectos)/produccion) * 100)
    if porcentaje > 2:
        return porcentaje
    return -1

def controlar_fallas_parciales(produccion, defectuoso):
    lista_maquinas_defectuosas = []
    for maquina in produccion:
        for maquina_defecto in defectuoso:
            if maquina.codigo == maquina_defecto.codigo and maquina.hora == maquina_defecto.hora:
                porcentaje = calcular_porcentaje(maquina, maquina_defecto)
                if porcentaje != -1:
                    porcentaje = round(porcentaje, 2)
                    defect = [maquina.codigo, maquina.hora, maquina.produccion, maquina_defecto.produccion, porcentaje]
                    lista_maquinas_defectuosas.append(defect)
    return lista_maquinas_defectuosas

def contar_produccion(lista, maquinas, contador_maquinas):
    for maquina in lista:
        indice = -1
        for codigo in maquinas:
            indice += 1
            if maquina.codigo == codigo:
                contador_maquinas[indice] += maquina.produccion
                break
    return contador_maquinas

def verificar_porcentaje(produccion_total, defecto_total):
    lista_porcentaje = []
    for i in range(5):
        porcentaje = 100 - (((produccion_total[i] - defecto_total[i])/produccion_total[i]) * 100)
        if porcentaje > 1:
            porcentaje = round(porcentaje, 2)
            lista_porcentaje.append(porcentaje)
        else:
            lista_porcentaje.append(0)
    return lista_porcentaje

def controlar_maquinas_defectuosas(produccion ,produccion_total, defecto_total, porcentaje_total):
    lista_maquinas_defectuosas = []
    for i in range(5):
        if porcentaje_total[i] == 0:
            continue
        else:
            maquina = [produccion[i].codigo, produccion_total[i], defecto_total[i], porcentaje_total[i]]
            lista_maquinas_defectuosas.append(maquina)
    return lista_maquinas_defectuosas

def calcular_totalidad(produccion, defectuoso):
    maquinas = 'ABCDE'
    contador_maquinas_produccion = [0, 0, 0, 0, 0]
    contador_maquinas_defectuosas = [0, 0, 0, 0, 0]
    produccion_total = contar_produccion(produccion, maquinas, contador_maquinas_produccion)
    defecto_total = contar_produccion(defectuoso, maquinas, contador_maquinas_defectuosas)
    porcentaje_total = verificar_porcentaje(produccion_total, defecto_total)
    lista_maquinas_defectuosas = controlar_maquinas_defectuosas(produccion ,produccion_total, defecto_total, porcentaje_total)
    return lista_maquinas_defectuosas
    
def crear_archivo_csv(nombre, lista, cantidad_elementos, sep):
    with open(nombre, 'w', encoding='utf-8') as archivo:
        if cantidad_elementos == 4:
            for linea in lista:
                archivo.write('{0}{4}{1}{4}{2}{4}{3}\n'.format(linea[0], linea[1], linea[2],linea[3], sep))
        elif cantidad_elementos == 5:
            for linea in lista:
                archivo.write('{0}{5}{1:>2}{5}{2:>4}{5}{3:>2}{5}{4:>5}\n'.format(linea[0], linea[1], linea[2],linea[3], linea[4], sep))

def main():
    lista_produccion = leer_archivo('produccion.csv')
    lista_calidad = leer_archivo('calidad.csv')
    fallas_parciales = controlar_fallas_parciales(lista_produccion, lista_calidad)
    maquinas_defectuosas = calcular_totalidad(lista_produccion, lista_calidad)
    crear_archivo_csv('fparciales.txt', fallas_parciales, 5, '|')
    crear_archivo_csv('fmaquinas.txt', maquinas_defectuosas, 4, '|')

if __name__ == '__main__':
    main()