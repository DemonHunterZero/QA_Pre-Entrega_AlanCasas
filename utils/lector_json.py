import json
from pathlib import Path

def leer_json_productos(ruta_archivo):
    #Preparación del archivo
    ruta = Path(ruta_archivo)

    #Apertura y carga del JSON
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
    
    #Extraccion de los nombres
    nombres = [producto["nombre"] for producto in productos] #de cada producto en productos se queda solo con el "nombre"
    return nombres