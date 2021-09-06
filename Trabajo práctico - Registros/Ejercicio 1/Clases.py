from dataclasses import dataclass
from typing import List

@dataclass
class Fecha:
    dia : int
    mes : int
    anio : int

@dataclass
class Horario:
    horas : int
    minutos : int
    segundos : int

@dataclass
class Producto:
    nombre : str
    precio_unitario : float
    fecha: Fecha

class ValorMayorMax(Exception):
    pass
class ValorMenorMin(Exception):
    pass