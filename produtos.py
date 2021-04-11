import sqlite3
from tkinter import *
from tkinter import ttk


def createTableProdutos():
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute("""CREATE TABLE produtos (
    nome text,
    preco integer
  )""")
  conexao.commit()
  conexao.close()

def dropTableProdutos():
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor = cursor.execute("DROP TABLE produtos")
  conexao.commit()
  conexao.close()

def addProdutoTable(nome, preco):
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute(f"SELECT nome, preco FROM produtos WHERE nome='{nome}' AND preco='{preco}'")
  existencia = cursor.fetchone()
  conexao.commit()
  if not existencia:
    cursor.execute(f"INSERT INTO produtos VALUES ('{nome}', '{preco}')")
    conexao.commit()
    conexao.close()
    return 0
  conexao.close()
  return 1

def rmProdutoTable(tree):
  itemIID = tree.focus()

  if itemIID:
    nomeProduto = tree.item(itemIID)['values'][0]
    precoProduto = tree.item(itemIID)['values'][1]

    conexao = sqlite3.connect("db-loja.db")
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM produtos WHERE nome='{nomeProduto}' AND preco={precoProduto}")
    conexao.commit()
    conexao.close()

    tree.delete(itemIID)
    return 0

  return 1
  
  

def tableProdutos(tree, body):
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM produtos")

  produtos = cursor.fetchall()

  for i in produtos:
    tree.insert('', 'end', values=(i[0], str(i[1])))

  body.pack()
  tree.pack(side=BOTTOM)

  conexao.commit()
  conexao.close()

  return produtos


if __name__ == '__main__':
  addProdutoTable('sabao', 4)
  addProdutoTable('monark da boa', 20)
  addProdutoTable('outfit da lacoste', 10)
  addProdutoTable('velharia', 2)
