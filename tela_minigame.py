from tkinter import *
from tkinter import ttk
from operacoes_db import pegarPontos, atualizarPontos
from minigame import aumentarProgresso

def telaMinigame(usuario, labelProdutos):
  tela = Toplevel()
  tela.geometry("800x600")

  voltar = Button(text='<--')
  voltar.pack(anchor=NW)

  progresso = ttk.Progressbar(tela, orient=HORIZONTAL,length=200,mode='determinate')
  progresso.pack()
  labelPontos = Label(tela, text='')
  clickBotao = Button(tela, text='CLIQUE!', command=lambda:aumentarProgresso(progresso, labelPontos, labelProdutos, usuario))
  clickBotao.pack(anchor=CENTER)
  labelPontos.pack()

  tela.mainloop()


