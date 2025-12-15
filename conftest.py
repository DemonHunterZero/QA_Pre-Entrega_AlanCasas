import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options # Importar Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import pathlib
from datetime import datetime
import time


# Carpeta donde se guardan los screenshots
target = pathlib.Path("reports/screens")
#Crea la carpeta. No levanta error si la carpeta existe y crea los directorios padres sino existen
target.mkdir(parents=True, exist_ok=True)

#Las funciones de este archivo son GLOBALES por llamarse conftest. No hace falta importarlas
@pytest.fixture
def chrome_driver():
    
    # Configurar las opciones de Chrome para evitar el popup de contraseña (SOLUCION CHAT GTP)
    chrome_options = Options()
    # Esta preferencia evita el cuadro de diálogo "Guardar contraseña" de Chrome
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
        "profile.exit_type": "Normal",
        "profile.exited_cleanly": True,
        "profile.password_manager_leak_detection": False  # <--- ESTA ES LA CLAVE
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--start-maximized') # Opcional: ventana maximizada
    chrome_options.add_argument('--incognito') 
    chrome_options.add_argument('--disable-gpu') #Mejora el rendimiento en github
    if os.getenv("CI"):  # GitHub Actions define CI=true
        chrome_options.add_argument('--no-sandbox') #github
        chrome_options.add_argument('--headless=new') #github (para entornos virtuales donde no hay entorno grafico como github) NO VERE EL NAVEGADOR EN MI PC


    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5) #las esperas implicitas seran de 5s
    yield driver
    driver.quit()

@pytest.fixture
def login_in_chrome(chrome_driver, user, password):
    LoginPage(chrome_driver).abrir_pagina().login_completo(user,password)
    return chrome_driver

#Variables globales para los test API
@pytest.fixture
def url_base():
    url = "https://reqres.in/api/users"
    return url

@pytest.fixture
def header_base():
    header = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
    return header

#En caso de error sacara screenshots
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield # 'yield' ejecuta el hook original de pytest. Almacenamos el resultado en 'outcome'.    
    report = outcome.get_result() # Obtener el objeto 'report' que contiene el resultado de la fase de prueba.

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("chrome_driver", None)

        if driver:
            timestamp = int(time.time()) # Generar un timestamp (número de segundos desde el epoch) para asegurar un nombre de archivo único.
            file_name = target / f"{report.when}_{item.name}_{timestamp}.png" # Construir el nombre completo del archivo de captura de pantalla: {fase}_{nombre_del_test}_{timestamp}.png
            
            try:
                driver.save_screenshot(str(file_name)) # Guardar la captura de pantalla en la direccion target/file_name

                # Adjuntar al reporte HTML            
                extra = getattr(report, "extra", []) # Intentar obtener la lista 'extra' del reporte, que pytest-html usa para contenido adicional. Si no existe, inicializarla como una lista vacía.
                extra.append(
                    pytest_html.extras.image(str(file_name))
                ) # Esto hace que la imagen aparezca incrustada en el reporte HTML.
                report.extra = extra # Asignar la lista 'extra' modificada de nuevo al reporte.
            except Exception as e:
                print(f"No se pudo capturar screenshot: {e}")


#py -m pip install -r requirements.txt para instalar las dependencias necesarias
