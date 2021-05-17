from tkinter import *
from tela_cadastro import *
from tela_login import *
from centralizar_tela import *
import config
import os

def telaInicial():
  tela_inicial = Tk()
  tela_inicial.geometry('1366x768')

  tela_inicial.resizable(False, False)

  tela_inicial.title("Lojinha da Dona Creuza :)")
  tela_inicial.configure(bg=config.COR_BG)

  # CRIANDO FRAME A ESQUERDA
  Left = Frame(tela_inicial, width=700, height=768, bg=config.COR_BG3)
  Left.pack(side=LEFT)

  # CRIANDO FRAME A DIREITA
  Right = Frame(tela_inicial, width=666, height=768, bg=config.COR_BG3)
  Right.pack(side=RIGHT)

  # INSERINDO DESIGN NO FRAME DA DIREITA
  img = PhotoImage(file="./imgs/design.png")
  lbldesign = Label(Right, image=img)
  lbldesign.pack()

  # INSERINDO IMAGEM NO FRAME DA ESQUERDA
  img2 = PhotoImage(file="./imgs/circulo-inferior-preto.png")
  lblimg = Label(Left, image=img2, bg=config.COR_BG3)
  lblimg.place(x=0, y=380)


  # INSERINDO TEXTO E LOGO NO FRAME DA ESQUERDA
  logo = PhotoImage(file="./imgs/logotipo-grande.png")
  lbllogo = Label(Left, image=logo, bg=config.COR_BG3)
  lbllogo.place(x=0, y=20)

  Label(Left, text=
  """
  A LOJINHA DA DONA CREUZA É UMA LOJA VIRTUAL DE VARIEDADES, AQUI
  VOCÊ ENCONTRARÁ DE PRODUTOS ELETRÔNICOS A ALIMENTOS.
  POSSUÍMOS MARCAS DE QUALIDADE E NOSSO ATENDIMENTO É PENSADO
  NO BEM ESTAR DOS NOSSOS CLIENTES, ALÉM DE POSSUÍMOS PROMOCOES
  QUE VOCÊ NÃO ENCONTRARÁ EM OUTRO LUGAR!
  TÁ ESPERANDO O QUE MENINO? VENHA SER NOSSO CLIENTE!
  """,
        bg=config.COR_BG3,
        fg=config.COR_BG,
        font='Arial 12',
        justify=LEFT).place(x=50, y=300)

  # INSERINDO BUTTON NO FRAME DA ESQUERDA 
  bnt1 = Button(Left, text='Entrar', font='Arial 13', bg=config.COR_BG2, command=telaCadastro, width=13, height=2)

  bnt1.place(x=230, y=450)
  tela_inicial.mainloop()



telaInicial()


