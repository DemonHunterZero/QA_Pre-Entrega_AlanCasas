from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.inventory_page import InventoryPage
from utils.logger import logger
import time
import pytest

logger.info("---EJECUTANDO TEST INVENTORY---")

#py -m pytest tests/test_inventory.py -v para ejecutarlo como prueba
#py -m pytest tests/test_inventory.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
@pytest.mark.parametrize("user, password",[("standard_user","secret_sauce")])
def test_inventory(login_in_chrome, user, password):
        
    try:
        driver = login_in_chrome
        inventory_page = InventoryPage(driver)
        
        logger.info("Verificando existencia de productos")
        #verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"
        
        logger.info("Verificando que el carrito este vacio")
        #Esta vacio el carrito al inicio?
        assert inventory_page.obtener_conteo_carrito() == 0
        time.sleep(1)

        #Agregar primer producto
        inventory_page.agregar_primer_producto()
        time.sleep(1)

        logger.info("Verificando que el contador del carrito cambie al agregar producto")
        #Verificar que el contador del carrito haya cambiado
        assert inventory_page.obtener_conteo_carrito() == 1, "Error, el contador debe ser 1"

        



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


    
