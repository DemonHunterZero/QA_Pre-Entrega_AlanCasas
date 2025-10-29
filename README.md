# 🧪 Automatización E2E - Swag Labs (Sauce Demo)

Este proyecto contiene un conjunto de pruebas de automatización *End-to-End* (E2E) desarrolladas en **Python** utilizando **Selenium** y el *framework* **Pytest**. El objetivo es validar el flujo principal de usuario en la tienda de demostración [Swag Labs](https://www.saucedemo.com/) (Login, Inventario y Compra).

---

## 🚀 Requisitos

Asegúrate de tener instalado lo siguiente:

* **Python 3.x**
* **Google Chrome**

### Dependencias

El proyecto utiliza las siguientes librerías. Puedes instalarlas ejecutando:

```bash
pip install selenium pytest pytest-html


#### Estructura
.
├── pruebas_viejas/       # Ignorar, son pruebas y apuntes tomados en clases para este proyecto
├── tests/
│   ├── test_buy.py       # Prueba el flujo completo de agregar y ver en el carrito.
│   ├── test_inventory.py # Prueba la visibilidad de elementos en la página de inventario.
│   └── test_login.py     # Valida el login exitoso y la redirección a la página de inventario.
├── utils/
│   └── utils.py          # Contiene la lógica para la inicialización del WebDriver y la función de login.
├── conftest.py           # Define los fixtures de Pytest (chrome_driver y login_in_chrome).
├── run_tests.py          # Script para ejecutar todas las pruebas desde Python sin la consola.
└── README.md

 Ejecución de PruebasPuedes ejecutar las pruebas utilizando el comando pytest directamente en la terminal o mediante el script run_tests.py.Opción 1: Usando la Terminal (Comando Pytest)Ejecuta cualquiera de los siguientes comandos desde la raíz del proyecto (PRE-E...):TareaComandoEjecutar todos los testspy -m pytest tests/ -vEjecutar un archivo específicopy -m pytest tests/test_buy.py -vGenerar Reporte HTMLpy -m pytest tests/ -v --html=report.html --self-contained-htmlEl flag -v (verbose) muestra el progreso detallado de cada test.Opción 2: Usando el script run_tests.pySi prefieres ejecutar todas las pruebas definidas en la lista test_files (que actualmente incluye test_inventory, test_login y test_buy) junto con el reporte HTML, simplemente ejecuta:Bashpython run_tests.py
# O si usas 'py':
# py run_tests.py

⚙️ Fixtures y ConfiguraciónEl archivo conftest.py define dos fixtures esenciales:chrome_driver(): Se encarga de crear el objeto webdriver.Chrome, aplicando configuraciones para evitar los pop-ups de guardar contraseña, y se asegura de cerrar el navegador al finalizar la prueba (yield y driver.quit()).login_in_chrome(chrome_driver): Utiliza el chrome_driver para navegar a la URL, ingresa las credenciales (standard_user / secret_sauce) y devuelve la instancia del driver ya autenticada. Todas las pruebas utilizan este fixture.