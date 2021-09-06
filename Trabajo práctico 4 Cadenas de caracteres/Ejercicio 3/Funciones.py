import random

def generar_clave_maestra():
    # Crea la Clave Maestra
    clave = (random.randint(0,9999999999))
    clave_m = str(clave)
    return clave_m

def descifrar_claves(clave_m):
    # Descifra las dos claves
    clave_par = ''
    clave_impar = ''
    for i in range(len(clave_m)):
        if (i + 1) % 2 == 0:
            clave_par += clave_m[i]
        else:
            clave_impar += clave_m[i]
    return clave_par, clave_impar