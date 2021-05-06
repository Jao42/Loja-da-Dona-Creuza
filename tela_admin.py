from centralizar_tela import *
from tkinter import *
from produtos import addProdutoTable
import config

def telaAdmin():
  telaADM = Toplevel()
  telaADM.title('ADMIN')
  telaADM.configure(bg=config.COR_BG2)
  telaADM.geometry('1366x768')

  # CRIANDO FRAME A ESQUERDA
  Left = Frame(telaADM, width=700, height=768, bg=config.COR_BG3)
  Left.pack(side=LEFT)

  # CRIANDO FRAME A DIREITA
  Right = Frame(telaADM, width=666, height=768, bg=config.COR_BG)
  Right.pack(side=RIGHT)

  # INSERINDO ELEMENTOS A FRAME DA ESQUERDA
  img = PhotoImage(file='./imgs/circulo-superior-preto.png')
  lblimg = Label(Left, image=img, bg=config.COR_BG3)
  lblimg.place(x=0, y=0)

  Label(Left, text='REGISTRO DE PRODUTOS', font="Arial 30 bold", bg=config.COR_BG3, fg=config.COR_BG2
        ).place(x=75, y=250)
  Label(Left, text='OLÁ ADMINSTRADOR! \nFAÇA O REGISTRO DE PRODUTOS AO LADO.\nNÃO ESQUEÇA DE NADA ;)',
        font='Arial 17',
        bg=config.COR_BG3,
        fg=config.COR_BG2,
        justify=LEFT).place(x=75, y=320)

  # INSERINDO ELEMENTOS NA FRAME DA DIREITA
  logo = PhotoImage(file='./imgs/logotipo.preto.png')
  lbllogo = Label(Right, image=logo, bg=config.COR_BG)
  lbllogo.place(x=200, y=80)

  img2 = PhotoImage(file='./imgs/onda.png')
  lblimg2 = Label(Right, image=img2, bg=config.COR_BG)
  lblimg2.place(x=15, y=355)

  nomeProduto = StringVar()
  precoProduto = StringVar()
  nomeImg = StringVar()
  quantProduto = StringVar()

  labelNome = Label(Right, text="NOME DO PRODUTO:", font='Arial 14', bg=config.COR_BG)
  labelPreco = Label(Right, text="PREÇO DO PRODUTO:", font='Arial 14', bg=config.COR_BG)
  labelQuantidade = Label(Right, text="QUANTIDADE:", font='Arial 14', bg=config.COR_BG)
  entryNome = Entry(Right, textvariable=nomeProduto)
  entryPreco = Entry(Right, textvariable=precoProduto)
  entryQuantidade = Entry(Right, textvariable=quantProduto)

  labelNome.place(x=60, y=250)
  entryNome.place(x=60, y=280, width=400, height=25)
  labelPreco.place(x=60, y=320)
  entryPreco.place(x=60, y=350, width=400, height=25)
  labelQuantidade.place(x=60, y=390)
  entryQuantidade.place(x=60, y=420, width=400, height=25)


  labelMensagem = Label(Right, bg=config.COR_BG)
  labelMensagem.place(x=200, y=10)

  Button(Right, text="Adicionar produto",font='Arial 12', height=2, width=20,
         command=lambda: addProdutoTable(nomeProduto.get(), int(precoProduto.get()), int(quantProduto.get()), labelMensagem)).place(x=150, y=470)

  telaADM.mainloop()

if __name__ == "__main__":
  telaAdmin()
