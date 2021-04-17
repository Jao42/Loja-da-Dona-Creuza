from tkinter import *
from login import *
from centralizar_tela import *
import config

def telaLogin():
  tela_login = Tk() 
  tela_login.configure(bg=config.COR_BG)

  centralizarTela(tela_login, 600, 500)

  tela_login.title("Login")

  email_usuario = StringVar()
  senha = StringVar()

  label_email_usuario = Label(tela_login, text="Digite o seu email ou usuário: ", height="3", font="Arial 12", bg=config.COR_BG)

  label_senha = Label(tela_login, text="Digite a sua senha: ", height="3", font='Arial 12', bg=config.COR_BG)

  email_usuario_entrada = Entry(tela_login, textvariable=email_usuario, width="40")
  senha_entrada = Entry(tela_login, textvariable=senha, width="25", show="*")

  label_email_usuario.place(x=30, y=30)
  email_usuario_entrada.place(x=30, y=70)

  label_senha.place(x=30, y=90)
  senha_entrada.place(x=30, y=130)

  labelMensagem = Label(tela_login, bg=config.COR_BG)
  labelMensagem['bg'] = config.COR_BG
  labelMensagem.pack()

  Button(tela_login, text="Login", height="2", width="30", command=lambda: displayVerifLogin(email_usuario, senha, tela_login, labelMensagem)).pack(side=BOTTOM)

  tela_login.mainloop()


telaLogin()
