import tkinter as tk
from tkinter import filedialog
from PIL import Image

import helper as h

window = tk.Tk()
window.title("Image Resizer")
window.resizable(width=False, height=False)
h.centerApp(window)

def fahrenheitToCelsius():
  fahrenheit = inputTemperature.get()
  celsius = (5/9) * (float(fahrenheit) - 32)
  labelResult["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

mainFrame = tk.Frame(master=window)
mainFrame.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

inputTemperature = tk.Entry(master=mainFrame, width=10)
labelTemperature = tk.Label(master=mainFrame, text="\N{DEGREE FAHRENHEIT}")
buttonConvert = tk.Button(master=mainFrame, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheitToCelsius)
labelResult = tk.Label(master=mainFrame, text="\N{DEGREE CELSIUS}")

inputTemperature.grid(row=0, column=0, padx=10, sticky="e")
labelTemperature.grid(row=0, column=1, padx=10, sticky="w")
buttonConvert.grid(row=0, column=2, padx=10)
labelResult.grid(row=0, column=3, padx=10)

# NEW CODE

def searchImage():
  imagePath = filedialog.askopenfilename(title = "Select file", filetypes = [('images', ('.png', '.jpg', '.jpeg'))])
  if imagePath:
    print('tes')
    imageBuffer = Image.open(imagePath)
    print(imageBuffer.format) # The file format of the source file. # Output: PNG / JPEG
    print(imageBuffer.size) # Image size, in pixels. The size is given as a 2-tuple (width, height).
  else:
    print('nol')

buttonImage = tk.Button(master=mainFrame, text="Search image", command=searchImage, width=36)
buttonImage.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

window.mainloop()
