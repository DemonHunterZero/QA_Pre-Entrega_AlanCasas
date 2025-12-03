import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options # Importar Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

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

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5) #las esperas implicitas seran de 5s
    yield driver
    driver.quit()

@pytest.fixture
def login_in_chrome(chrome_driver, user, password):
    LoginPage(chrome_driver).abrir_pagina().login_completo(user,password)
    return chrome_driver