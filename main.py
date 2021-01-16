from bs4 import BeautifulSoup
import requests
import string
import psycopg2
import random


#Conectando ao banco de dados
DB_NAME = "ScraperBoaDica"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")

cur = conn.cursor()

############################################## INSERIR FUNÇÃO FOR PARA PAGINAÇÃO
# Pegando lista de produtos
html_text = requests.get('https://www.boadica.com.br/pesquisa/multi_playstation/precos?ClasseProdutoX=2&CodCategoriaX=13&XT=8&XE=1&XF=48&curpage=2').text
soup = BeautifulSoup(html_text, 'lxml')
produtos = soup.find_all('div', class_ = 'row preco detalhe')
random.seed()

for produto in produtos:
    # Pegando preco do produto
    preco_produto = produto.find('div', class_='col-md-1 preco').text.replace('\n', '').replace(' ', '')

    #Pegando o modelo do produto
    coluna_modelo = produto.find('div', class_='col-md-2 center')
    modelo_produto = coluna_modelo.find('div', class_='no-mobile').text.split()
    separator = ''
    modelo_produto = separator.join(modelo_produto)

    #Gerando a ID chave primária
    id = random.randint(1,999999999)

    #Inserindo no banco de dados
    cur.execute("INSERT INTO VIDEOGAMESONY (ID, MODELO, PRECO) VALUES({}, '{}', '{}')".format(id,modelo_produto,preco_produto))### preco_produto nao está sendo passado para banco (revisar)
    conn.commit()
    print("ID {}, PREÇO {}, MODELO {} INSERIDOS".format(id,modelo_produto,preco_produto))
   
