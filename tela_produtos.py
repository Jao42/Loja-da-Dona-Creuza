from tkinter import *
from tkinter import ttk
from centralizar_tela import centralizarTela
from produtos import tableProdutos, rmProdutoTable
import sqlite3

def telaProdutos(tela_login):
  tela = Toplevel(tela_login)
  centralizarTela(tela, 600, 500)
  tela.title('estoque')

  #relief --> estilo da borda

  body = Frame(tela, borderwidth=2, relief='solid') 
  tabelaItems=['nome', 'preço']

#selectmode -> quantos items seleciona com mouse
#treeView heigth -> quantas rows
  scrollbarY = Scrollbar(body, orient=VERTICAL)
  scrollbarX = Scrollbar(body, orient=HORIZONTAL)

  tree = ttk.Treeview(
      body, columns=(tabelaItems[0], tabelaItems[1]), selectmode="extended", height=5,
      yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set
      )

  scrollbarY.config(command=tree.yview)
  scrollbarX.config(command=tree.xview)
  scrollbarY.pack(side=RIGHT, fill=Y)
  scrollbarX.pack(side=BOTTOM, fill=X)

  style = ttk.Style(body)
  style.configure('Treeview', rowheight=60)

  tree.heading(tabelaItems[0], text='produto')
  tree.heading(tabelaItems[1], text='preço')

  tree.column('#0', minwidth=0, width=0)
  tree.column('#1', anchor="center", minwidth=0, width=250)
  tree.column('#2', anchor="center", minwidth=0, width=250)

  tableProdutos(tree, body)
  Button(tela, text="COMPRAR", command=lambda:rmProdutoTable(tree)).pack(side=BOTTOM)

  tela.mainloop()
