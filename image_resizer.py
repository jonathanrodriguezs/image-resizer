import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image


def resize_image(path, new_path, width, height, crop_center=True):
    '''Image resizing and saving to new path'''
    original_image = Image.open(path)
    image = original_image if not crop_center else crop_center_image(
        path, original_image.size[1], original_image.size[1])
    new_image = image.resize((width, height))
    new_image.save("{}_{}_.{}".format(
        new_path, str(width), original_image.format))


def crop_center_image(path, new_width, new_height):
    '''Crop the center of the image'''
    image = Image.open(path)
    width, height = image.size  # Get dimensions

    left = (width - new_width) / 2
    top = (height - new_height) / 2
    right = (width + new_width) / 2
    bottom = (height + new_height) / 2

    image = image.crop((left, top, right, bottom))

    return image


def generate_icons(image, sizes=(32, 57, 76, 96, 128, 228)):
    for size in sizes:
        resize_image(image, "icons/icon", size, size)


def image_sizer():
    window = tk.Tk()
    window.title("Icon Generator")
    window.resizable(width=False, height=False)
    window.geometry("300x300")

    style = ttk.Style(window)
    style.theme_use("clam")

    def open_file_natively():
        files = filedialog.askopenfilenames(
            parent=window, filetypes=[("All files", "*")])
        try:
            image = files[0]
            generate_icons(image)
            # load = Image.open(image).resize((100, 100))
            # render = ImageTk.PhotoImage(load)
            # img = tk.Label(window, image=render)
            # img.image = render
            # img.place(x=0, y=0)

        except IndexError:
            print("No file selected")

    tk.Button(window, text="Select image",
              command=open_file_natively).pack(fill='x')

    window.mainloop()


if __name__ == '__main__':
    image_sizer()
