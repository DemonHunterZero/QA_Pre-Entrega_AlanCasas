from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

#py -m pytest test_login.py -v para ejecutarlo como prueba
#py -m pytest test_login.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
def test_login_validation(login_in_chrome):
    try:
        driver = login_in_chrome
        
        #Validacion de url luego del login
        assert '/inventory.html' in driver.current_url, "No se redirigio al inventario"
        print("Login exitoso y validado")
        
    
    #Manejo de errores
    except AssertionError:
        print("Test Fallido: La aserción no se cumplió.")
        raise
    except NoSuchElementException as e:
        print(f"Test Fallido: No se encontró un elemento. Error: {e}")
        raise
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise

    finally:
        driver.quit()