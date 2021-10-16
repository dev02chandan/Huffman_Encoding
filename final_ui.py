from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter import filedialog as fd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("648x394")
window.configure(bg = "#F0F0F0")


canvas = Canvas(
    window,
    bg = "#F0F0F0",
    height = 394,
    width = 648,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    104.0,
    146.0,
    anchor="nw",
    text="Select File to Compress (.txt) :",
    fill="#000000",
    font=("Roboto", 17 * -1)
)

canvas.create_text(
    104.0,
    223.0,
    anchor="nw",
    text="Select File to Decompress(.bin) :",
    fill="#000000",
    font=("Roboto", 17 * -1)
)

def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file_path_txt = fd.askopenfilename(filetypes=filetypes)
    print(file_path_txt)


    
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_text_file,
    relief="flat"
)
button_1.place(
    x=380.0,
    y=136.0,
    width=164.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_text_file,
    relief="flat"
)
button_2.place(
    x=380.0,
    y=213.0,
    width=164.0,
    height=44.0
)

window.resizable(False, False)
window.mainloop()