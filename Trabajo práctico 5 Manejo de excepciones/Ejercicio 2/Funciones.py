def sumar_dos_cadenas(cadena_1, cadena_2):
    try:
        return int(cadena_1) + int(cadena_2)
    except ValueError:
        return -1