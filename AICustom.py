from PIL import Image
from tkinter import filedialog as fd

def open(v="8", file="file.png", mode=Image.BOX, open="false"):
    c = Image.open(file)
    d = c.resize((c.width * v, c.height * v), resample=mode)
    filename = fd.asksaveasfilename(title='Save a file', defaultextension=".png", filetypes=(("Image File", "*.png"),("All Files", "*.*") ))
    d.save(filename)
    d.show()