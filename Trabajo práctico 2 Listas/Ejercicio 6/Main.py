import Funciones as f

def main():
    listas = f.ingresar_lista()
    lista, lista_del = listas[0], listas[1]
    print(f'La lista principal = {lista}\nLa lista de para eliminar = {lista_del}')
    lista_new = f.eliminar_palabras_lista(lista, lista_del)
    print(f'La lista nueva = {lista_new}')

if __name__ == '__main__':
    main()