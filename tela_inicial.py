from tkinter import *
from tela_cadastro import *
from tela_login import *
from centralizar_tela import *

def tela_inicial():
  tela_inicial = Tk()

  centralizarTela(tela_inicial, 600, 500)

  tela_inicial.title("Lojinha da Dona Creuza :)")
  Label(text="Bem Vindo a Lojinha da Dona Creuza!", height="4").pack()

  imagem = PhotoImage(file="./imgs/dona-creuza-peq.png")
  Label(image=imagem).pack()
  Label(text="Essa é a Dona Creuza :3", foreground="gray").pack(pady=10)

  Label(text="Se você ainda não se registrou, clique em \"Registrar\"").pack()
  Label(text="Se já se registrou, clique em \"Login\" :)").pack()

  Button(text="Registrar", height="2", width="30", command=lambda: tela_cadastro(tela_inicial)).pack(side=BOTTOM)
  Button(text="Login", height="2", width="30", command=lambda: telaLogin(tela_inicial)).pack(side=BOTTOM)
  tela_inicial.mainloop()
tela_inicial()


