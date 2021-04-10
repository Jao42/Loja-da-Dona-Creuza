from tkinter import *
from login import *
from centralizar_tela import *

def tela_login(main):
  tela_login = Toplevel(main)

  centralizarTela(tela_login, 600, 500)

  tela_login.title("Login")

  email_usuario = StringVar()
  senha = StringVar()

  label_email_usuario = Label(tela_login, text="Digite o seu email ou usuário: ", height="3")
  label_senha = Label(tela_login, text="Digite a sua senha: ", height="3")

  email_usuario_entrada = Entry(tela_login, textvariable=email_usuario, width="40")
  senha_entrada = Entry(tela_login, textvariable=senha, width="25", show="*")

  label_email_usuario.pack()
  email_usuario_entrada.pack()
  label_senha.pack()
  senha_entrada.pack()


  Button(tela_login, text="Login", height="2", width="30", command=lambda: displayVerifLogin(email_usuario, senha, tela_login)).pack(side=BOTTOM)

