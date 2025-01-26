#Conversión de unidades de temperatura

print("Selecciona una opción:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = int(input("Selecciona una opción: "))

if opcion == 1:
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}ºC son {fahrenheit}ºF")
elif opcion == 2:
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}ºF son {celsius}ºC")
else:
    print("No has seleccionado ninguna opción válida")
    exit(1)