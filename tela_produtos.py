from tkinter import *
from tkinter import ttk
from centralizar_tela import centralizarTela
from produtos import tableProdutos, comprarProduto, promocao
import sqlite3
from time import localtime

def promocao(inicio, fim):
  hora = localtime().tm_hour
  if not (hora >= inicio and hora < fim):
    return 0
  return 1

     

def telaProdutos(tela_login):
  tela = Toplevel(tela_login)
  centralizarTela(tela, 600, 500)
  tela.title('estoque')

  #relief --> estilo da borda

  body = Frame(tela, borderwidth=2, relief='solid') 
  tabelaItems=['nome', 'preco', 'promocao', 'qtd']

#selectmode -> quantos items seleciona com mouse
#treeView heigth -> quantas rows
  scrollbarY = Scrollbar(body, orient=VERTICAL)
  scrollbarX = Scrollbar(body, orient=HORIZONTAL)

  tree = ttk.Treeview(
      body, columns=(tabelaItems[0], tabelaItems[1], tabelaItems[2], tabelaItems[3]), selectmode="extended", height=5,
      yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)

  scrollbarY.config(command=tree.yview)
  scrollbarX.config(command=tree.xview)
  scrollbarY.pack(side=RIGHT, fill=Y)
  scrollbarX.pack(side=BOTTOM, fill=X)

  style = ttk.Style(body)
  style.configure('Treeview', rowheight=60)

  tree.heading(tabelaItems[0], text=tabelaItems[0])
  tree.heading(tabelaItems[1], text=tabelaItems[1])
  tree.heading(tabelaItems[2], text=tabelaItems[2])
  tree.heading(tabelaItems[3], text=tabelaItems[3])

  tree.column('#0', minwidth=0, width=0)
  tree.column('#1', anchor="center", minwidth=0, width=200)
  tree.column('#2', anchor="center", minwidth=0, width=150)
  tree.column('#3', anchor="center", minwidth=0, width=100)
  tree.column('#4', anchor="center", minwidth=0, width=50)

  horaPromocao = bool(promocao(8, 10))
  tableProdutos(tree, body, horaPromocao)

  Button(tela, text="COMPRAR", command=lambda:comprarProduto(tree)).pack(side=BOTTOM)
  
  promocaoLabel = Label(tela)
  promocaoLabel.pack()
  if horaPromocao:
    promocaoLabel['text'] = 'PROMOÇÃO! Produtos com mais de 20% de desconto!'
    promocaoLabel['fg'] = 'blue'
  tela.mainloop()


if __name__ == '__main__':
  telaProdutos()
