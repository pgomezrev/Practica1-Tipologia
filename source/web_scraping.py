from obtencion_datos import obtencion_urls
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

url_general = 'https://www.pccomponentes.com/'
scraper_api_key = "4498f114a561c6e7a433fb5a51194227"
archivo_csv = "data/productos.csv"

def obtencion_datos_web(web):
    datos_csv = []
    web_urls = obtencion_urls(web)
    for web_url in web_urls:
        obtener_dato(datos_csv, web_url)
    
    df = pd.DataFrame(datos_csv)
    df.to_csv(archivo_csv, index=False, sep=';', encoding='utf-8')

def obtener_dato(datos_csv, web_url):
    session = requests.Session()
    scraper_api_url = f"http://api.scraperapi.com/?api_key={scraper_api_key}&url={web_url}"
    response = requests.get(scraper_api_url)

    if response.status_code == 200:
        extraer_datos(response, datos_csv)
    else:
        print(f"Error {response.status_code} en la peticion a la url {web_url}")
    

def extraer_datos(response, datos_csv):
    html_parseado = BeautifulSoup(response.text, 'html.parser')
    titulo_producto = html_parseado.find('h1', {'id': 'pdp-title'}).text.strip()
    precio = html_parseado.find('span', {'id': 'pdp-price-current-integer'}).text.strip()
    p_n = html_parseado.find('span', {'id': 'pdp-mpn'}).text.strip().replace('P/N: ','')
    estrellas = html_parseado.find('span', {'class': 'sc-dVCGSn dEQtAy'}).text.strip()
    estrellas_5 = html_parseado.find('li', {'data-testid': 'star-5'}).find('span', {'class' : 'count-E1B_yO'}).text.strip()
    estrellas_4 = html_parseado.find('li', {'data-testid': 'star-4'}).find('span', {'class' : 'count-E1B_yO'}).text.strip()
    estrellas_3 = html_parseado.find('li', {'data-testid': 'star-3'}).find('span', {'class' : 'count-E1B_yO'}).text.strip()
    estrellas_2 = html_parseado.find('li', {'data-testid': 'star-2'}).find('span', {'class' : 'count-E1B_yO'}).text.strip()
    estrellas_1 = html_parseado.find('li', {'data-testid': 'star-1'}).find('span', {'class' : 'count-E1B_yO'}).text.strip()
    marca = html_parseado.find('div', {'class':'container-w7c3sq'}).find_all('a')[0].text.strip()
    path_imagen = html_parseado.find('div', {'id': 'pdp-section-images'}).find_all('img')[0].get('src')
    guardar_imagen('http:' + path_imagen)

    datos_csv.append({'Marca' : marca, 'Modelo' : titulo_producto, 'Precio' : precio, 
                      'P/N' : p_n, 'Valoración' : estrellas, 'Valoraciones 5 estrellas' : estrellas_5,
                      'Valoraciones 4 estrellas' : estrellas_4, 'Valoraciones 3 estrellas' : estrellas_3,
                      'Valoraciones 2 estrellas' : estrellas_2, 'Valoraciones 1 estrellas' : estrellas_1})
    
    print(f'Producto {titulo_producto} añadido a la lista')

def guardar_imagen(path_imagen):
    response = requests.get(path_imagen)
    if response.status_code == 200:
        with open(os.path.join('data/images', path_imagen.split('/')[-1]), 'wb') as file:
            file.write(response.content)
    else:
        print(f'Error al guardar la imagen del producto {path_imagen.split('/')[-1]}')  

def borrar_datos_ejecucion_previa():
    if os.path.exists(archivo_csv):
        os.remove(archivo_csv)
    
    imagenes = 'data/images'
    if os.path.exists(imagenes):
        for archivo in os.listdir(imagenes):
            os.remove(os.path.join(imagenes, archivo))

if __name__ == '__main__':
    borrar_datos_ejecucion_previa()
    obtencion_datos_web(url_general)
    

    