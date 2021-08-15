# Ejercicio 3
import random

def generar_clave_maestra(long):
    clave_m = []
    for i in range(0, long):
        clave_m.append(random.randint(0,9))
    return clave_m

def descifrar_claves(clave_m):
    clave_uno , clave_dos = [], []
    for i in range(0, len(clave_m)):
        if clave_m[i] % 2 == 0:
            clave_dos.append(clave_m[i])
        else:
            clave_uno.append(clave_m[i])
    return clave_uno, clave_dos        