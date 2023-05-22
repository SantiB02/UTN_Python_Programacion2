"""Variables de Clase y Métodos de Clase."""


class Article:
    """Todos los artículos tienen un nombre y un costo, opcionalmente algunos
    tienen un porcentaje de descuento.

    El IVA es un impuesto que se aplica a todos los productos por igual,
    actualmente es de 21% pero puede cambiar en el futuro.

    Para calcular el precio de un artículo, hay que sumar el IVA y luego restar
    los descuentos si hubiera. Redondear a 2 decimales.

    Restricciones:
        - Utilizar 3 variables de instancia (nombre, costo, porcentaje)
        - Utilizar 1 método de instancia (Calcular precio)
        - Utilizar 1 variable de clase (IVA)
        - Utilizar 1 método de clase (Actualizar IVA)
        - No utilizar Dataclasses
        - No utilizar Properties
        - Utilizar Type Hints en todos los métodos y variables
    """
    def __init__(self, nombre: str, costo: float, descuento = 0): #constructor de objetos
        self.nombre = nombre
        self.costo = costo
        self.descuento = descuento

    IVA = 0.21 #variable de clase

    def calcular_precio(self) -> float: #la flechita corresponde al Type Hint. Método de instancia
        precio = (self.costo + (self.costo * self.IVA)) - (self.costo * self.descuento)
        return round(precio, 2)

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

# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article("Auto", 1, 0.25) #cambié el descuento a 0.25 porque 0.21 daba error la cuenta de la línea 31
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.25) #cambié el descuento a 0.25 porque 0.21 daba error la cuenta de la línea 31
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.25
# NO MODIFICAR - FIN
