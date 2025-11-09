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

El repositorio se organiza de la siguiente manera:

### Archivos en la raíz del proyecto

- **.gitignore** → Define los archivos y carpetas que no deben incluirse en el control de versiones.  
- **README.md** → Contiene la información general y documentación del proyecto.  
- **source/** → Carpeta principal que agrupa el código fuente y los datos generados o recopilados.

---

### Contenido de la carpeta `source/`

- **dataset/** → Contiene los resultados obtenidos del proceso de scraping y análisis.
  - **graficos/** → Carpeta donde se almacenan los gráficos generados a partir de los datos del CSV.  
  - **images/** → Carpeta con las imágenes descargadas de los productos procesados.  
  - **productos.csv** → Archivo que almacena la información estructurada extraída mediante web scraping.

- **environment.yml** → Archivo que define el entorno de trabajo de Python, incluyendo las librerías y versiones necesarias para ejecutar el proyecto.  
- **geckodriver.exe** → Ejecutable requerido por Selenium para la automatización del navegador Firefox.  
- **obtencion_datos.py** → Script encargado de recopilar las URLs de los productos que posteriormente serán procesados.  
- **web_scraping.py** → Script principal de extracción de datos. Utiliza las URLs obtenidas para recolectar información e imágenes de los productos, y genera el archivo `productos.csv`.  
- **crear_graficas.py** → Script que analiza el archivo CSV generado y produce visualizaciones gráficas a partir de los datos recopilados.

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
```
5.2 Realizar el scraping

```bash

python web_scraping.py
```

Crea el archivo productos.csv y descarga las imágenes en dataset/images/.

## 6. Parámetros y Personalización

Actualmente, los scripts no requieren parámetros externos para su ejecución.  
No obstante, el usuario puede personalizar distintos aspectos del proyecto según sus necesidades:

- **Fuente o dominio de las URLs:** permite definir desde qué página web se extraerán los datos.  
- **Número de productos a analizar:** configurable para ajustar la cantidad de elementos procesados.  
- **Formato de salida del dataset o de las gráficas:** se puede modificar el tipo de archivo o el estilo visual de las representaciones.

Estas configuraciones se encuentran dentro de los propios scripts Python y pueden adaptarse fácilmente editando las variables definidas al inicio de cada archivo.

---

## 7. Resultados Generados

El proyecto produce los siguientes resultados principales:

- **`productos.csv`** → Contiene los datos estructurados extraídos mediante web scraping.  
- **`images/`** → Carpeta que almacena las imágenes descargadas de los productos procesados.  
- **`graficos/`** → Carpeta con los gráficos generados automáticamente a partir del archivo CSV.

Estos recursos permiten **analizar el comportamiento del mercado y las características de los productos** de manera visual e interactiva.

---

## 8. DOI del Dataset

El dataset final ha sido publicado en **Zenodo**, disponible en el siguiente enlace:

🔗 **[https://doi.org/10.5281/zenodo.17566073](https://doi.org/10.5281/zenodo.17566073)**  

---

## 9. Licencia

Este proyecto se distribuye con fines **académicos y de investigación**.  
El código puede ser utilizado, modificado o extendido citando la fuente original y respetando las licencias de las herramientas utilizadas.

---
