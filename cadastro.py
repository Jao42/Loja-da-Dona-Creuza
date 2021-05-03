import csv
from tkinter import *
import sqlite3
import bcrypt
from mensagem import mensagemPadrao

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
  conexao.commit()

  if ((existencia) or
      (email.count('@') > 1) or
      (email.find('@') == 0) or
      (email.find('@') > email.rfind('.')) or
      (email.find('@') == (email.rfind('.') - 1)) or
      (email.rfind('.') == (len(email) - 1)) or
      (not all(i in email for i in emailChars))):

    conexao.close()
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


def verifUsuario(usuario, conexao):
  cursor = conexao.cursor()
  cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario = '{usuario}'")
  existencia = cursor.fetchone()
  conexao.commit()

  if (len(usuario) < 4 or
      existencia):
    conexao.close()
    return 1

  return 0


def verifCadastro(usuario, email, senha):
  conexao = sqlite3.connect('db-loja.db')

  if verifEmail(email, conexao):
    return 1

  if verifUsuario(usuario, conexao):
    return 2

  if verifSenha(senha):
    return 3

  conexao.close()
  return 0


def cadastro(usuario, email, senha, labelMensagem):

  usuario = usuario.get()
  email = email.get()
  senha = senha.get()

  if displayVerifCadastro(usuario, email, senha, labelMensagem) == 0:
    conexao = sqlite3.connect('db-loja.db')
    cursor = conexao.cursor()

    senhaHashed = hashSenha(senha)
    cursor.execute(f"INSERT INTO usuarios VALUES ('{usuario}', '{email}', '{senhaHashed}', 50)")
    conexao.commit()
    conexao.close()
    return 0

  return 1


def displayVerifCadastro(usuario, email, senha, label):
  retornoVerifCadastro = verifCadastro(usuario, email, senha)

  if retornoVerifCadastro == 1:
    label['text'] = 'Email Inválido ou já cadastrado!'
    label['foreground'] = 'red'
    return 1
  if retornoVerifCadastro == 2:
    label['text'] = 'Usuário Inválido(menos de 4 characteres) ou já cadastrado!' 
    label['foreground'] = 'red'
    return 2
  if retornoVerifCadastro == 3:
    label['text'] = 'Senha fraca! Informe uma senha com no mínimo 8 caracteres sendo eles:\nSimbolos, números e letras.' 
    label['foreground'] = 'red'
    return 3

  label['text'] = 'Usuário registrado com sucesso!'
  label['foreground'] = 'green'

  return 0

