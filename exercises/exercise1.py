"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

area_cuadrado = lado_cuadrado * lado_cuadrado

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

area_cuadrado = lado_cuadrado**2

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO

cociente = presupuesto_disponible // precio
resto = presupuesto_disponible % precio

if resto == 0:
    unidades_a_comprar = cociente
else:
    unidades_a_comprar = cociente + 1

# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO

resto = numero_incalculable
ultimo_digito = 0

while resto > 0:
    ultimo_digito = resto % 10
    resto = (resto - ultimo_digito) // 10 - 2 * ultimo_digito

if resto % 7 == 0:
    print(numero_incalculable, "es divisible por 7")
else:
    print(numero_incalculable, "no es divisible por 7")


# COMPLETAR - FIN

assert es_divisible_por_siete