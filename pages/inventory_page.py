from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options # Importar Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class InventoryPage:

    #Selectores

    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CART_LINK= (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        return productos
    
    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._ITEM_NAME)
        return [producto_nombre.text for producto_nombre in productos ] #es una lista de nombres de productos en formato texto
    
    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()
        return self
    
    def agregar_producto_por_nombre(self, nombre_producto):
        productos = self.obtener_todos_los_productos()

        for producto in productos:
            nombre = producto.find_element(*self._ITEM_NAME).text
            #.strip elimina los espacios de la cadena de texto .lower los hace en minuscula
            if nombre.strip().lower() == nombre_producto.strip().lower():
                boton = producto.find_element(self._ADD_TO_CART_BUTTON)
                boton.click()
                return self
            else:
                raise Exception(f"No se encontro el producto {nombre_producto}")
            
    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
        return self

    def obtener_conteo_carrito(self):
            try:
                # Espera a que el contador sea visible
                self.wait.until(EC.visibility_of_element_located(self._CART_COUNT))
                
                # Ubica el elemento utilizando el desempaquetado (*)
                contador_carrito = self.driver.find_element(*self._CART_COUNT) 
                
                return int(contador_carrito.text)
                
            except:
                # Si hay un error (TimeoutException porque no aparece), retorna 0
                return 0


    
