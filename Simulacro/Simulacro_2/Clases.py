from dataclasses import dataclass

@dataclass
class Solicitud:
    nro_solicitud : int
    nombre : str
    zona : int
    tecnico : int

@dataclass
class Tecnico:
    legajo : int
    cant_servicios : int
    localidad_dia : int

class ValorMayorMax(Exception):
    pass
class ValorMenorMin(Exception):
    pass