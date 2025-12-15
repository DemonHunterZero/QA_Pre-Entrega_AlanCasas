import pytest
#Ejecutar este archivo te ahorra escribir el comando en la consola y ejecuta los tests selecionados
pytest.main(["tests/","--html=reports/report.html","--self-contained-html","-v"])


"""
--MODELO VIEJO--
#Lista de archivos para ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_login_faker.py",
    "tests/test_inventory.py",    
    "tests/test_cart.py",
    "tests/test_cart_json.py",
    "tests/test_api_request.py"
]

#Argumentos para ejecutar las pruebas
pytest_args = test_files + ["--html=report.html","--self-contained-html", "-v"]

pytest.main(pytest_args) """