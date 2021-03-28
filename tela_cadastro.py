from tkinter import *
from cadastro import *

def tela_cadastro(main):
  tela_cadastro = Toplevel(main)
  tela_cadastro.geometry("600x500")
  tela_cadastro.title("Registro")

  email = StringVar()
  user = StringVar()
  senha = StringVar()

  label_email = Label(tela_cadastro, text="Digite o seu email: ", height="3")
  label_user = Label(tela_cadastro, text="Digite o seu usuario: ", height="3")
  label_senha = Label(tela_cadastro, text="Digite a sua senha: ", height="3")

  email_entrada = Entry(tela_cadastro, textvariable=email, width="40")
  user_entrada = Entry(tela_cadastro, textvariable=user, width="25")
  senha_entrada = Entry(tela_cadastro, textvariable=senha, width="25", show="*")

  label_email.pack()
  email_entrada.pack()
  label_user.pack()
  user_entrada.pack() 
  label_senha.pack()
  senha_entrada.pack()


  Button(tela_cadastro, text="Entrar", height="2", width="30", command=lambda: verifCadastro(user_entrada, email_entrada, senha_entrada, tela_cadastro)).pack(side=BOTTOM)



