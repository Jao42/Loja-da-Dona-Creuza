from operacoes_db import atualizarPontos, pegarPontos

def aumentarProgresso(progresso, labelPontos, labelProdutos, usuario):
  progresso['value'] += 20
  if progresso['value'] == 100:
    
    pontos = pegarPontos(usuario)
    pontos += 50
    atualizarPontos(usuario, pontos)
    labelProdutos['text'] = f'{usuario} --> {pontos}'

    progresso['value'] = 0
    labelPontos['text'] = '+50 CreuzaPoints!'

  if progresso['value'] == 20:
    labelPontos['text'] = ''

  return 0


