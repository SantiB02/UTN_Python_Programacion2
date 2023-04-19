#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.

#INICIO

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
try:
    resultado = numero_1 / numero_2
except ZeroDivisionError:
    print("ERROR! No puede dividir por cero")
else:
    print("Division exitosa! El resultado es ", resultado)

#FIN