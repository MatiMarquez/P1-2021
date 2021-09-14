import Funciones as f
import Clases as c

def menu(oper, nro_solicitud, nro_legajo, list_s, list_t):
    # Muestra un menú de opciones     
    while oper!= '6':
        print("\nMenú de selección")
        print("  1- Cargar una nueva solicitud")
        print("  2- Recorrer lista de solicitudes")
        print("  3- Emitir listado de Ordenes de Trabajo")
        print("  4- Salir del programa")  
        oper = input("Elija una opción para continuar: ")
        if oper == '4':
            print("Fin del programa")
            break
        elif oper == '1':
            nro_solicitud += 1
            nueva_solicitud = f.cargar_nueva_solicitud(nro_solicitud)
            list_s.append(nueva_solicitud)
            print("Se asignó la nueva solicitud con éxito\n", nueva_solicitud)
        elif oper == '2':
            f.recorrer_solicitud(list_s, list_t)
        elif oper == '3':
            pass
        else:
            print("Opción incorrecta, vuelva a intentar \n")


def main():
    list_tecnicos = f.cargar_tecnicos()
    lista_solicitud = []
    menu(0, 0, 0, lista_solicitud, list_tecnicos)


if __name__ == '__main__':
    main()