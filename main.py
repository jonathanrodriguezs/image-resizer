import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_resizer import generate_icons, crop_center_image


def open_file_natively():
    files = filedialog.askopenfilenames(
        parent=window, filetypes=[('images', ('.png', '.jpg', '.jpeg'))])
    try:
        image = files[0]
        generate_icons(image, (120, 144, 152, 167, 180, 192, 512))
        image_pil = Image.open(image)
        loaded_img = crop_center_image(image_pil).resize((150, 150))
        render = ImageTk.PhotoImage(loaded_img)
        img_preview = tk.Label(window, image=render)
        img_preview.image = render
        img_preview.place(x=75, y=75)

    except IndexError:
        print("No file selected")


window = tk.Tk()
window.title("Icon Generator")
window.resizable(width=False, height=False)
window.geometry("300x300")

style = ttk.Style(window)
style.theme_use("alt")


tk.Button(window, text="Select image",
          command=open_file_natively).pack(fill='x')

window.mainloop()
