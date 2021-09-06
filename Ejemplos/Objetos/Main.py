from dataclasses  import dataclass
from typing import List

@dataclass
class Fecha:
    dia : int
    mes : int
    anio : int

@dataclass
class Direccion:
    calle : str
    altura : int
    localidad : str

@dataclass
class Persona:
    nombre : str
    apellido : str
    direcciones : List[Direccion]
    fecha_nacimiento : Fecha

class Servicio:
    def __init__(self, nombre, costo):  # Constructor de la clase
        self.nombre = nombre
        self.costo = costo
    def __repr__(self) -> str:
        return f"Servicio(nombre = {0}, costo = {1})".format # Falta copiar

def imprimir_servicio(srv: Servicio):  # srv:    Nombre del parámetro
    print(srv.nombre, srv.costo)

def main():
    cable = Servicio("Cablevisión", 1000)
    luz = Servicio("Calp", 500)
    imprimir_servicio(cable)
    imprimir_servicio(luz)
    direc1 = Direccion("Bunge", 1200, "Pinamar")
    direc2 = Direccion("Bunge", 1300, "Pinamar")
    direcciones = [direc1, direc2]
    print(direc1)
    p = Persona("Carlos", "Perez", direcciones, Fecha(1, 1, 2001))
    print(p.fecha_nacimiento.anio)
    r = Persona("Gastón", "Dominguez", direcciones, Fecha(4, 4, 1980))
    print(r. nombre , r.apellido, r.fecha_nacimiento)

main()