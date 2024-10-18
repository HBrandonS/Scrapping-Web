# Librerias que se van a utilizar
import requests, mechanize, re
from bs4 import BeautifulSoup
from Wappalyzer import Wappalyzer, WebPage

#1 Primer uso de la libreria REQUESTS
website = input(str("Digite la pagina para hacer Scrapping Web: ")) #Se obtiene pagina
req_response = requests.get(website)

#1.2 Condicion en caso de encontrar la pagina o no encontrarla usando REQUESTS
if req_response.status_code == 200: #Codigo 200 "Succesfull"
    req_content = req_response.content
else:
    print("La pagina web digitada no esta disponible:", req_response.status_code)

#2 Primer uso de la libreria MECHANIZE
browser = mechanize.Browser() #Objeto que se comportara como navegador
browser.set_handle_robots(False) #Ignorar reglas de Rastreadores Web
browser.addheaders = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36"
)]

#2.1 Se utiliza MECHANIZER para navegar por el sitio web
browser.open(website) #Se abre la pagina web
print(f"El titulo de la pagina {website} es:", browser.title) #Titulo de la pagina
enlaces = [enlace.url for enlace in browser.links()] #Enlaces de la pagina 
print(f"Enlaces de la pagina {website}") # Se imprimen los enlaces
for enlace in enlaces:
    print(enlace)
if enlaces:
    primer_enlace = enlaces[0]
    print("Siguiendo el primer enlace: ", primer_enlace)
    browser.follow_link(url = primer_enlace)
    print("Titulo de la pagina secundaria: ", browser.title()) #Se imprime el titulo del link
else:
    print(f"No se encontraron links en {website}")

# 3 Primer uso de la libreria Wappalyzer
wapp = Wappalyzer.latest() #Se usa ultima version
webpag = WebPage.new_from_url(website) #Descarga el contenido y analiza
results = wapp.analyze(webpag) #Resultados
print(f"Las tecnologias que se usan en {website} son, {results}") #Se imprime la informacion obtenida

# 4 Se utiliza por primera vez BEAUTIFULSOUP para analiar y extraer la informacion de una imagen
req_content = req_response.content 
beauti = BeautifulSoup(req_content, "html.parser")

#7.- Procesar la información (imagenes) utilizando expresiones regulares
img_element = beauti.find('img')
if img_element:# Verificar si se encontró una imagen
    src = img_element.get('src')
    alt = img_element.get('alt')
    pattern = re.compile(r'\b(\w+)\b')  # Expresión regular para encontrar palabras individuales
    src_words = [match.group(0) for match in pattern.finditer(src)]
    alt_words = [match.group(0) for match in pattern.finditer(alt)]
    # Imprimir la información ordenada de la imagen
    print("Fuente de la imagen:", ' '.join(src_words))
    print("Descripción de la imagen:", ' '.join(alt_words))
else:
    print("No se encontró ninguna imagen en la página.")