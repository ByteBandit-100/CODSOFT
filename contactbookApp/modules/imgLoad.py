# modules/imgLoad.py
from PIL import Image, ImageTk

def load_png(path, size=None, master=None):
    """
    Load a PNG image and optionally resize it.
    Ensures the image is bound to a Tkinter master window.
    """
    img = Image.open(path)
    if size:
        img = img.resize(size, Image.Resampling.LANCZOS)  # modern Pillow
    return ImageTk.PhotoImage(img, master=master)
