import csv
from tkinter import *
import sqlite3
import bcrypt

def hashSenha(senha):

  salt = bcrypt.gensalt(10)
  senha = senha.encode('utf-8')
  senhaHash = bcrypt.hashpw(senha, salt)
  return str(senhaHash.decode())


def verifEmail(email, conexao):
  emailChars = '@.'
  cursor = conexao.cursor()
  cursor.execute(f"SELECT email FROM usuarios WHERE email = '{email}'")
  existencia = cursor.fetchone()
  
  if ((existencia) or
      (email.count('@') > 1) or
      (email.find('@') == 0) or
      (email.find('@') > email.rfind('.')) or
      (email.find('@') == (email.rfind('.') - 1)) or
      (email.rfind('.') == (len(email) - 1)) or
      (not all(i in email for i in emailChars))):

    conexao.close()
    return 1

  conexao.commit()
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


def verifUsuario(usuario, conexao):
  cursor = conexao.cursor()
  cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario = '{usuario}'")
  existencia = cursor.fetchone()

  if (len(usuario) < 4 or
      existencia):
    conexao.close()
    return 1

  conexao.commit()
  return 0




def verifCadastro(usuario, email, senha, tela):

  conexao = sqlite3.connect('db-loja.db')
  cursor = conexao.cursor()

  fieldnames = ['usuario', 'email', 'senha']

  usuario = usuario.get()
  email = email.get()
  senha = senha.get()


  if verifEmail(email, conexao):
    mensagem = Label(tela,  text="Email Inválido ou já cadastrado!", fg="red", font=("calibri", 11))
    mensagem.pack()
    return 1

  elif verifUsuario(usuario, conexao):
    mensagem = Label(tela, text="Usuário Inválido(menos de 4 characteres) ou já cadastrado!", fg="red", font=("calibri", 11))
    mensagem.pack()
    return 2


  elif verifSenha(senha):
    mensagem = Label(tela, text="Senha fraca! Informe uma senha com no mínimo 8 caracteres sendo eles:\nSimbolos, números e letras.", fg="red", font=("calibri", 11))
    mensagem.pack()
    return 3

  senhaHashed = hashSenha(senha)

  cursor.execute(f"INSERT INTO usuarios VALUES ('{usuario}', '{email}', '{senhaHashed}')")
  conexao.commit()
  conexao.close()

  mensagem = Label(tela, text="Usuário registrado com sucesso!", fg="green", font=("calibri", 11))
  mensagem.pack()
  return 0


if __name__ == '__main__':
  senha = 'testesenha123'
  conexao = sqlite3.connect('db-loja.db')

  #c = conexao.cursor()

  #usuarios = [('tadeu', 'tadeuo@email.com', senhaHashed)]
  #c.executemany("INSERT INTO usuarios VALUES (?, ?, ?)", usuarios)
  #c.execute("SELECT senha FROM usuarios WHERE usuario = 'taideu'")
  #print(c.fetchone())

  #conexao.commit()
  #conexao.close()


  

