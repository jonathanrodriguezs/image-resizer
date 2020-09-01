import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Frame): # pylint: disable=too-many-ancestors
  '''
  The Window class extens from the Frame one of tkinter
  '''
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.master = master
    self.pack(fill=tk.BOTH, expand=1)

    load = Image.open("sir.jpeg")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)


# Image resizing and saving to new path
def resize_image(path, new_path, width, height):
  image = Image.open(path)
  new_image = image.resize((width, height))
  new_image.save("{}_{}_.{}".format(new_path, str(width), image.format))

original_sizes = (32, 57, 76, 96, 128, 228)

def generate_icons(sizes = original_sizes):
  for size in sizes:
    resize_image("sir.jpeg", "generated/sir_resized", size, size)

if __name__ == '__main__':
  window = tk.Tk()
  window.title("Image Editor")
  window.resizable(width=False, height=False)

  app = Window(window)
  window.wm_title("Image Editor")
  window.geometry("300x300")
  window.mainloop()
