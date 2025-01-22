# Números pares en un rango

inicio = int(input("Introduce el primer número del rango: "))
fin = int(input("Introduce el último número del rango: "))

print("Los números pares entre ", inicio, " y ", fin, " son:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)