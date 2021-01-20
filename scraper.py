from bs4 import BeautifulSoup
import requests
import string
import random
from itertools import count


def scraper(Url, cur, conn):
  i = 1
  while(True):
      print(i)
      # Pegando lista de produto da pagina
      Url = "https://www.boadica.com.br/pesquisa/multi_playstation/precos?ClasseProdutoX=2&CodCategoriaX=13&XT=8&XE=1&XF=48&curpage={}".format(i)
      html_text = requests.get(Url).text

      if "Nenhum resultado nesta categoria." in html_text:
          print("Fim das paginas")
          break                           
      else:
          soup = BeautifulSoup(html_text, 'lxml')
          produtos = soup.find_all('div', class_ = 'row preco detalhe')
          random.seed()
          for produto in produtos:
              separator = ''

              # Pegando preco do produto
              preco_produto = str(produto.find('div', class_='col-md-1 preco').text.replace('\n', '').replace(' ', '')).split()
              preco_produto = separator.join(preco_produto)

              #Pegando modelo do produto
              coluna_modelo = produto.find('div', class_='col-md-2 center')
              modelo_produto = coluna_modelo.find('div', class_='no-mobile').text.split()
              modelo_produto = separator.join(modelo_produto)

              #Gerando a ID chave primária
              id_produto = random.randint(1,999999999)

              #Inserindo no banco de dados
              cur.execute("INSERT INTO videogamesony VALUES (%s, %s, %s)", (id_produto, modelo_produto, preco_produto))
              conn.commit()
              print("Entrada inserida em banco")
      i = i + 1