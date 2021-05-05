from tela_login import telaLogin
from cadastro import cadastro


def botaoCadastro(tela_cadastro, labelMensagem, usuario, email, senha):
  retornoCadastro = cadastro(usuario, email, senha, labelMensagem)
  if retornoCadastro == 0:
    tela_cadastro.destroy()
    telaLogin()
    
def checkboxCadastro(tela_cadastro):
  tela_cadastro.destroy()
  telaLogin()

