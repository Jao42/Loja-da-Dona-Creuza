from operacoes_db import atualizarPontos, pegarPontos
from random import randint
import config

def aumentarProgresso(progresso, tasks, labelPontos, labelProdutos, labelTask, usuario):
  progresso['value'] += 20

  if progresso['value'] == 20:
    labelPontos['text'] = ''
    return 0

  if progresso['value'] == 100:
    pontos = pegarPontos(usuario)
    pontos += 50
    atualizarPontos(usuario, pontos)
    indexTask = randint(0, 4)
    labelTask['text'] = f'Ajude a Dona Creuza a {config.TASKS[indexTask]}'
    labelProdutos['text'] = f'{usuario} --> {pontos}'
    progresso['value'] = 0
    labelPontos['text'] = '+50 CreuzaPoints!'
  return 0



