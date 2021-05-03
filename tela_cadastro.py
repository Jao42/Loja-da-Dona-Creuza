from tkinter import *
from tela_login import*
from cadastro import *
import config

def telaCadastro():
  tela_cadastro = Toplevel()
  tela_cadastro.configure(bg=config.COR_BG2)
  tela_cadastro.geometry('1366x768')
  tela_cadastro.title("Cadastro")

  email = StringVar()
  user = StringVar()
  senha = StringVar()

  # CRIANDO FRAME A ESQUERDA
  Left = Frame(tela_cadastro, width=650, height=900, bg=config.COR_BG3)
  Left.pack(side=LEFT)

  # CRIANDO FRAME A DIREITA
  Right = Frame(tela_cadastro, width=750, height=900, bg=config.COR_BG)
  Right.pack(side=RIGHT)

  # INSERINDO ELEMENTOS A FRAME DA ESQUERDA
  img = PhotoImage(file='./imgs/circulo-superior-preto.png')
  lblimg = Label(Left, image=img, bg=config.COR_BG3)
  lblimg.place(x=0, y=0)

  lbl1 = Label(Left, font='Arial 43 bold', bg=config.COR_BG3, fg='#ffffff', justify=LEFT,
               text='SEJA BEM-VINDO!\n')
  lbl1.place(x=60, y=280)

  lbl2 = Label(Left, font='Arial 15', bg=config.COR_BG3, fg=config.COR_BG2, justify=LEFT,
               text='FALTA POUCO PARA SE TORNAR NOSSO CLIENTE, FAÇA \nSEU CADASTRO PREENCHENDO'
                    ' OS DADOS AO LADO ;)')
  lbl2.place(x=60, y=380)

  # INSERINDO ELEMENTOS A FRAME DA DIREITA
  logo = PhotoImage(file='./imgs/logotipo.preto.png')
  lbllogo = Label(Right, image=logo, bg=config.COR_BG)
  lbllogo.place(x=200, y=80)

  img2 = PhotoImage(file='./imgs/onda.png')
  lblimg2 = Label(Right, image=img2, bg=config.COR_BG)
  lblimg2.place(x=15, y=355)

  label_email = Label(Right, text="DIGITE SEU E-MAIL: ", height="3", font='Arial 14 ', bg=config.COR_BG, fg=config.COR_BG3)
  label_user = Label(Right, text="DIGITE SEU USUÁRIO: ", height="3", font='Arial 14 ', bg=config.COR_BG, fg=config.COR_BG3)
  label_senha = Label(Right, text="DIGITE A SUA SENHA: ", height="3", font='Arial 14 ', bg=config.COR_BG, fg=config.COR_BG3)

  email_entrada = Entry(Right, textvariable=email, width="40")
  user_entrada = Entry(Right, textvariable=user, width="25")
  senha_entrada = Entry(Right, textvariable=senha, width="25", show="*")

  label_email.place(x=60, y=220)
  email_entrada.place(x=60, y=270, width=400, height=25)

  label_user.place(x=60, y=300)
  user_entrada.place(x=60, y=350, width=400, height=25)

  label_senha.place(x=60, y=380)
  senha_entrada.place(x=60, y=430, width=400, height=25)

  email_entrada.focus()

  label_mensagem = Label(Right)
  label_mensagem['bg'] = config.COR_BG
  label_mensagem.place(x=200, y=10)

  # INSERINDO BUTTONs NA FRAME DA DIREITA
  bnt1 = Button(Right,
    text='Cadastrar',
    font='Arial 13',
    bg=config.COR_BG2,
    height=2,
    width=20,
    command=lambda: cadastro(user, email, senha, label_mensagem))

  bnt1.place(x=160, y=480)

  # INSERINDO CHECKBUTTON NA FRAME DA DIREITA
  valor_check = IntVar()

  ja_cadastrado = Checkbutton(Right,
      text='Já sou cadastrado.',
      variable=valor_check,
      bg=config.COR_BG,
      fg=config.COR_BG3,
      font='Arial 12 bold',
      command=telaLogin
    ).place(x=165, y=535)

  tela_cadastro.mainloop()

