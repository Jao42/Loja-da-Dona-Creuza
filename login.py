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
  confirmacaoSenha = bcrypt.checkpw(senha.encode(),  hashSenha[0].encode())
  if hashSenha and confirmacaoSenha:
    telaProdutos(tela)
    return 0
  
  mensagem = Label(tela, text='algum dado está incorreto, tente novamente!', foreground='red')
  mensagem.pack()
  return 1



