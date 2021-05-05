from tkinter import *
from tkinter import ttk
from operacoes_db import pegarPontos, atualizarPontos
from minigame import aumentarProgresso

def telaMinigame(usuario, labelProdutos):
  tela = Toplevel()
  tela.geometry("600x500")

  task = Label(tela, text="Ajude a Dona Creuza com as compras!", pady=50)
  task.pack()
  progresso = ttk.Progressbar(tela, orient=HORIZONTAL,length=200,mode='determinate')
  progresso.pack()
  labelPontos = Label(tela, text='')
  clickBotao = Button(tela, text='CLIQUE!', command=lambda:aumentarProgresso(progresso, labelPontos, labelProdutos, usuario))
  clickBotao.pack(anchor=CENTER)
  labelPontos.pack()

  tela.mainloop()


