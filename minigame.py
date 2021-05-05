from operacoes_db import atualizarPontos, pegarPontos

def aumentarProgresso(progresso, labelPontos, labelProdutos, usuario):
  progresso['value'] += 1
  if progresso['value'] == 100:
    
    pontos = pegarPontos(usuario)
    pontos += 250
    atualizarPontos(usuario, pontos)
    labelProdutos['text'] = f'{usuario} --> {pontos}'

    progresso['value'] = 0
    labelPontos['text'] = '+250 CreuzaPoints!'

  if progresso['value'] == 1:
    labelPontos['text'] = ''

  return 0


