import csv
import pathlib


def leer_csv_login(ruta_archivo):
    ruta = pathlib.Path(ruta_archivo)

    datos = []
    with open(ruta, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convierte la cadena 'True' a True, y 'False' a False por logica. Si true == true entonces verdadero si false == true entonces false
            es_exitoso = fila["expected_login_success"].lower() == 'true' 
            
            datos.append((fila["username"], fila["password"], es_exitoso))
            
    
    return datos

print(leer_csv_login("datos/datos_login.csv"))
