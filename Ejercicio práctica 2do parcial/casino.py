import random
from dataclasses import dataclass

@dataclass
class Jugada:
    ruleta : str
    numero : int

def generar_archivo(nombre_archivo):
    ruleta = 'ABCD'
    with open (nombre_archivo, 'w', encoding='utf-8') as archivo:
        for i in range(1000):
            for i in ruleta:
                numero = random.randint(0, 36)
                archivo.write(f'{i},{numero}\n')
        
def leer_archivo(nombre_archivo):
    lista_jugadas = []
    try:
        with open(nombre_archivo, 'r',encoding='utf-8') as arch:
            for linea in arch:
                campos = linea[:-1].split(',')
                j = Jugada(campos[0], int(campos[1]))
                lista_jugadas.append(j)
        return lista_jugadas
    except:
        print("No se pudo abrir el archivo")

def iniciar_matriz():
    matriz = []
    for filas in range(37):
        lista = []
        for columnas in range(4):
            lista.append(0)
        matriz.append(lista)
    return matriz

def decodificar(letra):
    if letra == 'A':
        return 0
    elif letra == 'B':
        return 1
    elif letra == 'C':
        return 2
    return 3

def calcular_totales(lista):
    matriz = iniciar_matriz()
    for jugada in lista:
        matriz[jugada.numero][decodificar(jugada.ruleta)] += 1
    return matriz

def calcular_frecuencias(totales):
    for r in range(4):
        contador = 0
        for i in range(len(totales)):
            contador += totales[i][r]
            if contador != 0:
                for j in range(len(totales)):
                    totales[i][r] = totales[i][r]/contador
    print(totales)
    return totales

def mostrar_frecuencias(listado):
    print('|{0:^12}|{1:^12}|{2:^12}|{3:^12}|{4:^12}|'.format('Numero','Frecuencia A','Frecuencia B','Frecuencia C','Frecuencia D'))
    for listaInd in range(len(listado)):
        print('|{0:^12}|{1:^.10f}|{2:^.10f}|{3:^.10f}|{4:^.10f}|'.format(listaInd,listado[listaInd][0],listado[listaInd][1],listado[listaInd][2],listado[listaInd][3]))

def buscar_incidencias(frecuencias):
    incidencias = []
    for columna in range(4):
        for fila in range(len(frecuencias)):
            desvio = abs(frecuencias[fila][columna] - 1/37)
            if abs(desvio) > 0.005:
                incidencias.append([columna, fila, frecuencias[fila][columna], desvio])
    return incidencias

def mostrar_incidencias(incidencias):
    print('|{0:^12}|{1:^12}|{2:^12}|{3:^12}|{4:^12}|'.format('Columna','Frecuencia A','Frecuencia B','Frecuencia C','Frecuencia D'))
    for fila in incidencias:
        print('|{0:^12f}|{1:^10f}|{2:^10f}|{3:^10f}|{4:^10f}|'.format(incidencias[0], incidencias[1], incidencias[2], incidencias[3]))

def main():
    nombre_archivo = 'ruleta.csv'
    generar_archivo(nombre_archivo)
    lista_jugadas = leer_archivo(nombre_archivo)
    totales = calcular_totales(lista_jugadas)
    frecuencias = calcular_frecuencias(totales)
    mostrar_frecuencias(frecuencias)
    incidencias = buscar_incidencias(frecuencias)
    mostrar_incidencias(incidencias)

if __name__ == '__main__':
    main()