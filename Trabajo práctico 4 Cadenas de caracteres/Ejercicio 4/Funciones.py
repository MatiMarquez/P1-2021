'''def convertir_entero_romano(num):
    m = num // 1000
    num = num - (1000 * m)
    d = num // 500
    
    if d > 3:
        d = 'CD'
        num = num - 400
    else:
        num = num - (500 * d)
    
    num = num - (100 * c)
    l = num // 50
    num = num - (50 * l)
    x = num // 10
    num = num - (10 * x)

    resto = verificar_terminacion(num)
    concatenar(m, d, c, l, x, resto)
    
def verificar_terminacion(num):
    if num == 4:
        resto = 'IV'
    elif num == 9:
        resto = 'I'
    else:
        v = num // 5
        num = num - (5 * v)
        i = num // 1
        resto = 'V' * v + 'I' * i
        return resto

def concatenar(m, d, c, l, x, resto):
    print('M' * m + 'D' * d +'C' * c + 'L' * l + 'X' * x + resto)
'''
def convertir_entero_romano(num):
    list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for i in range(len(list)):
        if num >= list[i]:
            valor = num // list[i]
            num = num - (list[i] * valor)
            if list[i] == list[0]:
                print('M' * valor, end='')
            elif list[i] == list[1]:
                print('CM' * valor, end='')
            elif list[i] == list[2]:
                print('D' * valor, end='')
            elif list[i] == list[3]:
                print('CD' * valor, end='')
            elif list[i] == list[4]:
                print('C' * valor, end='')
            elif list[i] == list[5]:
                print('XC' * valor, end='')
            elif list[i] == list[6]:
                print('L' * valor, end='')
            elif list[i] == list[7]:
                print('XL' * valor, end='')
            elif list[i] == list[8]:
                print('X' * valor, end='')
            elif list[i] == list[9]:
                print('IX' * valor, end='')
            elif list[i] == list[10]:
                print('V' * valor, end='')
            elif list[i] == list[11]:
                print('IV' * valor, end='')
            elif list[i] == list[12]:
                print('I' * valor, end='')