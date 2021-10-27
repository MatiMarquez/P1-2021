from dataclasses import dataclass

@dataclass
class Nombre:
    #Variable : tipo
    pass

class NombreError(Exception):
    pass

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
                campos = linea[-1].split(',')
                j = Jugada(campos[0], int(campos[1]))
                lista_jugadas.append(j)
        return lista_jugadas
    except:
        print("No se pudo abrir el archivo")
    
def main():
    nombre_archivo = 'ruleta.csv'
    generar_archivo(nombre_archivo)
    lineas_archivo = leer_archivo(nombre_archivo)

if __name__ == '__main__':
    main()