from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


#py -m pytest tests/test_inventory.py -v para ejecutarlo como prueba
#py -m pytest tests/test_inventory.py -v --html=report.html --self-contained-html para ejecutarlo y realizar el reporte html
def test_inventory(login_in_chrome):
    driver = login_in_chrome
    
    try:
        #Validacion de titulo
        assert driver.title == "Swag Labs"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "inventory_container"))) #Espera que cargue el div contenedor principal


                                #products = driver.find_elements(By.CLASS_NAME, "inventory_item")
                                #assert len(products) > 0, "No hay productos en la pagina"
        
        #Valida que existan, sean visibles y mayor a 0
        products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        #Si wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))) se cumple retorna driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"

        #Validacion de existencia de precio numerico visible en el primer producto
        product = products[0]
        precio_visible = product.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div").is_displayed()
        precio_valor = product.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text #"$29.99"
        precio_numerico = precio_valor.replace("$", "")
        precio_es_numerico = precio_numerico.isnumeric
        
        assert precio_visible and precio_es_numerico, "No existe precio en ese item y/o no es un valor numerico" #tambien es posible simplemente poner assert precio_visible

        #Validacion de existencia de titulo visible en el primer producto
        existe_nombre_producto = product.find_element(By.CSS_SELECTOR, "#item_4_title_link > div").is_displayed()
        assert existe_nombre_producto == True, "No existe nombre del primer producto"

        #Validacion del nombre del primer producto
        nombre_producto = product.find_element(By.CSS_SELECTOR, "#item_4_title_link > div").text
        assert nombre_producto == "Sauce Labs Backpack", "El nombre del primer producto no es el correcto"

        #Validacion del menu de filtro
        menu_filtro = driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
        assert menu_filtro, "El menu de filtro no existe"

        #Validacion del menu de hamburguesa
        menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        assert menu_hamburguesa, "El menu de filtrhamburguesa no existe"


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
    

    
