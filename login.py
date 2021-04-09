import csv
from tkinter import *
import bcrypt
import sqlite3 
from tela_produtos import *
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


def displayVerifLogin(email_usuario, senha, tela):
  verifRetorno = verifLogin(email_usuario, senha)

  if verifRetorno == 1:
    mensagemPadrao('Usuário não cadastrado!', 'red', tela)
    return 1
  if verifRetorno == 2:
    mensagemPadrao('Senha incorreta!', 'red', tela)
    return 2
  mensagemPadrao('Logado com sucesso!', 'green', tela)
  telaProdutos(tela)
  return 0

