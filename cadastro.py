import csv
from tkinter import *

def verifCadastro(entrada_usuario, entrada_email, entrada_senha, tela):
  usuario = entrada_usuario.get()
  email = entrada_email.get()
  senha = entrada_senha.get()
  mensagem = False

  emailChars = '@.'
  fieldnames = ['usuario', 'email', 'senha']

  with open('usuarios.csv', 'r', newline='') as usuariosCad:
    reader = csv.DictReader(usuariosCad, fieldnames=fieldnames)
    if not all(i in email for i in emailChars) or any(i['email'] == email for i in reader):
      mensagem = Label(tela,  text="Email Inválido ou já cadastrado!", fg="red", font=("calibri", 11))
      mensagem.pack()

      return 1

    elif (len(usuario) < 4) or any(i['usuario'] == usuario for i in reader):
      mensagem = Label(tela, text="Usuário Inválido(menos de 4 characteres) ou já cadastrado!", fg="red", font=("calibri", 11))
      mensagem.pack()
      return 2

    else (len(senha) < 8) or (senha.upper() == senha.lower()) or not any(str(i) in senha any(for i in range(10))):
      mensagem = Label(tela, text="Para sua segurança pedimos que sua senha tenha pelomenos:\n 8 characteres, uma letra MAIÚSCULA e uma minúscula.", fg="gray", font=("calibri", 11))
      mensagem.pack()
      return 3

  with open('usuarios.csv', 'a', newline='') as usuariosCad:
    writer = csv.DictWriter(usuariosCad, fieldnames=fieldnames)
    writer.writerow({'usuario': usuario, 'email': email, 'senha': senha})
  mensagem = Label(tela, text="Usuário registrado com sucesso!", fg="green", font=("calibri", 11))
  mensagem.pack()
  return 0
      

def unpackTkinter(x):
  if x:
    x.destroy()
