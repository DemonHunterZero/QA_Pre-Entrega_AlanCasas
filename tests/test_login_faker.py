from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
import pytest
from utils.logger import logger
from faker import Faker


logger.info("---EJECUTANDO TEST LOGIN FAKER---")
#py -m pytest tests/test_login_faker.py -v para ejecutarlo como prueba
#py -m pytest tests/test_login_faker.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html

#Inicializamos Faker (genera datos falsos)
fake = Faker()

@pytest.mark.parametrize("user, password, debe_funcionar", [
    (fake.user_name(), fake.password(), False),
    (fake.user_name(), fake.password(), False),
    (fake.user_name(), fake.password(length=4, lower_case=True, upper_case=True, digits=True, special_chars=True), False) #en password decimos que caracteristicas debe tener
    ])
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
            logger.warning("Las credenciales no son las correctas")
            logger.info("Verificando mensaje de error...")
            #Validacion para credenciales incorrectas (verifica que salga el cartel de aviso de error)
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