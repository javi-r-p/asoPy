# Contar palabras en un archivo

archivo = input("Introduce la ruta absoluta de un archivo (sin comillas): ")

try:
    with open(archivo, "r") as a:
        contenido = a.read()
        palabras = contenido.split()
        print("El archivo tiene ", len(palabras), "palabras.")
except FileNotFoundError:
    print("El archivo que has especificado no existe.")
