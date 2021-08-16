''' Escribir dos funciones para imprimir por pantalla cada uno de los siguientes 
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro.
'''
import Funciones as f

def main():
    filas = int(input("Ingrese la cantidad de filas: "))
    f.cubo(filas)
    f.escalera(filas)

if __name__ == '__main__':
    main()