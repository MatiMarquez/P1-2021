''' Desarrollar cada una de las siguientes funciones y escribir un programa que permita 
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función
'''
import Funciones as f

def main():     
    lista = f.cargar_lista()
    print(f"La lista creada es: {lista}")
    suma = f.calcular_sumatoria(lista)
    print(f"La sumatoria de la lista es: {suma}")
    eliminar = int(input("Ingrese un número para eliminar: "))
    lista = f.eliminar_valores(lista, eliminar)
    print(f"La nueva lista queda así {lista}")
    verificacion_capicua = f.determinar_capicua(lista)
    print(f"La lista {verificacion_capicua} es capicúa")

if __name__ == '__main__':
    main()