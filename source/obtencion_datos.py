from bs4 import BeautifulSoup as bs
from selenium import webdriver as wb
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from urllib.request import Request, urlopen
from time import sleep

def obtencion_urls(web):
    '''
    Esta funcion la usaremos para extraer las urls de los diferentes productos (En este caso los telefonos) para despues extraer los detalles de los mismos

    Entrada: <str> web (web de la que queremos extraer los datos)
    Salida : <lista> res (lista con las urls de los productos)
    
    '''
    res = []
    # Configurar opciones de Firefox
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument("-headless")
    options.add_argument("-private")

    # Opcional: proxy
    # proxy = Proxy()
    # proxy.proxy_type = ProxyType.MANUAL
    # proxy.http_proxy = "http.proxy:1234"
    # options.proxy = proxy

    service = Service("./geckodriver.exe")
    driver = wb.Firefox(service=service, options=options)

    wait = WebDriverWait(driver, 10)

    driver.get(web)

    # Cookies
    wait.until(EC.element_to_be_clickable((By.ID, "cookiesrejectAll"))).click()

    # Navegación hasta la sección de teléfonos
    wait.until(EC.element_to_be_clickable((By.ID,"menu-btn-text"))).click()
    wait.until(EC.element_to_be_clickable((By.ID,"first-level-section-2-15033"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"typography-module_body2Regular__LOgUw"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"mainWrapper-uv_VtK"))).find_element(By.CLASS_NAME,"titleInnerLinkText-B4sfyG").click()

    # Extracción de URLs
    for i in range(2):
        for _ in range(3):  # reintenta hasta 3 veces
            try:
                lista_hrefs = [
                    movil.get_attribute("href")
                    for movil in WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, ".link-module_wrapper__DMT-Z.link-module_notDecorated__B-zTb.link-O9JV8C")
                        )
                    )
                ]
                break  # si funciona, sal del bucle
            except StaleElementReferenceException:
                continue
        res.extend(lista_hrefs)

        # Click en siguiente página
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="icon_right"]')))
        next_button.click()

    driver.quit()
    print(res)
    return res

if __name__ == '__main__':

    lista_urls = obtencion_urls('https://www.pccomponentes.com/')

