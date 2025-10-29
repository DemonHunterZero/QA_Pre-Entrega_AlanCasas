from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options # Importar Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


#Crear driver = create_webdriver_chrome()
def create_webdriver_chrome():
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
    
    #Creacion del driver con las configuraciones
    return webdriver.Chrome(options=chrome_options)


def login(driver):
    driver.get("https://www.saucedemo.com/") 
    
    #Espera implicita
    driver.implicitly_wait(10)
    #Espera explicita
    wait = WebDriverWait(driver, 5)

    #Esperas explicita a que los elementos esten y sean visibles
    wait.until(EC.visibility_of_element_located((By.ID,"user-name")))
    wait.until(EC.visibility_of_element_located((By.ID,"password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='submit']")))

    #Ingreso de credenciales
    time.sleep(1)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    time.sleep(1)        
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']" ).click()
    time.sleep(1)    