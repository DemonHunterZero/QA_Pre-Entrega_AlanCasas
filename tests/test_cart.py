from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger
import time
import pytest

logger.info("---EJECUTANDO TEST CART---")
#py -m pytest tests/test_cart.py -v para ejecutarlo como prueba
#py -m pytest tests/test_cart.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
@pytest.mark.parametrize("user, password",[("standard_user","secret_sauce")])
def test_cart(login_in_chrome, user, password):
        
    try:
        driver = login_in_chrome
        inventory_page = InventoryPage(driver)
        
        #Agregar productos al carrito
        time.sleep(1)
        logger.info("Agregando productos al carrito")
        inventory_page.agregar_primer_producto()

        #Abrir carrito
        time.sleep(1)
        logger.info("Abriendo el carrito")
        inventory_page.abrir_carrito()

        #Validar que se haya agregador producto
        time.sleep(3)
        cartPage = CartPage(driver)
        productos_en_carrito = cartPage.obtener_productos_carrito()
        logger.info("Validando que se agregaron productos al carrito")
        assert len(productos_en_carrito) == 1
    

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
