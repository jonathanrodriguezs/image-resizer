import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def resize_image(path, new_path, width, height, crop_center=True):
    '''Image resizing and saving to new path'''
    original_image = Image.open(path)
    image = original_image if not crop_center else crop_center_image(
        original_image)
    new_image = image.resize((width, height))
    new_image.save("{}-{}.{}".format(new_path, str(width), 'png'))


def crop_center_image(image, new_width=None, new_height=None):
    '''Crop the center of an image'''
    width, height = image.size  # Get dimensions

    if (new_width is None or new_height is None):
        new_width, new_height = height, height

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
    style.theme_use("alt")

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

    tk.Button(window, text="Select image",
              command=open_file_natively).pack(fill='x')

    window.mainloop()


if __name__ == '__main__':
    image_sizer()
