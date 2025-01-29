#Localizar un archivo, moverlo a otro directorio, comprimirlo y después borrar el archivo original

import shutil, subprocess
from pathlib import Path
from shutil import unpack_archive

print("1. Hacer copia de seguridad")
print("2. Descomprimir copia de seguridad")
opcion = int(input("Selecciona una opción: "))

if opcion == 1:
    archivo = input("Introduce el nombre del archivo: ")

    print("Copiando archivo...")
    shutil.copy2(archivo, "backups")

    print("Comprimiendo directorio...")
    shutil.make_archive("backup", "zip", "backups")

    print("Eliminando archivo original...")
    archivo = Path("backups/"+archivo)
    archivo.unlink()

elif opcion == 2:
    archivo = input("Introduce el archivo a descomprimir: ")
    unpack_archive(archivo, "restauraciones/")

    listado = subprocess.run(["dir"], shell=True)

else:
    print("No has seleccionado una opción válida.")
    exit(1)