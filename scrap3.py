#Importando librerías
import requests
from bs4 import BeautifulSoup

#configuración de URL
URL = 'https://anpemurcia.es'

#realizar la petición GET a la url
reqs = requests.get(URL)

#extraer todo el texto que ha recibido de
#la solicitud GET
content = reqs.text

#convertir el texto en un objeto beautifulsoup
soup = BeautifulSoup(content, 'html.parser')

#Lista vacía para almacenar la salida
urls = []

#Bucle For que itera sobre todas las etiquetas <h5>
for h in soup.findAll('h5'):
    
    #buscando la etiqueta de anclaje dentro de la etiqueta <h5>
    a = h.find('a')
    try:
        
        #buscando la etiqueta de anclaje dentro de la etiqueta <h5>
        if 'href' in a.attrs:
            #almacenar el valor de href en una variable separada
            url = a.get('href')
            
            #añadir la url a la lista de salida
            urls.append(url)
            
            
    #si la lista no tiene una etiqueta de anclaje
    #o una etiqueta de anclaje no tiene un parámetro href pasamos
    except:
        pass
    


#imprimir todas las urls almacenadas en la lista de urls
for url in urls:
    print(url)
