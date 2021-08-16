''' Desarrollar una función que reciba tres números positivos y 
devuelva el mayor de los tres, sólo si éste es unico (mayor estricto).
'''
import Funciones as f

def main():
    numeros = f.ingresar_numeros()
    f.reconocer_mayor_estricto(numeros)

if __name__ == '__main__':
    main()