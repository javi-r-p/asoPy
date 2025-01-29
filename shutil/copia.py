#Localizar un archivo, moverlo a otro directorio, comprimirlo y después borrar el archivo original

import shutil
from pathlib import Path

archivo = input("Introduce el nombre del archivo: ")

print("Copiando archivo...")
shutil.copy2(archivo, "backups")

print("Comprimiendo directorio...")
shutil.make_archive("backup", "zip", "backups")

print("Eliminando archivo original...")
archivo = Path("backups/"+archivo)
archivo.unlink()