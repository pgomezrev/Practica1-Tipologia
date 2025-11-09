# 🧠 Web Scraping y Análisis de Productos

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licencia-Académica-lightgrey.svg)]()
[![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow.svg)]()
[![DOI](https://img.shields.io/badge/DOI-Zenodo-blue.svg)](https://doi.org/10.XXXX/zenodo.XXXXXXX)

---

## 📚 Tabla de Contenidos

1. [Autores](#1-autores)  
2. [Resumen del Proyecto](#2-resumen-del-proyecto)  
3. [Estructura del Repositorio](#3-estructura-del-repositorio)  
4. [Metodología de Trabajo](#4-metodología-de-trabajo)  
5. [Instrucciones de Uso](#5-instrucciones-de-uso)  
6. [Parámetros y Personalización](#6-parámetros-y-personalización)  
7. [Resultados Generados](#7-resultados-generados)  
8. [DOI del Dataset](#8-doi-del-dataset)  
9. [Licencia](#9-licencia)

---

## 1. Autores

- **Pedro Gómez Revilla**  
- **Andrea Isabel Espada Murguia**

---

## 2. Resumen del Proyecto

El presente proyecto tiene como objetivo la **obtención, procesamiento y análisis de datos de productos** mediante técnicas de **web scraping** automatizado.  

Se emplean herramientas de **Python** y librerías de automatización (como *Selenium*) para recopilar información de distintas fuentes web, almacenar los datos en formato CSV

El flujo de trabajo abarca desde la **recolección automática de URLs**, pasando por la **extracción de datos e imágenes**.

---

## 3. Estructura del Repositorio

├── .gitignore # Define los archivos que no deben subirse al repositorio
├── README.md # Información general del proyecto
└── source/ # Carpeta principal del código fuente y los datos
├── dataset/
│ ├── graficos/ # Gráficos generados a partir del CSV
│ ├── images/ # Imágenes de los productos procesados
│ └── productos.csv # Datos extraídos mediante web scraping
│
├── environment.yml # Configuración del entorno Python (librerías y dependencias)
├── geckodriver.exe # Ejecutable necesario para Selenium
├── obtencion_datos.py # Obtiene las URLs de los productos a procesar
├── web_scraping.py # Extrae información e imágenes de los productos y genera el CSV
└── crear_graficas.py # Genera gráficos a partir del CSV generado


---

## 4. Metodología de Trabajo

1. **Obtención de URLs**  
   Se utiliza `obtencion_datos.py` para recopilar enlaces de productos desde una fuente web determinada.  

2. **Extracción de Datos (Web Scraping)**  
   El script `web_scraping.py` accede a las URLs, extrae la información relevante de cada producto y descarga sus imágenes.  

3. **Generación de Dataset**  
   Los datos se consolidan en el archivo `productos.csv` dentro de la carpeta `dataset/`.  

---

## 5. Instrucciones de Uso

### 5.1 Crear el entorno de ejecución

Para preparar el entorno Python, ejecutar:

```bash
conda env create -f environment.yml
conda activate scraping_project

5.2 Realizar el scraping

python web_scraping.py

Crea el archivo productos.csv y descarga las imágenes en dataset/images/.

6. Parámetros y Personalización

Actualmente, los scripts no requieren parámetros externos.
Sin embargo, el usuario puede personalizar:

    La fuente o dominio de las URLs.

    El número de productos a analizar.

    El formato de salida del dataset o de las gráficas.

Estas configuraciones se encuentran dentro de los propios scripts Python.

7. Resultados Generados

El proyecto produce los siguientes resultados:

    Archivo productos.csv con los datos estructurados.

    Carpeta images/ con las imágenes de cada producto.

Estos recursos permiten analizar el comportamiento del mercado y las características de los productos de forma visual e interactiva.

8. DOI del Dataset

El dataset final ha sido publicado en Zenodo, disponible en el siguiente enlace:

🔗 https://doi.org/10.XXXX/zenodo.XXXXXXX

9. Licencia

Este proyecto se distribuye con fines académicos y de investigación.
El código puede ser utilizado, modificado o extendido citando la fuente original y respetando las licencias de las herramientas utilizadas.
