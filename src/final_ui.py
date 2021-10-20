from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter import filedialog as fd
from huffman_coding import huff as huffman
import os
 


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("648x394")
window.configure(bg = "#F0F0F0")

def compress():
 
    file_path_txt = fd.askopenfilename(filetypes= [('text files', '*.txt')])
    file_name=os.path.basename(file_path_txt)
    text=huffman.read_file(file_path_txt)
    # print(text)
    Binary, Table = huffman.Huffman(text)
    huffman.make_output(file_name,Binary,Table)
def decompress():
    file_path_bin = fd.askopenfilename(filetypes= [('bin files', '*.bin')])
    file_path_pkl = fd.askopenfilename(filetypes= [('Pickle files', '*.pkl*')])
    decoded_text = huffman.decompress(file_path_bin,file_path_pkl)
    with open('output'+"/"+"_"+"decoded.txt", 'w') as output:
            output.write(decoded_text)
    print("decoded_text generated")
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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=compress,
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
    command=decompress,
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
