from tkinter import *
from tkinter import ttk
from centralizar_tela import centralizarTela
from tela_minigame import telaMinigame
from produtos import tableProdutos, comprarProduto, promocao
import config

def telaProdutos(usuario, pontos):
  tela = Toplevel()
  tela.configure(bg=config.COR_BG)
  tela.geometry('1366x768')
  tela.title('Estoque')

  tela.resizable(False, False)

  img = PhotoImage(file='./imgs/circulop.png')
  lblimg = Label(tela, image=img, bg=config.COR_BG)
  lblimg.place(x=0, y=0)
  img2 = PhotoImage(file='./imgs/onda.png')
  lblimg2 = Label(tela, image=img2, bg=config.COR_BG)
  lblimg2.place(x=665, y=370)

  label_usuario_pontos = Label(
    tela,
    text=f"{usuario} → {pontos}",
    font='Arial 15 bold',
    bg=config.COR_BG,
    width=20
  )

  botaoMinigame = Button(
      tela,
      text='GANHAR PONTOS',
      font='Arial 12',
      height=2,
      width=20,
      command=lambda: telaMinigame(usuario, label_usuario_pontos))

  botaoMinigame.place(x=470, y=600)
  label_usuario_pontos.pack()

  #relief --> estilo da borda

  body = Frame(tela, borderwidth=2, relief='solid')
  body.pack(side=TOP)
  tabelaItems = ['nome', 'preco', 'promocao', 'qtd']

#selectmode -> quantos items seleciona com mouse
#treeView heigth -> quantas rows
  scrollbarY = Scrollbar(body, orient=VERTICAL)
  scrollbarX = Scrollbar(body, orient=HORIZONTAL)

  tree = ttk.Treeview(
      body, columns=tabelaItems, selectmode="extended", height=8,
      yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)

  scrollbarY.config(command=tree.yview)
  scrollbarX.config(command=tree.xview)
  scrollbarY.pack(side=RIGHT, fill=Y)
  scrollbarX.pack(side=BOTTOM, fill=X)

  style = ttk.Style(body)
  style.configure('Treeview', rowheight=60)

  for i in tabelaItems:
    tree.heading(i, text=i)

  tree.column('#0', minwidth=0, width=0)
  tree.column('#1', anchor="center", minwidth=0, width=250)
  tree.column('#2', anchor="center", minwidth=0, width=150)
  tree.column('#3', anchor="center", minwidth=0, width=150)
  tree.column('#4', anchor="center", minwidth=0, width=100)

  horaPromocao = promocao(17, 23)
  temProdutoPromocao = tableProdutos(tree, body, horaPromocao)

  comprarButton = Button(
      tela,
      text="COMPRAR",
      font='Arial 12',
      height=2,
      width=20,
      command=lambda: comprarProduto(tree, label_usuario_pontos, usuario))

  comprarButton.place(x=700, y=600)

  promocaoLabel = Label(tela, bg=config.COR_BG)
  promocaoLabel.pack()
  if horaPromocao and temProdutoPromocao:
    promocaoLabel['text'] = 'PROMOÇÃO!' + ' Produtos com mais de 20% de desconto!'
    promocaoLabel['fg'] = 'blue'
    promocaoLabel['bg'] = config.COR_BG
  tela.mainloop()


