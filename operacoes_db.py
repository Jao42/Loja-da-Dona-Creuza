import sqlite3

def pegarPontos(email_usuario):
  conexao = sqlite3.connect('db-loja.db')
  cursor = conexao.cursor()
  cursor.execute(f"SELECT usuario, pontos FROM usuarios WHERE usuario = '{email_usuario}' OR email = '{email_usuario}'")
  usuario, pontos = cursor.fetchone()
  conexao.commit()
  conexao.close()
  return pontos



def atualizarPontos(usuario, novosPontos):
  conexao = sqlite3.connect("db-loja.db")
  cursor = conexao.cursor()
  cursor.execute(f"UPDATE usuarios SET pontos = {novosPontos} WHERE usuario = '{usuario}'")
  conexao.commit()
  conexao.close()
  return 0

