"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List


"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""
@dataclass #decorador que funciona como atajo para instanciar una clase (por ej: evita el uso de __init__ inicializando las variables directamente)
class Carrera:
    materias: List[str]

    def __len__(self) -> int: #método mágico (están entre guiones bajos) para saber la longitud de una instancia de la clase
        return len(self.materias)

@dataclass
class Materia:
    nombre: str

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    materia = Materia()
    assert False, "No se puede instanciar sin nombre"
except TypeError:
    assert True

try:
    materia = Carrera()
    assert False, "No se puede instanciar sin materias"
except TypeError:
    assert True

# Test básico
matematica = Materia("Matemática")
assert matematica.nombre == "Matemática"

estadistica = Materia(nombre="Estadística")
assert estadistica.nombre == "Estadística"

ciclo_basico = Carrera([matematica, estadistica])
assert (
    str(ciclo_basico)
    == "Carrera(materias=[Materia(nombre='Matemática'), Materia(nombre='Estadística')])"  # noqa: 501
)

assert len(ciclo_basico) == 2
# NO MODIFICAR - FIN
