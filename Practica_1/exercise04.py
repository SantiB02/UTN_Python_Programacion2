"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
suma_de_numeros = int(numero_01)+int(numero_02)+int(numero_03)+int(numero_04)

print("el resultado de la suma entre los numeros convertidos a enteros es de: ", suma_de_numeros)
# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
suma_de_numeros_string = str(numero_01) + str(numero_02) + str(numero_03) 

print("la concatenacion de los numeros convertidos a strings es de:", suma_de_numeros_string)
# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
numero_entero_1 = int(numero_binario, 2)
numero_entero_2 = int(numero_octal, 8)
numero_entero_3 = int(numero_hexadecimal, 16)

multiplicacion_de_numeros = numero_entero_1 * numero_entero_2 * numero_entero_3

print("el resultado de la multiplicacion entre los numeros convertidos a enteros es de:", multiplicacion_de_numeros)
# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
entero_1 = int(numero_01)
entero_2 = int(numero_02, 16)
entero_3 = int(numero_03, 8)
entero_4 = numero_04

resultado_resta = entero_1 - entero_2 - entero_3 - entero_4

print("el resultado de la resta secuencial de los numero convertidos a enteros es de:", resultado_resta)
# COMPLETAR - FIN

assert resultado_resta == -456350
