def determinar_capicua_cadena(cadena):
    largo = len(cadena)-1
    for letra in cadena:
        if letra != cadena[largo]:
            return 'no es capicúa'
        else:
            largo -= 1
    return 'es capicúa'