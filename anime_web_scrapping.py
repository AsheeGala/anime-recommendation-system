import requests
from bs4 import BeautifulSoup

url = "https://animeseries.so/search/character=special"
anime_links = []
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Getting links to the animes
links = soup.find('ul', class_="items").find_all('a')

for link in links:
    print(link.get('href'))
    anime_links.append(link.get('href'))


