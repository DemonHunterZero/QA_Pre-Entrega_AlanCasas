from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest
import time

#py -m pytest tests/test_login.py -v para ejecutarlo como prueba
#py -m pytest tests/test_login.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
@pytest.mark.parametrize("user, password, debe_funcionar",(
        ("standard_user","secret_sauce", True),
        ("locked_out_user","secret_sauce", False),
        ("problem_user","secret_sauce", True),
        ("performance_glitch_user","secret_sauce", True),
        ("error_user","secret_sauce", True),
        ("visual_user","secret_sauce", True)
))
def test_login_validation(login_in_chrome, user, password, debe_funcionar):
    try:
        driver = login_in_chrome #toma los parametros user y password implicitamente
        
        if debe_funcionar:
            #Validacion de url luego del login        
            assert '/inventory.html' in driver.current_url, "No se redirigio al inventario"
            print("Login exitoso y validado")
        else:
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se muestra correctamente"
        
    
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