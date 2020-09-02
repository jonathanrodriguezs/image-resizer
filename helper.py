def centerApp(win):
  width = 300
  height = 300
  win.update_idletasks()
  padX = (win.winfo_screenwidth() // 2) - (width // 2)
  padY = (win.winfo_screenheight() // 2) - (height // 2)
  win.geometry('{}x{}+{}+{}'.format(width, height, padX, padY))
