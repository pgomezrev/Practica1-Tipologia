from obtencion_datos import obtencion_urls
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

url_general = 'https://www.pccomponentes.com/'
scraper_api_key = '4498f114a561c6e7a433fb5a51194227'
archivo_csv = 'dataset/productos.csv'
path_imagenes = 'dataset/images'

def obtencion_datos_web(web):
    '''
        obtenemos una lista de URL a las que hacer peticiones web. Iteramos sobre ellas para rellenar la lista con los diccionarios de datos y finalmente creamos el csv con la información.

        Args:
            web: página web base sobre la que vamos a sacar el listado de URLs.
    '''
    datos_csv = []
    # sacar URLs para sacar los datos
    web_urls = obtencion_urls(web)
    # iteramos por cada URL obtenida
    for web_url in web_urls:
        # sacamos los datos para el csv y guardamos la imagen
        obtener_dato(datos_csv, web_url)
    
    # creamos el archivo csv
    df = pd.DataFrame(datos_csv)
    df.to_csv(archivo_csv, index=False, sep=';', encoding='utf-8')

def obtener_dato(datos_csv, web_url):
    '''
        Hacemos la petición http mediante el uso de scraper_api, de esta manera no recibimos error 403: Forbbiden. Después la añadimos a la lista final.

        Args:
            datos_csv: lista que contiene los diccionarios de cada producto
            web_url: URL de la siguiente página que queremos procesar
    '''
    # abrimos sesión para hacer un request y utilizamos scraper_api
    session = requests.Session()
    scraper_api_url = f"http://api.scraperapi.com/?api_key={scraper_api_key}&url={web_url}"
    response = requests.get(scraper_api_url)

    # si la petición ha ido correcta, guardamos los datos
    if response.status_code == 200:
        datos_csv.append(extraer_datos(response))
    else:
        print(f"Error {response.status_code} en la peticion a la url {web_url}")
    

def extraer_datos(response):
    '''
    Parseamos el HTML y sacamos los datos e imagenes necesarias.

    Args:
        response: respuesta de la petición http previamente hecha

    Returns:
        diccionario con la información del producto
    '''
    # parseamos HTML
    html_parseado = BeautifulSoup(response.text, 'html.parser')
    # sacamos los datos que nos interesan del html
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
    # sacamos la primera imagen de la web para descargarla
    path_imagen = html_parseado.find('div', {'id': 'pdp-section-images'}).find_all('img')[0].get('src')
    guardar_imagen('http:' + path_imagen)

    # añadimos la lista de productos la información sacada
    return {'Marca' : marca, 'Modelo' : titulo_producto, 'Precio' : precio, 
                      'P/N' : p_n, 'Valoración' : estrellas, 'Valoraciones 5 estrellas' : estrellas_5,
                      'Valoraciones 4 estrellas' : estrellas_4, 'Valoraciones 3 estrellas' : estrellas_3,
                      'Valoraciones 2 estrellas' : estrellas_2, 'Valoraciones 1 estrellas' : estrellas_1}
    
    print(f'Producto {titulo_producto} añadido a la lista')

def guardar_imagen(path_imagen):
    '''
    Se hace petición http para descargar la imágen y la guardamos en {path_imagenes}

    Args:
        path_imagen: La URL de la imagen que queremos descargar
    '''
    # hacemos una petición para sacar la imagen
    response = requests.get(path_imagen)
    if response.status_code == 200:
        # si ha ido bien guardamos la imagen
        with open(os.path.join(path_imagenes, path_imagen.split('/')[-1]), 'wb') as file:
            file.write(response.content)
    else:
        print(f'Error al guardar la imagen del producto {path_imagen.split('/')[-1]}')  

def borrar_datos_ejecucion_previa():
    '''
    Borra el archivo csv y las imágenes de la ejecución previa.
    '''
    if os.path.exists(archivo_csv):
        os.remove(archivo_csv)
    
    if os.path.exists(path_imagenes):
        for archivo in os.listdir(path_imagenes):
            os.remove(os.path.join(path_imagenes, archivo))

if __name__ == '__main__':
    '''
    Función de ejecución principal
    '''
    # borramos los datos de la ejecución anterior
    borrar_datos_ejecucion_previa()
    # obtenemos los datos
    obtencion_datos_web(url_general)
    

    
