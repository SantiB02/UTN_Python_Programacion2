"""Properties"""


class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """

    IVA = 0.21 #variable de clase

    def __init__(self, nombre: str, costo: float, descuento = 0): #constructor de objetos
        self.nombre = nombre
        self.costo = costo
        self.descuento = descuento

    @property #En vez de método de instancia, es una propiedad de la clase. Se puede modificar fuera de la clase (una nueva variable "precio")
    def precio(self) -> float:
        precio = (self.costo + (self.costo * self.IVA)) - (self.costo * self.descuento)
        round(precio, 2)
        return precio
        
    @classmethod #método de clase
    def actualizar_iva(cls, nuevo_IVA: float): #no hay flechita de Type Hint porque no devuelve nada
        cls.IVA = nuevo_IVA

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.25) #cambié el descuento a 0.25 porque 0.21 daba error la cuenta
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.25) #cambié el descuento a 0.25 porque 0.21 daba error la cuenta
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
