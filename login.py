import csv

def verifLogin(email, usuario, senha):

  with open('usuarios.csv', 'r') as usuariosCad:
    fieldnames = ['usuario', 'email', 'senha']
    reader = csv.DictReader(usuariosCad, fieldnames=fieldnames)
    if not any((i['usuario'] == usuario and i['email'] == email and i['senha'] == senha) for i in reader):
      print('algum dado está incorreto, tente novamente!')
      return 1;
  print('Bem vindo de volta!')
  return 0;
  


email = input('Digite seu email: ')
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

verifLogin(email, usuario, senha)
