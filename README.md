# 🧪 Suite de Automatización de Pruebas - TalentoTech

Este proyecto es una **suite de automatización robusta** para pruebas de **interfaz de usuario (UI)** y **pruebas de API**, construida utilizando el stack de **Pytest** y **Selenium** en **Python**.

El objetivo es garantizar la calidad y funcionalidad de la aplicación **Sauce Demo**  
👉 https://www.saucedemo.com/  
y de servicios externos como **Reqres.in**, a través de un marco de pruebas **modular, escalable y mantenible**.

---

## ✨ Características Principales

- **Modelo de Objeto de Página (POM)**  
  Implementación clara y mantenible de Page Objects en la carpeta `pages/`.

- **Pruebas Basadas en Datos (DDT)**  
  Uso de archivos `.csv` y `.json` (`datos/`) para ejecutar múltiples escenarios automáticamente.  
  Ejemplos:
  - `test_login.py`
  - `test_cart_json.py`

- **Generación de Datos Falsos (Faker)**  
  Uso de la librería **Faker** para probar escenarios de login con credenciales inválidas (`test_login_faker.py`).

- **Pruebas de API**  
  Pruebas funcionales de endpoints REST (`test_api_request.py`).

- **Reporte HTML**  
  Generación automática de reportes detallados y autocontenidos (`report.html`) usando `pytest-html`.

- **Captura de Fallos (Screenshots)**  
  Configuración en `conftest.py` para tomar screenshots automáticamente cuando falla una prueba de UI y adjuntarlos al reporte HTML.

- **Integración Continua (CI)**  
  Ejecución automática de la suite completa mediante **GitHub Actions**.

---

## 🛠️ Tecnologías y Librerías

| Tecnología / Librería     | Propósito                              | Instalación |
|----------------------     |----------                              |-------------|
| Python                    | Lenguaje base (3.12)                   | N/A |
| Pytest                    | Framework de testing                   | `pytest` |
| Selenium                  | Automatización del navegador Chrome    | `selenium` |
| pytest-html               | Reportes HTML                          | `pytest-html` |
| Faker                     | Generación de datos falsos             | `faker` |
| Requests                  | Pruebas de API REST                    | `requests` |
| GitHub Actions            | CI/CD                                  | N/A |

---

## 🚀 Instalación y Ejecución

### 1️⃣ Pre-requisitos

- Python **3.12** instalado en el sistema.

---

### 2️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_directorio>
---

### 3️⃣ Instalación de dependencias

Instalar todas las librerías necesarias con pip:

pip install -r requirements.txt


### 4️⃣ Ejecución local de las pruebas

La suite se ejecuta mediante el script run_tests.py, el cual encapsula el comando completo de Pytest y genera el reporte HTML:

python run_tests.py

✔ Esto ejecuta todos los tests de la carpeta tests/
✔ Genera los resultados en la carpeta reports/

## Estructura del proyecto
| Directorio / Archivo | Descripción                                                       |
| -------------------- | ----------------------------------------------------------------- |
| `tests/`             | Contiene todos los archivos de prueba (`test_*.py`).              |
| `pages/`             | Implementación del Page Object Model (POM).                       |
| `datos/`             | Archivos de datos para DDT (`datos_login.csv`, `productos.json`). |
| `utils/`             | Módulos auxiliares: `logger.py`, `datos.py`, `lector_json.py`.    |
| `reports/`           | Resultados de ejecución: `report.html` y `screens/`.              |
| `logs/`              | Archivo `suite.log` con logs detallados.                          |
| `conftest.py`        | Fixtures globales y hook para screenshots automáticos.            |
| `run_tests.py`       | Script principal de ejecución de la suite.                        |

## Detalles de pruebas (tests/)
| Archivo               | Tipo de Prueba  | Descripción                                                                 |
| --------------------- | --------------- | --------------------------------------------------------------------------- |
| `test_login.py`       | UI (Login)      | Login con credenciales válidas e inválidas desde CSV.                       |
| `test_login_faker.py` | UI (Login)      | Validación de errores con datos aleatorios (Faker).                         |
| `test_inventory.py`   | UI (Inventario) | Verificación de productos y contador del carrito.                           |
| `test_cart.py`        | UI (Carrito)    | Agregado de productos y navegación (incluye error forzado para screenshot). |
| `test_cart_json.py`   | UI / DDT        | Agregado de productos desde archivo JSON.                                   |
| `test_api_request.py` | API             | Pruebas GET, POST y DELETE contra Reqres.in.                                |

## 📊 Reportes y Logs

Luego de la ejecución, los resultados se almacenan en:

reports/report.html
    Reporte visual con el estado de cada prueba y screenshots incrustados.

reports/screens/
    Capturas de pantalla automáticas ante fallos de UI.

logs/suite.log
    Logs detallados de la ejecución (INFO, WARNING).

## ⚙️ Integración Continua (GitHub Actions)

El archivo .github/workflows/ci.yml configura un flujo de CI automático que se ejecuta en cada:

    push
    pull request

sobre las ramas main y develop.

##🔧 Detalles del CI

Entorno: ubuntu-latest

Python: 3.12

Optimización: cache de dependencias pip

Ejecución:

python run_tests.py

Artefactos:
    Carpeta reports/
    Carpeta logs/

Los artefactos quedan disponibles para descarga desde GitHub Actions.