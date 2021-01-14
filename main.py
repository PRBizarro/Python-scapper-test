from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.boadica.com.br/pesquisa/multi_playstation/precos?ClasseProdutoX=2&CodCategoriaX=13&XF=48&XT=8&XE=1&modelo=179320&regiao=&em_box=&cl=&preco_min=&preco_max=').text
soup = BeautifulSoup(html_text, 'lxml')
precos = soup.find_all('div', class_='row preco detalhe')
print(precos)
