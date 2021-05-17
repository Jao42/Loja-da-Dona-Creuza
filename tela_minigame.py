from tkinter import *
from tkinter import ttk
import config
from operacoes_db import pegarPontos, atualizarPontos
from minigame import aumentarProgresso

def telaMinigame(usuario, labelProdutos):
  tela = Toplevel()
  tela.geometry("600x500")
  tela.title('Minigame')
  tela.configure(bg=config.COR_BG)

  tela.resizable(False, False)
  logo = PhotoImage(file='./imgs/logotipo.preto.png')
  lbllogo = Label(tela, image=logo, bg=config.COR_BG)
  lbllogo.place(x=140, y=10)
  img2 = PhotoImage(file='./imgs/onda2.png')
  lblimg2 = Label(tela, image=img2, bg=config.COR_BG)
  lblimg2.place(x=0, y=180)


  labelTask = Message(tela, text="Ajude a Dona Creuza a fazer as compras", font="Arial 14 bold", bg=config.COR_BG, width=220, justify=CENTER)
  labelTask.place(x=190, y=140)
  progresso = ttk.Progressbar(tela, orient=HORIZONTAL, length=200, mode='determinate')
  progresso.place(x=190, y=230)
  labelPontos = Label(tela, text='', bg=config.COR_BG)
  
  clickButton = Button(tela, text='CLIQUE!', command=lambda: aumentarProgresso(progresso, config.TASKS, labelPontos, labelProdutos, labelTask, usuario))

  clickButton.place(x=260, y=260)
  labelPontos.place(x=235, y=290)

  tela.mainloop()

