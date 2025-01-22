edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
if (num1 < num2) and (num1 > 5):
    total = num1 + num2
    print("El resultado de la suma es:",total)
else:
    print("El operando 1 es mayor que el 2, no se puede calcular la suma")