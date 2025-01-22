import os

# Cambiar al directorio del usuario
home_dir = os.environ.get("HOME", "/")
os.chdir(home_dir)

# Crear un directorio nuevo
os.makedirs("nuevoDirectorio", exist_ok=True)

# Listar contenido del directorio
contenido = os.listdir(".")
print(f"Contenido en {home_dir}: {contenido}")

# Crear y renombrar un archivo
with open("nuevoDirectorio/archivo.txt", "w") as f:
    f.write("Hola, mundo!")
os.rename("nuevoDirectorio/archivo.txt", "nuevoDirectorio/archivoRenombrado.txt")