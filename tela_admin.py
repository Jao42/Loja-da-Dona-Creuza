from centralizar_tela import *
from tkinter import *
from produtos import addProdutoTable
import config

def telaAdmin(tela_login):
  telaADM = Toplevel(tela_login)
  telaADM.configure(bg=config.COR_BG)
  centralizarTela(telaADM, 600, 500)

  nomeProduto = StringVar()
  precoProduto = StringVar()
  nomeImg = StringVar()
  quantProduto = StringVar()

  telaADM.title('ADMIN')
  Label(telaADM, text='Registro de Produtos', bg=config.COR_BG).pack(anchor=W, pady=20)

  labelNome = Label(telaADM, text="Nome do produto:", bg=config.COR_BG)
  labelPreco = Label(telaADM, text="Preço do produto:", bg=config.COR_BG)
  labelQuantidade= Label(telaADM, text="Quantidade:", bg=config.COR_BG)
  entryNome = Entry(telaADM, textvariable=nomeProduto)
  entryPreco = Entry(telaADM, textvariable=precoProduto)
  entryQuantidade = Entry(telaADM, textvariable=quantProduto)

  labelNome.pack(anchor=W)
  entryNome.pack(anchor=W)
  labelPreco.pack(anchor=W)
  entryPreco.pack(anchor=W)
  labelQuantidade.pack(anchor=W)
  entryQuantidade.pack(anchor=W)


  labelMensagem = Label(telaADM, bg=config.COR_BG)
  labelMensagem.pack()
  Button(telaADM, text="ADICIONAR PRODUTO", command=lambda:addProdutoTable(nomeProduto.get(), int(precoProduto.get()), int(quantProduto.get()), labelMensagem)).pack(pady=50)

  telaADM.mainloop()

if __name__ == "__main__":
  telaAdmin()
