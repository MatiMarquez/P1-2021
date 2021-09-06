def diadelasemana(dia,mes,anio):
    # Devuelve el día de la semana del 0 al 6
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes -2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def esBiciesto(numYear):
    if (numYear % 4 == 0): 
        if (numYear % 400 == 0): 
            return True 
        elif (numYear % 100 == 0): 
            return False
        else: 
            return True          
    else: 
        return False    

def cant_dias_mes(mes, anio):
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if esBiciesto(anio) and mes == 2:
        return 29
    return meses[mes-1]

def imprimir_calendario(mes, anio):
    print(" D  L  M  X  J  V  S")
    dias_mes= cant_dias_mes(mes, anio)
    primer_semana= True
    for dia in range(1, dias_mes + 1):
        dia_semana = diadelasemana(dia,mes,anio)
        if primer_semana:
            print("   " * dia_semana, end='')
            primer_semana= False
        if dia < 10:
            print(' ', end='')
        print(dia, end=' ')
        if dia_semana == 6:
            print()