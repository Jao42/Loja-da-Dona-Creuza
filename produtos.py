import sqlite3
from tkinter import *
from tkinter import ttk
from time import localtime
from math import ceil
from operacoes_db import atualizarPontos

def createTableProdutos():
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute("""CREATE TABLE produtos (
    nome text,
    preco integer,
    quantidade integer
  )""")
  conexao.commit()
  conexao.close()

def dropTableProdutos():
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor = cursor.execute("DROP TABLE produtos")
  conexao.commit()
  conexao.close()

def addProdutoTable(nome, preco, qtd, label):
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute(f"SELECT nome FROM produtos WHERE nome='{nome}'")
  existencia = cursor.fetchone()
  conexao.commit()
  
  if not existencia:
    cursor.execute(f"INSERT INTO produtos VALUES ('{nome}', '{preco}', '{qtd}')")
    conexao.commit()
    conexao.close()

    label['text'] = 'Produto cadastrado com sucesso!'
    label['fg'] = 'green'
    return 0

  conexao.close()
  label['text'] = 'Produto já cadastrado!'
  label['fg'] = 'red'
  return 1

def rmProdutoTable(tree):
  itemIID = tree.focus()

  if itemIID:
    nomeProduto = tree.item(itemIID)['values'][0]

    conexao = sqlite3.connect("db-loja.db")
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM produtos WHERE nome='{nomeProduto}'")
    conexao.commit()
    conexao.close()

    tree.delete(itemIID)
    return 0

  return 1

def comprarProduto(tree, label_usuario_pontos, usuario):
  itemIID = tree.focus()
  itemValues = tree.item(itemIID)['values']

  nome = itemValues[0]
  preco = int(itemValues[1])
  promocao = itemValues[2]
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()

  cursor.execute(f"SELECT pontos FROM usuarios WHERE usuario = '{usuario}'")
  pontos = cursor.fetchone()[0]

  conexao.commit()
  conexao.close()
  
  if promocao:
    if (pontos - int(promocao)) < 0:
      return 1
    novosPontos = pontos - int(promocao)
    atualizarPontos(usuario, novosPontos)

  else:
    if (pontos - preco) < 0:
      return 1 
    novosPontos = pontos - preco
    atualizarPontos(usuario, novosPontos)

  label_usuario_pontos['text'] = f'{usuario} --> {novosPontos}'

  qtd = int(itemValues[3])
  if qtd == 1:
    rmProdutoTable(tree)   
    return 0
   
  tree.item(itemIID, text="", values=(itemValues[0], itemValues[1], itemValues[2], str(qtd - 1)))

  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute(f"""UPDATE produtos SET quantidade='{qtd - 1}'
        WHERE nome='{nome}' AND preco='{preco}' AND quantidade='{qtd}'
      
      """)
  conexao.commit()
  conexao.close()

  return 0

def promocao(inicio, fim):
  hora = localtime().tm_hour
  if hora >= inicio and hora < fim:
    return 1
  else:
    return 0

def tableProdutos(tree, body, horaPromocao):
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM produtos")
  produtos = cursor.fetchall()

  promocao = 1 - 20/100
  valorMinimo = ceil(1/promocao)
  cursor.execute(f"SELECT preco FROM produtos WHERE preco >= {valorMinimo}")
  temProdutoPromocao = bool(cursor.fetchall())
  conexao.commit()
  conexao.close()

  for i in produtos:

    promocaoProduto = ''
    if horaPromocao and i[1] >= valorMinimo:
      promocaoProduto = int(i[1] * promocao)
    tree.insert('', 'end', values=(i[0], str(i[1]), str(promocaoProduto), str(i[2])))

  body.pack()
  tree.pack(side=BOTTOM)

  return temProdutoPromocao 
