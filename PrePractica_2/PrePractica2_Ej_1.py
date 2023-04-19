#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

numero_1 = input("Ingrese el primer número: ")
numero_2 = input("Ingrese el segundo número: ")
numero_max = max(numero_1, numero_2)
##numero_max = numero_1 if numero_1 > numero_2 else numero_2
print("El número mayor es ", numero_max)

#FIN