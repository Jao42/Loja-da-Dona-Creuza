from tkinter import *
from tkinter import ttk


def telaProdutos(tela_login):

  tela = Toplevel(tela_login)

  screenWidth = tela.winfo_screenwidth()
  screenHeight = tela.winfo_screenheight()

  width = 600
  height = 500

  x = int((screenWidth/2) - (width/2))
  y = int((screenHeight/2) - (height/2))

  tela.geometry(f'{width}x{height}+{x}+{y}')
  tela.title('Estoque')

  #relief --> estilo da borda

  body = Frame(tela, borderwidth=2, relief='solid') 

  tabelaItems=['nome', 'preço']

#selectmode -> quantos items seleciona com mouse
#treeView heigth -> quantas rows
  scrollbarY = Scrollbar(body, orient=VERTICAL)
  scrollbarX = Scrollbar(body, orient=HORIZONTAL)

  tree = ttk.Treeview(
      body, columns=(tabelaItems[0], tabelaItems[1]), selectmode="extended", height=5,
      yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set
      )

  scrollbarY.config(command=tree.yview)
  scrollbarX.config(command=tree.xview)
  scrollbarY.pack(side=RIGHT, fill=Y)
  scrollbarX.pack(side=BOTTOM, fill=X)

  style = ttk.Style(body)
  style.configure('Treeview', rowheight=60)

  tree.heading(tabelaItems[0], text='produto')
  tree.heading(tabelaItems[1], text='preço')


#tabela
  tree.column('#0', minwidth=0, width=100)
  tree.column('#1', anchor="center", minwidth=0, width=200)
  tree.column('#2', anchor="center", minwidth=0, width=200)
  
  imagem = PhotoImage(file="./imgs/uno.png")

  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '20', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '21', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '22', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '23', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '24', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '25', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '26', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '27', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '28', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '29', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '30', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '31', '1'))
  tree.insert('', 'end', image=imagem, values=('Uno duas portas seminovo', '32', '1'))
  body.pack()
  tree.pack(side=BOTTOM)

  tela.mainloop()

if __name__ == '__main__':
  telaProdutos()
