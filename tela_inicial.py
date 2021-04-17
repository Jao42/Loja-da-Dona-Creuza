from tkinter import *
from tela_cadastro import *
from tela_login import *
from centralizar_tela import *
import config
import os

def telaInicial():
  tela_inicial = Tk()
  centralizarTela(tela_inicial, 600, 500)

  tela_inicial.title("Lojinha da Dona Creuza :)")
  tela_inicial.configure(bg=config.COR_BG)

  Label(text="Bem Vindo a Lojinha da Dona Creuza!",
      bg=config.COR_BG,
      height="3",
      font='Calibrin 19 bold').place(x=30, y=30)

  imagem = PhotoImage(file="./imgs/dona-creuza-peq.png")

  Label(image=imagem,
      bg=config.COR_BG,
      bd=2,
      relief='solid').place(x=40, y=150)

  Label(text="Essa é a Dona Creuza :3", 
      fg="Black", 
      bg=config.COR_BG,
      font='Arial 11 italic').place(x=27, y=360)


  Label(text="Se você ainda não se registrou, clique em \"Registrar\"", 
    bg=config.COR_BG, 
    font='Arial 12', 
    anchor=CENTER).place(x=200, y=170)

  Label(text="Se já se registrou, clique em \"Login\"",
      bg=config.COR_BG,
      font='Arial 11',
      anchor=CENTER).place(x=250, y=195)

  Button(text="Registrar",
      height="2",
      width="30",
      bg="#ffffcc",
      command=lambda: telaCadastro(tela_inicial)).place(x=260, y=230)

  Button(text="Login",
      height="2",
      width="30",
      bg="#ffffcc",
      command=lambda: telaLogin(tela_inicial)).place(x=260, y=270)

  tela_inicial.mainloop()


telaInicial()


