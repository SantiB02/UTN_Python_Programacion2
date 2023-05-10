""" Se desea crear un programa que simule el funcionamiento basico de un vehiculo.

-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo. """

class Vehiculo:
    def __init__(self, marca, ruedas, color):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = False
    
    def arrancar(self):
        self.enMarcha = True

    def tipoVehiculo(self):
        if self.ruedas == 4:
            print("Automovil")
        elif self.ruedas == 2:
            print("Motocicleta")
    
    def mostrar(self):
        print("Marca:", self.marca, "Ruedas:", self.ruedas, "Color:", self.color, "En marcha:", self.enMarcha)

autito = Vehiculo('Ford', 4, 'Azul')
autito.arrancar()
autito.tipoVehiculo()
autito.mostrar()