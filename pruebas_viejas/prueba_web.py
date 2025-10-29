from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Importar Options
from selenium.common.exceptions import NoSuchElementException


# 1. Configurar las opciones de Chrome para evitar el popup de contraseña (SOLUCION CHAT GTP)
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


#Creamos el driver de chrome y le seteamos las opciones
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


try:
    #Login
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']" ).click()
    time.sleep(5)
    #EN CASO DE APARECER CERRAR EL POP UP MANUALMENTE!!!!!!

    #Valida la pagina contenga la cadena de caracteres '/inventory.html' en la url
    assert '/inventory.html' in driver.current_url

    #Interacciones 
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print(carrito)
    assert carrito == "1"
    
    print("Test ok")

except AssertionError:
    print("Test Fallido: La aserción no se cumplió.")
except NoSuchElementException as e:
    print(f"Test Fallido: No se encontró un elemento. Error: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    driver.quit()

