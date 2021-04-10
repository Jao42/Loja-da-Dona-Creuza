def centralizarTela(tela, width, height):

  screenWidth = tela.winfo_screenwidth()
  screenHeight = tela.winfo_screenheight()

  x = int((screenWidth/2) - (width/2))
  y = int((screenHeight/2) - (height/2))

  tela.geometry(f'{width}x{height}+{x}+{y}')

  return 0
