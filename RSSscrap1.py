#Importando librerías
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#importar pandas para crear dataframe y csv
import pandas as pd

#Lista vacía para almacenar las etiquetas por separado y guardarlas
news_items = []

#el fichero "ANPES.txt" contiene las urls de las secciones RSS de los distintos ANPEs. ejem: https://anpemurcia.es/rss.php
#usar "open" con segundo parámetro "r" (read only) encapsulado en un bloque "with" para abrir un fichero de texto que
#contiene la URLs correspondientes iterando sobre las mismas con un "for" (el "with" hará que el fichero se cierre 
# cuando ya no se necesite)("strip()" función que elimina espacios, tabulaciones, nuevas líneas..etc al principio
# y al final de cada línea)
with open('ANPES.txt', 'r') as url_file:
    for line in url_file:
        URL = line.strip()
        reqs =requests.get(URL)
        content = reqs.text
        soup = BeautifulSoup(reqs.content, features="xml")
        
        #encontrar la etiqueta generator donde se muestra el ANPE que es
        generator = soup.find('generator').get_text()

        #encontrar todas las etiquetas "item"
        items = soup.find_all('item')
        
        #iterar sobre los items cogiendo los tags que nos interesan, creando para ello un diccionario
        for item in items:
            news_item = {}
            news_item['generator'] = generator
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text
            news_item['link'] = item.link.text
            news_item['pubDate'] = item.pubDate.text
            news_items.append(news_item)
            
#usar pandas para crear dataframe y exportarlo. Docu de pandas: https://pandas.pydata.org/
nombre = "ANPE-"+datetime.now().strftime("%Y-%m-%d")
df = pd.DataFrame(news_items,columns=['generator','title','description','link','pubDate'])

df.head()

df.to_csv(nombre+'.csv',index=False, encoding='utf-8')
df.to_excel(nombre+'.xlsx',index=False, encoding='utf-8')
df.to_html(nombre+'.html',index=False, encoding='utf-8', render_links=True)
