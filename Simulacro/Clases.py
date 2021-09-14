from dataclasses import dataclass

@dataclass
class Tecnico:
    nro_legajo : str
    cant_solicitud : int

@dataclass
class Solicitud:
    nro_solicitud : str
    nombre : str
    zona : int
    tecnico : int

class ValorMayorMax(Exception):
    pass
class ValorMenorMin(Exception):
    pass