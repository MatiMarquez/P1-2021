import Funciones as f

def main():
    largo = int(input("Ingrese la cantidad de números que tendrá la Clave Maestra: "))
    clave_maestra = f.generar_clave_maestra(largo)
    claves = f.descifrar_claves(clave_maestra)
    print(f"\nClave Maestra = {clave_maestra}\n")
    print(f"La clave 1 es: {claves[0]}\n")
    print(f"La clave 2 es: {claves[1]}")

if __name__ == '__main__':
    main()