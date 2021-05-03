import sqlite3 

conexao = sqlite3.connect('db-loja.db')


cursor = conexao.cursor() 
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()
print(produtos)

conexao.commit()
conexao.close()
