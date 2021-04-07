import csv
from tkinter import *
import sqlite3

def verifEmail(email, arq):
  emailChars = '@.'
  if (any(i['email'] == email for i in arq) or
      (email.count('@') > 1) or
      (email.find('@') == 0) or
      (email.find('@') > email.rfind('.')) or
      (email.find('@') == (email.rfind('.') - 1)) or
      (email.rfind('.') == (len(email) - 1)) or
      (not all(i in email for i in emailChars))):
    return 1
  return 0


def verifSenha(senha):
#no mínimo 8 caracteres incluindo letras, numeros e simbolos.

  num = [str(i) for i in range(10)]
  condNum = False
  condSimb = False

  if senha.upper() == senha.lower() or len(senha) < 8:
    return 1

  for i in senha:
    if i in num:
      condNum = True

    elif i.upper() == i.lower(): 
      condSimb = True

    if condNum and condSimb: 
      return 0

  return 1


def verifUsuario(usuario, arq):
  if (len(usuario) < 4 or
      any(i['usuario'] == usuario for i in arq)):
    return 1
  return 0


def verifCadastro(usuario, email, senha, tela):

  fieldnames = ['usuario', 'email', 'senha']

  usuario = usuario.get()
  email = email.get()
  senha = senha.get()

  with open('usuarios.csv', 'r', newline='') as usuariosCad:
    reader = csv.DictReader(usuariosCad, fieldnames=fieldnames)

    if verifEmail(email, reader):
      mensagem = Label(tela,  text="Email Inválido ou já cadastrado!", fg="red", font=("calibri", 11))
      mensagem.pack()
      return 1

    elif verifUsuario(usuario, reader):
      mensagem = Label(tela, text="Usuário Inválido(menos de 4 characteres) ou já cadastrado!", fg="red", font=("calibri", 11))
      mensagem.pack()
      return 2


    elif verifSenha(senha):
      mensagem = Label(tela, text="Senha fraca! Informe uma senha com no mínimo 8 caracteres sendo eles:\nSimbolos, números e letras.", fg="red", font=("calibri", 11))
      mensagem.pack()
      return 3

  with open('usuarios.csv', 'a', newline='') as usuariosCad:
    writer = csv.DictWriter(usuariosCad, fieldnames=fieldnames)
    writer.writerow({'usuario': usuario, 'email': email, 'senha': senha})
  mensagem = Label(tela, text="Usuário registrado com sucesso!", fg="green", font=("calibri", 11))
  mensagem.pack()
  return 0

