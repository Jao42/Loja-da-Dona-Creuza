from tkinter import *
from tkinter import ttk
from centralizar_tela import centralizarTela
from tela_minigame import telaMinigame
from produtos import tableProdutos, comprarProduto, promocao
import sqlite3
import config


def telaProdutos(usuario, pontos):
  tela = Toplevel()
  tela.configure(bg=config.COR_BG)
  centralizarTela(tela, 600, 500)
  tela.title('estoque')

  label_usuario_pontos = Label(tela, text=f"{usuario} --> {pontos}", bg=config.COR_BG, width=20)
  botaoMinigame = Button(tela, text='GANHAR PONTOS', width=15, command= lambda:telaMinigame(usuario, label_usuario_pontos))
  botaoMinigame.pack(anchor=W)
  label_usuario_pontos.pack()

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

  horaPromocao = promocao(8, 18)
  temProdutoPromocao = tableProdutos(tree, body, horaPromocao)

  Button(tela, text="COMPRAR", command = lambda:comprarProduto(tree, label_usuario_pontos, usuario)).pack(side=BOTTOM)
  
  promocaoLabel = Label(tela, bg=config.COR_BG)
  promocaoLabel.pack()
  if horaPromocao and temProdutoPromocao:
    promocaoLabel['text'] = 'PROMOÇÃO! Produtos com mais de 20% de desconto!'
    promocaoLabel['fg'] = 'blue'
    promocaoLabel['bg'] = config.COR_BG
  tela.mainloop()


