def calcular_tarifa(viajes, precio):
    # Calcula el precio por la cantidad de viajes
    precio_total = viajes*precio
    if viajes>0 and viajes<=20:
        print(f"El total gastado en viajes es: {precio_total}")
    elif viajes>20 and viajes<=30:
        print(f"El total gastado en viajes es: {precio_total-(precio_total*0.20)}\n Tuvo un descuento del 20%")
    elif viajes>30 and viajes<=40:
        print(f"El total gastado en viajes es: {precio_total-(precio_total*0.30)}\n Tuvo un descuento del 30%")
    elif viajes>40:
        print(f"El total gastado en viajes es: {precio_total-(precio_total*0.40)}\n Tuvo un descuento del 40%")
    else:
        print("Ingresó una cantidad de viajes negativa o 0")        
    
def ingresar_datos():
    cantidad_viajes = int(input("Ingrese la cantidad de pasajes: "))
    valor_hoy = float(input("Ingrese el valor del pasaje actual: "))
    calcular_tarifa(cantidad_viajes, valor_hoy)