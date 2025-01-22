# Ordenar lista de nombres

nombres = input("Introduce una lista de nombres separados por comas: ")
lista_nombres = [nombre.strip() for nombre in nombres.split(",")]
lista_nombres.sort()

print("Lista de nombres ordenados alfabéticamente:")
for nombre in lista_nombres:
    print(nombre)