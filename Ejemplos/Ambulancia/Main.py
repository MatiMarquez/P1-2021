'''
Inicialice una matriz con la siguiente declaración: 
ambulancias=[[1000,2,5,9],[200,2,4,8],[303,4,6,5],[1000,4,4,9],[1000,6,5,8],[200,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]]
Las columnas de la matriz representan: 
Numero de ambulancia (móvil) 
Día del mes 
Cantidad de servicios 
Kilómetros recorridos 
Se le solicita que el programa: 
Cree 3 vectores para contener los siguientes datos: 
Numero de ambulancia 
Total de Servicios 
Total de Kilómetros recorridos 
Cargue los vectores acumulando los datos de la matriz por ambulancia (1 fila por ambulancia). 
Indique el móvil y el día con mayor promedio de kilómetros por servicio (a calcular sobre la matriz, es promedio diario y no total) 
Crear una función que solicite al usuario un día, valide que sea numérico, valide que sea un número entre 1 y 31 y devuelva el día ingresado. 
Utilizando la función del punto anterior solicitar al usuario un día válido e informar el móvil con mayor cantidad de servicios ese día. 
'''
import Funciones as f

def main():
    ambulancias = [[1000,2,5,9],[200,2,4,8],[303,4,6,5],[1000,4,4,9],[1000,6,5,8],[200,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]]
    ambulancias_numeros = []
    ambulancias_servicios = []
    ambulancias_kilometros = []
    
    print('Ambulancias')
    f.cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros)
    print(ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros)
    f.buscar_indice_ambulancia(ambulancias)

    dia = f.ingresar_dia()
    f.informar_ambulancia_mayor_servicio(dia, ambulancias)

if __name__ == '__main__':
    main()