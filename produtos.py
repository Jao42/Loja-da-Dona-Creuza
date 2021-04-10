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
  cursor.execute(f"INSERT INTO produtos VALUES ('{nome}', '{preco}')")
  conexao.commit()
  conexao.close()


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


