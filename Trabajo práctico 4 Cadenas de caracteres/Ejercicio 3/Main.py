''' Los números de claves de dos cajas fuertes están intercalados dentro de un
número entero llamado "Clave Maestra", cuya longitud se desconoce.
'''
import Funciones as f

def main():
    clave_maestra = f.generar_clave_maestra()
    claves = f.descifrar_claves(clave_maestra)
    print(f"\nClave Maestra = {clave_maestra}\n")
    print(f"La clave 1 es: {claves[0]}\n")
    print(f"La clave 2 es: {claves[1]}")

if __name__ == '__main__':
    main()