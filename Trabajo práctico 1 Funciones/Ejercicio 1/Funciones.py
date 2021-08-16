def mayor(num1, num2, num3):
    # De tres números devuelve el mayor
    maximo = num1
    igual = False
    maximo = num1
    if num2 != maximo:
        if num2 > maximo:
            maximo = num2
            igual = False
    else:
        igual = True
    if num3 != maximo:
        if num3 > maximo:
            maximo = num3
            igual = False
    else:
        igual = True  
    if igual == False:
        return maximo
    else:
        return -1

def ingresar_numeros():
    # Ingreso de números
    nume1 = int(input("Ingrese el primer número: "))
    nume2 = int(input("Ingrese el segundo número: "))
    nume3 = int(input("Ingrese el tercer número: "))
    return nume1, nume2, nume3

def reconocer_mayor_estricto(num):
    # Devuelve el mayor estricto o un informe
    numero_mayor = mayor(num[0], num[1], num[2])
    if numero_mayor == -1:
        print(f"El número máximo no es estricto")
    else:
        print(f"El número máximo hallado es: {numero_mayor}")