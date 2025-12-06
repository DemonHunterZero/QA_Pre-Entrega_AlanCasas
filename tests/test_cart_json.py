from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time
import pytest
from utils.lector_json import leer_json_productos

RUTA_JSON = "datos/productos.json"

#py -m pytest tests/test_cart_json.py -v para ejecutarlo como prueba
#py -m pytest tests/test_cart_json.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
@pytest.mark.parametrize("user, password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_chrome, user, password, nombre_producto):
        
    try:
        driver = login_in_chrome
        inventory_page = InventoryPage(driver)

        #Agregar productos al carrito
        time.sleep(1)
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        #Abrir carrito
        time.sleep(1)
        inventory_page.abrir_carrito()

        #Validar que se haya agregador producto
        time.sleep(3)
        cartPage = CartPage(driver)

        assert cartPage.obtener_nombre_productor_carrito() == nombre_producto

    

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