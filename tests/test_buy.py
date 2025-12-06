#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


#py -m pytest tests/test_buy.py -v para ejecutarlo como prueba
#py -m pytest tests/test_buy.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
def test_buy(login_in_chrome):
    driver = login_in_chrome
    
    try:
        #Valida la pagina contenga la cadena de caracteres '/inventory.html' en la url (Que estemos en la pagina correcta)
        assert '/inventory.html' in driver.current_url

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "inventory_container"))) #Espera que cargue el div contenedor principal

        #Valida que existan, sean visibles y mayor a 0
        products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        #Si wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))) se cumple retorna driver.find_elements(By.CLASS_NAME, "inventory_item")


        product = products[0]
        name_product = product.find_element(By.CLASS_NAME,"inventory_item_name").text #Sauce Labs Backpack
        product.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)

        #Validacion de que el contador del carrito se sume
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1"

        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click() #hace click para ir al carrito
        assert '/cart.html' in driver.current_url #Validacion de que nos cambie a la pagina correcta

        producto_carrito = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list > div:nth-child(3)")
        existe_producto_carrito = producto_carrito.is_displayed() #indica si existe un producto y es visible
        nombre_producto_carrito = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").text #Sauce Labs Backpack
        assert existe_producto_carrito and name_product == nombre_producto_carrito, "Existe un producto y es el mismo que seleccionamos"
        
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
    
