import requests
from bs4 import BeautifulSoup

# Descargar el contenido de la página web
url = "https://siata.gov.co/"
response = requests.get(url)

# Analizar la estructura de la página web con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Buscar todos los enlaces en la página web
links = soup.find_all("a")

# Filtrar los enlaces para obtener solo los que apuntan a directorios
directories = []
for link in links:
    if "href" in link.attrs and link["href"].endswith("/"):
        directories.append(link["href"])

# Imprimir los directorios
print("Directorios:")
for directory in directories:
    print(directory)

