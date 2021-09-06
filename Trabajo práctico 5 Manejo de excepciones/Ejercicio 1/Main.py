import Funciones as f

def main():
    edad = f.ingresa_numero("Ingrese su edad: ", 0, 125)
    print(edad)
    nota = f.ingresa_numero("Ingrese la nota: ", 1, 10)
    print(nota)
    
if __name__ == '__main__':
    main()