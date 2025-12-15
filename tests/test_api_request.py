import requests
import pytest
import time
from utils.logger import logger

logger.info("---EJECUTANDO TEST API REQUEST---")
#py -m pytest tests/test_api_request.py -v para ejecutarlo como prueba

#Obtener usuario
def test_get_user(url_base, header_base):
    HEADER = header_base
    URL = f"{url_base}/2" #tbm conocida como endpoint
    
    logger.info("Obteniendo usuario por solicitud GET")
    response = requests.get(URL, headers=HEADER)

    logger.info("Validando status code 200")
    assert response.status_code == 200

    logger.info("Trayendo el usuario en json")
    data = response.json()

    logger.info("Validando id")
    assert data["data"]["id"]==2


#Crear usuario
def test_post_user(url_base, header_base):
    HEADER = header_base
    URL = url_base #tbm conocida como endpoint
    PAYLOAD = {"name":"Alan", "job":"Piloto"}

    logger.info("Creando usuario por solicitud POST")
    response = requests.post(URL, headers=HEADER, json=PAYLOAD)

    #Verifica que el recurso sea creado (code: 201)
    logger.info("Validando status code 201")
    assert response.status_code == 201

    logger.info("Trayendo el usuario en json")
    data = response.json()

    #Verifica que el nombre de la respuesta sea el mismo que el enviado
    assert data["name"] == PAYLOAD["name"]

    #Verifica que la respuesta tenga un id
    logger.info("Validando id")
    assert "id" in data

#Eliminar usuario
def test_delete_user(url_base, header_base):
    HEADER = header_base
    URL = f"{url_base}/2" #tbm conocida como endpoint    

    inicio = time.time() #Toma la hora
    logger.info("Borrando usuario por solicitud DELETE")
    response = requests.delete(URL, headers=HEADER)
    final = time.time() #Toma la hora
    tiempo_tardo = final - inicio

    #Verifica que el recurso sea borrado (code: 204)
    logger.info("Validando status code 204")
    assert response.status_code == 204

    #Verifica que la respuesta sea menor a 2 seg
    logger.info("Validando tiempo de respuesta menor a 2seg")
    assert tiempo_tardo < 2, f"La api tardo demasiado {tiempo_tardo}"