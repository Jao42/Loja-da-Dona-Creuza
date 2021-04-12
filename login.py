import csv
from tkinter import *
import bcrypt
import sqlite3 
from tela_produtos import *
from tela_admin import telaAdmin
from mensagem import mensagemPadrao


def verifLogin(email_usuario, senha):
  email_usuario = email_usuario.get()
  senha = senha.get()

  conexao = sqlite3.connect('db-loja.db')
  cursor = conexao.cursor()

  cursor.execute(f"SELECT senha FROM usuarios WHERE email = '{email_usuario}' OR usuario = '{email_usuario}' ")
  hashSenha = cursor.fetchone()
  conexao.commit()
  conexao.close()
  
  if not hashSenha:
    return 1

  confirmacaoSenha = bcrypt.checkpw(senha.encode(),  hashSenha[0].encode())

  if confirmacaoSenha:
    return 0
  
  return 2


def displayVerifLogin(email_usuario, senha, tela, label):
  verifRetorno = verifLogin(email_usuario, senha)

  if verifRetorno == 1:
    label['foreground'] = 'red'
    label['text'] = 'Usuário não cadastrado!'
    return 1
  if verifRetorno == 2:
    label['foreground'] = 'red'
    label['text'] = 'Senha Incorreta!'
    return 2
  label['foreground'] = 'green'
  label['text'] = 'Logado com sucesso!'
  if email_usuario.get() != 'admin' and email_usuario.get() != 'admin@admin.com':
    telaProdutos(tela)
  else:
    telaAdmin(tela)
  return 0

