import Clases as c

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

def cargar_horario():
    horario = c.Horario(0, 0, 0)
    horario.horas = ingresar_numero("Ingrese la hora: ", 0, 23)
    horario.minutos = ingresar_numero("Ingrese los minutos: ", 0, 60)
    horario.segundos = ingresar_numero("Ingrese los segundos: ", 0, 60)
    return horario