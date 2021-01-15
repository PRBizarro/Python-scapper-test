from bs4 import BeautifulSoup
import requests
import string

# Pegando lista de produtos
html_text = requests.get('https://www.boadica.com.br/pesquisa/multi_playstation/precos?ClasseProdutoX=2&CodCategoriaX=13&XT=8&XE=1&XF=48').text
soup = BeautifulSoup(html_text, 'lxml')
produtos = soup.find_all('div', class_ = 'row preco detalhe')

for produto in produtos:
    # Pegando preco do produto
    preco_produto = produto.find('div', class_='col-md-1 preco').text.replace('\n', '').replace(' ', '')

    #Pegando o modelo do produto
    coluna_modelo = produto.find('div', class_='col-md-2 center')
    modelo_produto = coluna_modelo.find('div', class_='no-mobile').text.split()
    separator = ''
    modelo_produto =separator.join(modelo_produto)
        

    print("Preço do produto:")
    print(preco_produto)
    print("Modelo do produto:")
    print(modelo_produto)
    print('')
