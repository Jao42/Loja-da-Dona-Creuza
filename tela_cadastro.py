from tkinter import *
from cadastro import *
from centralizar_tela import *
import config



def tela_cadastro(main):
  tela_cadastro = Toplevel(main)
  tela_cadastro.configure(bg=config.COR_BG)

  centralizarTela(tela_cadastro, 600, 500)

  tela_cadastro.title("Registro")

  email = StringVar()
  user = StringVar()
  senha = StringVar()

  label_email = Label(tela_cadastro, text="Digite o seu email: ", height="3", bg=config.COR_BG)
  label_user = Label(tela_cadastro, text="Digite o seu usuario: ", height="3", bg=config.COR_BG)
  label_senha = Label(tela_cadastro, text="Digite a sua senha: ", height="3", bg=config.COR_BG)

  email_entrada = Entry(tela_cadastro, textvariable=email, width="40")
  user_entrada = Entry(tela_cadastro, textvariable=user, width="25")
  senha_entrada = Entry(tela_cadastro, textvariable=senha, width="25", show="*")

  label_email.pack()
  email_entrada.pack()
  label_user.pack()
  user_entrada.pack() 
  label_senha.pack()
  senha_entrada.pack()

  label_mensagem = Label(tela_cadastro)
  label_mensagem['bg'] = config.COR_BG
  label_mensagem.pack()

  Button(tela_cadastro,
      text="Registrar",
      height="2",
      width="30",
      command=lambda: cadastro(user, email, senha, tela_cadastro, label_mensagem)).pack(side=BOTTOM)


