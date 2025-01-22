# Gestión de un inventario simple

from pathlib import Path

archivo = Path("inventario.txt")

print(" --- MENÚ ---")
print("1. Ver inventario")
print("2. Añadir un objeto al inventario")
opcion = int(input("Selecciona una opción: "))

if opcion == 1:
    print("Has elegido ver el inventario.")
    print("Elementos del inventario:")
    archivo.open("r")
    for objeto in archivo.read_text().split():
        print(objeto)
elif opcion == 2:
    print("Has elegido añadir un objeto al inventario.")
    objetoNuevo = input("Introduce el objeto que quieres añadir: ")
    with archivo.open("a") as archivo:
        archivo.write(objetoNuevo+"\n")
else:
    print("No has seleccionado una opción válida.")
    exit(1)