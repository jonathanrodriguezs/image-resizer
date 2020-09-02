import tkinter as tk
from PIL import Image

image = Image.open('unsplash_01.jpg')

# The file format of the source file.
print(image.format)  # Output: JPEG

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size)  # Output: (1200, 776)

window = tk.Tk()
window.title("Image Editor")
window.resizable(width=False, height=False)


def center(win):
    width = 400
    height = 400
    win.update_idletasks()
    x_pad = (win.winfo_screenwidth() // 2) - (width // 2)
    y_pad = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x_pad, y_pad))


center(window)


def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Create the Fahrenheit entry frame with an Entry widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
# Layout the temperature Entry and Label in frm_entry using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
btn_convert = tk.Button(  # Create the conversion Button and result display Label
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
