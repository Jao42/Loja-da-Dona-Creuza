import sqlite3

conexao = sqlite3.connect('db-loja.db')
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE usuarios (
    usuario text,
    email text,
    senha text
)""")

conexao.commit()
conexao.close()
