from tkinter import *
from login import *
import config

def telaLogin():
  tela_login = Toplevel()
  tela_login.configure(bg=config.COR_BG2)
  tela_login.title("Login")
  tela_login.geometry('1366x768')
  tela_login.resizable(False, False)

  # CRIANDO FRAME DA ESQUERDA
  Left = Frame(tela_login, width=650, height=900, bg=config.COR_BG3)
  Left.pack(side=LEFT)

  # CRIANDO FRAME A DIREITA
  Right = Frame(tela_login, width=750, height=900, bg=config.COR_BG)
  Right.pack(side=RIGHT)

  # INSERINDO ELEMENTOS NA FRAME DA ESQUERDA
  img = PhotoImage(file='./imgs/circulo-superior-preto.png')
  lblimg = Label(Left, image=img, bg=config.COR_BG3)
  lblimg.place(x=0, y=0)

  lbl1 = Label(Left, font='Arial 28 bold', bg=config.COR_BG3, fg=config.COR_BG2, justify=LEFT,
               text='É ÓTIMO TER VOCÊ AQUI\nMAIS UMA VEZ!')
  lbl1.place(x=60, y=280)

  lbl2 = Label(Left, font='Arial 13', bg=config.COR_BG3, fg=config.COR_BG2, justify=LEFT,
               text='FAÇA SEU LOGIN PARA FAZER SUA NOVA COMPRA.')
  lbl2.place(x=60, y=380)

  # INSERINDO ELEMENTOS NA FRAME DA DIREITA
  logo = PhotoImage(file='./imgs/logotipo.preto.png')
  lbllogo = Label(Right, image=logo, bg=config.COR_BG)
  lbllogo.place(x=200, y=80)

  img2 = PhotoImage(file='./imgs/onda.png')
  lblimg2 = Label(Right, image=img2, bg=config.COR_BG)
  lblimg2.place(x=15, y=355)

  email_usuario = StringVar()
  senha = StringVar()

  label_email_usuario = Label(Right, text='DIGITE O SEU E-MAIL OU USUÁRIO:', font='Arial 14', bg=config.COR_BG, fg=config.COR_BG3)
  label_senha = Label(Right, text='DIGITE SUA SENHA:', font='Arial 14', bg=config.COR_BG, fg=config.COR_BG3)
  email_usuario_entrada = Entry(Right, textvariable=email_usuario)
  senha_entrada = Entry(Right, textvariable=senha, show="*")
  email_usuario_entrada.focus()

  label_email_usuario.place(x=60, y=285)
  email_usuario_entrada.place(x=60, y=315, width=400, height=25)

  label_senha.place(x=60, y=360)
  senha_entrada.place(x=60, y=390, width=400, height=25)

  labelMensagem = Label(Right, bg=config.COR_BG)
  labelMensagem['bg'] = config.COR_BG
  labelMensagem.place(x=200, y=10)

  bttn = Button(Right,
                text='Login',
                font='Arial 13',
                bg=config.COR_BG2,
                height=2,
                width=20,
                command=lambda: displayVerifLogin(email_usuario, senha, tela_login, labelMensagem))
  bttn.place(x=160, y=480)
  tela_login.mainloop()


