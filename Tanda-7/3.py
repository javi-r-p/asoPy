# Crear una función para comprobar números primos

numero = int(input("Introduce un número: "))

def comprobar(i):
    if i < 2:
        return False
    for j in range(2, int(i*0.5) +1):
        if i % j == 0:
            return False
    return True

if comprobar(numero):
    print("El número", numero, "es primo.\n")
else:
    print("El número", numero, "no es primo.\n")

for i in range(1, 101):
    if comprobar(i):
        print(i)