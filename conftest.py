import pytest
from selenium import webdriver
from utils.utils import login, create_webdriver_chrome

#Las funciones de este archivo son GLOBALES por llamarse conftest. No hace falta importarlas
@pytest.fixture
def chrome_driver():
    #driver = webdriver.Chrome()
    driver = create_webdriver_chrome()
    driver.implicitly_wait(10) #agregado (borrar sino funciona)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_chrome(chrome_driver):
    login(chrome_driver)
    return chrome_driver
