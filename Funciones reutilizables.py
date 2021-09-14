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