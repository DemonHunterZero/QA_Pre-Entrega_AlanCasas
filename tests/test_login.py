from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from utils.datos import leer_csv_login
from utils.logger import logger
import pytest

logger.info("---EJECUTANDO TEST LOGIN---")
#py -m pytest tests/test_login.py -v para ejecutarlo como prueba
#py -m pytest tests/test_login.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
@pytest.mark.parametrize("user, password, debe_funcionar", leer_csv_login("datos/datos_login.csv"))
def test_login_validation(login_in_chrome, user, password, debe_funcionar):
    try:
        logger.info(f"Completando con las credenciales... User: {user} - Password: {password}")
        driver = login_in_chrome #toma los parametros user y password implicitamente
        
        if debe_funcionar: #debe_funcionar == True:
            logger.info("Verificando redireccionamiento dentro de la pagina.")
            #Validacion de url luego del login        
            assert '/inventory.html' in driver.current_url, "No se redirigio al inventario"            
            print("Login exitoso y validado")
        else:
            #Validacion para credenciales incorrectas (verifica que salga el cartel de aviso de error)
            logger.warning("Las credenciales no son las correctas")
            logger.info("Verificando mensaje de error...")
            mensaje_error = LoginPage(driver).obtener_error()            
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se muestra correctamente"
        
        logger.info("Test de login completado")

        
    
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

