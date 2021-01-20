from scraper import scraper
import psycopg2

#Conectando ao banco de dados
DB_NAME = "ScraperBoaDica"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")
cur = conn.cursor()
cur.execute("DELETE FROM videogamesony")
conn.commit()

Url = "TEST"
# Função de scraping
scraper(Url,cur,conn)
