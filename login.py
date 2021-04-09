import csv
from tkinter import *
import bcrypt
from tela_produtos import *

def verifLogin(email_usuario, senha, tela):
  email_usuario = email_usuario.get()
  senha = senha.get()
  senha = senha.encode()

  with open('usuarios.csv', 'r') as usuariosCad:
    fieldnames = ['usuario', 'email', 'senha']
    reader = csv.DictReader(usuariosCad, fieldnames=fieldnames)

    if (not any((i['email'] == email_usuario or i['usuario'] == email_usuario)
        and bcrypt.checkpw(senha, i['senha'].encode())for i in reader)):
      mensagem = Label(tela, text='algum dado está incorreto, tente novamente!', foreground='red')
      mensagem.pack()
      return 1;

  telaProdutos(tela) 
  return 0
  


