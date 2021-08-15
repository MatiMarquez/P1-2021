import Funciones as f

def main():
    lista = f.generar_lista()
    print(lista)
    boolean = f.verificar_repetidos(lista)
    print(boolean)
    nueva_lista = f.clasificar_elementos_unicos(lista)
    print(nueva_lista)

if __name__ == '__main__':
    main()