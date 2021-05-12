from produtos import addProdutoTable

def admin(nome, preco, quant, labelMensagem, entradas):
  addProdutoTable(nome, preco, quant, labelMensagem)
  for i in entradas:
    i.delete(0, 'end')


