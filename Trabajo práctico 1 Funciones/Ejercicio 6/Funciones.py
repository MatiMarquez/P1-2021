def cubo(rows):
    # Genera un cubo de asteriscos
    print("\nCUBO DE ASTERISCOS\n")
    for j in range(0, rows):
        print("*" * (rows*2), end="")
        print()
               
def escalera(rows):
    # Genera un cubo de asteriscos
    print("\nESCALERA DE ASTERISCOS\n")
    for i in range(0, rows+1):
        for j in range(0, i):
            print("**", end="")
        print()