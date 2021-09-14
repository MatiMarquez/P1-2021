from dataclasses import dataclass

@dataclass
class Departamento:
    nro_unidad : int
    descripcion : str
    mt_cuadrados : int
    estado : int
    precio_venta : float

class ValorMayorMax(Exception):
    pass
class ValorMenorMin(Exception):
    pass