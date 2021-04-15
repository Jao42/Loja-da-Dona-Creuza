from tkinter import *
from login import *
from centralizar_tela import *
import config

def telaLogin(main):
  tela_login = Toplevel(main)
  tela_login.configure(bg=config.COR_BG)

  centralizarTela(tela_login, 600, 500)

  tela_login.title("Login")

  email_usuario = StringVar()
  senha = StringVar()

  label_email_usuario = Label(tela_login, text="Digite o seu email ou usuário: ", height="3", bg=config.COR_BG)
  label_senha = Label(tela_login, text="Digite a sua senha: ", height="3", bg=config.COR_BG)

  email_usuario_entrada = Entry(tela_login, textvariable=email_usuario, width="40")
  senha_entrada = Entry(tela_login, textvariable=senha, width="25", show="*")

  label_email_usuario.pack()
  email_usuario_entrada.pack()
  label_senha.pack()
  senha_entrada.pack()

  labelMensagem = Label(tela_login, bg=config.COR_BG)
  Button(tela_login, text="Login", height="2", width="30", command=lambda: displayVerifLogin(email_usuario, senha, tela_login, labelMensagem)).pack(side=BOTTOM)
  labelMensagem.pack()

