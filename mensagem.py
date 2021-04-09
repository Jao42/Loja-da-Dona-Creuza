from tkinter import Label

def mensagemPadrao(text, cor, tela):
  mensagem = Label(tela, text=text, foreground=cor)
  return mensagem.pack()
