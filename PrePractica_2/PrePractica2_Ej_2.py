#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

lista_og = []
lista_impares = []
tamanio = int(input("Ingrese cantidad de numeros a ingresar: "))

for i in range(tamanio):
    lista_og.append(int(input("Ingrese un numero: ")))
    if lista_og[i] % 2 == 1:
        lista_impares.append(lista_og[i])

print("Lista de numeros originales:")
print(lista_og)
print("Lista de numeros impares:")
print(lista_impares)

#FIN