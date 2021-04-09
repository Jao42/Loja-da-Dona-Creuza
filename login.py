import csv
from tkinter import *
import bcrypt
import sqlite3 
from tela_produtos import *

def verifLogin(email_usuario, senha, tela):
  email_usuario = email_usuario.get()
  senha = senha.get()

  conexao = sqlite3.connect('db-loja.db')
  cursor = conexao.cursor()

  cursor.execute(f"SELECT senha FROM usuarios WHERE email = '{email_usuario}' OR usuario = '{email_usuario}' ")
  hashSenha = cursor.fetchone()
  conexao.commit()
  conexao.close()
  if not hashSenha:
    mensagem = Label(tela, text='Usuário não cadastrado!', foreground='red')
    mensagem.pack()
    return 1
  confirmacaoSenha = bcrypt.checkpw(senha.encode(),  hashSenha[0].encode())
  if confirmacaoSenha:
    telaProdutos(tela)
    return 0
  
  mensagem = Label(tela, text='Senha incorreta!', foreground='red')
  mensagem.pack()
  return 1



