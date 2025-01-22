# Gestión de un inventario simple

from pathlib import Path

archivo = Path("inventario.txt")

print(" --- MENÚ ---")
print("1. Ver inventario")
print("2. Añadir un objeto al inventario")
#print("3. Eliminar un objeto del inventario")
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
    archivo = open("inventario.txt", "a")
    archivo.write_text(objetoNuevo)
#elif opcion == 3:
#   print("Has elegido eliminar un objeto del inventario.")
#   elementoEliminar = input("Introduce el objeto que quieres eliminar: ")
else:
    print("No has seleccionado una opción válida.")
    exit(1)