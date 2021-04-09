import sqlite3


conexao = sqlite3.connect('db-loja.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

conexao.commit()
conexao.close()
