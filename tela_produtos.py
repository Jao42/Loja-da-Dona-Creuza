from tkinter import *
from tkinter import ttk

def telaProdutos():
  tela = Tk()

  screenWidth = tela.winfo_screenwidth()
  screenHeight = tela.winfo_screenheight()

  width = 600
  height = 500

  x = int((screenWidth/2) - (width/2))
  y = int((screenHeight/2) - (height/2))

  tela.geometry(f'{width}x{height}+{x}+{y}')
  tela.title('Loja da Dona Creuza')

  #relief --> estilo da borda

  frameTitulo = Frame(tela, borderwidth=2, width=400, height=2) 
  titulo = Label(frameTitulo, text='PRODUTOS')

  frameTitulo.pack(side=TOP)
  titulo.pack()

  body = Frame(tela, borderwidth=2, relief='solid') 

  tabelaItems=['nome', 'preço', 'quantidade']

#selectmode -> quantos items seleciona com mouse


#treeView heigth -> quantas rows
  tree = ttk.Treeview(body, columns=(tabelaItems[0], tabelaItems[1], tabelaItems[2]), selectmode="extended")

  tree.heading(tabelaItems[0], text='produto')
  tree.heading(tabelaItems[1], text='preço')
  tree.heading(tabelaItems[2], text='quantidade')

#inicializacao da tabela(exotico, neh?).
  tree.column('#0', stretch=NO, minwidth=0, width=0)

#tabela
  tree.column('#1', stretch=1, minwidth=0, width=200)
  tree.column('#2', stretch=1, minwidth=0, width=200)
  tree.column('#3', stretch=1, minwidth=0, width=200)
  
  imagem = PhotoImage(file="./imgs/dona-creuza-peq.png")

  tree.insert('', 'end', text='fdd', open=True, image=imagem, values=('Uno duas portas', '20', '1'))
  body.pack()
  tree.pack(side=BOTTOM)

  tela.mainloop()

if __name__ == '__main__':
  telaProdutos()
