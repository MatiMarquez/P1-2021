import random

def generar_clave_maestra():
    # Crea la Clave Maestra
    clave_m = (random.randint(0,9999999999))
    clave_maestra = str(clave_m)
    return clave_maestra

def descifrar_claves(clave_m):
    # Descifra las dos claves
    clave_uno = ''
    clave_dos = ''
    pares = ['0', '2', '4', '6', '8']
    for i in range(0, len(clave_m)):
        if clave_m[i] in pares:
            clave_dos += clave_m[i] 
        else:
            clave_uno += clave_m[i]
    return clave_uno, clave_dos