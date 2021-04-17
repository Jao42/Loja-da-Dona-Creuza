from tkinter import *
from cadastro import *
from centralizar_tela import *
import config



def telaCadastro(tela_inicial):
  tela_cadastro = Toplevel(tela_inicial)
  tela_cadastro.configure(bg=config.COR_BG)

  centralizarTela(tela_cadastro, 600, 500)

  tela_cadastro.title("Registro")

  email = StringVar()
  user = StringVar()
  senha = StringVar()

  label_email = Label(tela_cadastro, text="Digite o seu email: ", height="2", font='Arial 12', bg=config.COR_BG)
  label_user = Label(tela_cadastro, text="Digite o seu usuario: ", height="2", font='Arial 12', bg=config.COR_BG)
  label_senha = Label(tela_cadastro, text="Digite a sua senha: ", height="2", font='Arial 12', bg=config.COR_BG)

  email_entrada = Entry(tela_cadastro, textvariable=email, width="40")
  user_entrada = Entry(tela_cadastro, textvariable=user, width="25")
  senha_entrada = Entry(tela_cadastro, textvariable=senha, width="25", show="*")

  label_email.place(x=30, y=30)
  email_entrada.place(x=30, y=60)
  
  label_user.place(x=30, y=90)
  user_entrada.place(x=30, y=120)

  label_senha.place(x=30, y=150)
  senha_entrada.place(x=30, y=180)

  label_mensagem = Label(tela_cadastro)
  label_mensagem['bg'] = config.COR_BG
  label_mensagem.pack()

  Button(tela_cadastro,
      text="Registrar",
      height="2",
      width="30",
      command=lambda: cadastro(user, email, senha, tela_cadastro, label_mensagem)).pack(side=BOTTOM)
  tela_cadastro.mainloop()


