from os import startfile
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from image_resizer import generate_icons, crop_center_image


def open_file_browser():
    files = filedialog.askopenfilenames(
        parent=window, filetypes=[('images', ('.png', '.jpg', '.jpeg'))])
    try:
        image = files[0]
        print(f"User selected image: {image}")
        image_pil = Image.open(image)
        loaded_img = crop_center_image(image_pil).resize((150, 150))
        render = ImageTk.PhotoImage(loaded_img)
        img_preview = tk.Label(window, image=render)
        img_preview.image = render
        img_preview.place(x=75, y=75)

        tk.Button(window, text="Save pack of icons generated",
                  command=lambda: save_icons_pack(image)).pack(fill='x')
    except IndexError:
        print("No file selected")


def save_icons_pack(image, ):
    directory = filedialog.askdirectory()
    if directory:
        print(f"User selected directory: {directory}")
        # suggested sizes: (120, 144, 152, 167, 180, 192, 512)
        generate_icons(image, directory)
        messagebox.showinfo(
            message="Icons were saved into " + directory, title="Success")
        startfile(directory)
    else:
        messagebox.showwarning(
            message="Please select a directory", title="Advice")


window = tk.Tk()
window.title("Icon Generator")
window.resizable(width=False, height=False)
window.geometry("300x300")

style = ttk.Style(window)
style.theme_use("clam")

tk.Button(window, text="Select image",
          command=open_file_browser).pack(fill='x')

window.mainloop()
