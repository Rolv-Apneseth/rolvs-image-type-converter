import glob
import os
import tkinter as tk
from tkinter import ttk

from PIL import Image


# Define Convert Function
def convert(type1, type2):
    console1["bg"] = "black"
    console2["bg"] = "black"

    console1["fg"] = "white"
    console2["fg"] = "white"

    console1["text"] = f"Converting .{type1[0]}\nfiles to .{type2[0]} files..."
    console2["text"] = f"Converting .{type1[0]}\nfiles to .{type2[0]} files..."

    for file in glob.iglob(f"Images/*.{str(type1[0])}"):
        img = Image.open(file)
        rgb_img = img.convert("RGB")
        file = file.replace("Images", "")
        print(f"Converted_Images/{file.replace(type1[0], type2[0])}")
        rgb_img.save(f"Converted_Images/{file.replace(type1[0], type2[0])}", quality=95)

    console1["bg"] = "gray"
    console2["bg"] = "gray"

    console1["fg"] = "black"
    console2["fg"] = "black"

    console1["text"] = f"Finished converting\n.{type1[0]} files\nto .{type2[0]} files"
    console2["text"] = f"Finished converting\n.{type1[0]} files\nto .{type2[0]} files"


# Variables (default values for conversion i.e. jpg to png)
type1 = ["jpg"]
type2 = ["png"]


# Button Functions
def set_type1(type1, x):
    type1[0] = x
    console1["text"] = f"File type to\nbe converted\nset to: .{type1[0]}"


def set_type2(type2, x):
    type2[0] = x
    console2["text"] = f"File type to\nconvert into\n set to: .{type2[0]}"


# UI ---------------------------------------------------------------------
root = tk.Tk()

# Set icon and title for window
FOLDER = os.path.dirname(os.path.abspath(__file__))
icon = tk.PhotoImage(os.path.join(FOLDER, "assets", "icon.ico"))
root.tk.call("wm", "iconphoto", root._w, icon)
root.title("Simple Image Converter")

# define canvas
height = 400
width = 500
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

# define background(label)
background = tk.Label(root, bg="black")
background.place(relheight=1, relwidth=1)

# Define frames
frame1 = tk.Frame(root, bd=5)
frame2 = tk.Frame(root, bd=5)
frame3 = tk.Frame(root, bd=5)

frame1.place(relwidth=0.425, relheight=0.6, relx=0.025, rely=0.025)
frame2.place(relwidth=0.425, relheight=0.6, relx=0.55, rely=0.025)
frame3.place(relwidth=0.95, relheight=0.325, relx=0.025, rely=0.65)

# Make Type Button labels
flabel = tk.Label(
    frame1, text="File type to\nconvert from:", font=("Courier", 10), bg="gray"
)
tlabel = tk.Label(
    frame2, text="File type to\nconvert to:", font=("Courier", 10), bg="gray"
)
# #Place Type Button Labels
flabel.place(relwidth=0.925, relheight=0.2, relx=0.025, rely=0.025)
tlabel.place(relwidth=0.925, relheight=0.2, relx=0.025, rely=0.025)

# Make type Buttons
fjpg = ttk.Button(frame1, command=lambda: set_type1(type1, "jpg"), text=".jpg")
fpng = ttk.Button(frame1, command=lambda: set_type1(type1, "png"), text=".png")


tjpg = ttk.Button(frame2, command=lambda: set_type2(type2, "jpg"), text=".jpg")
tpng = ttk.Button(frame2, command=lambda: set_type2(type2, "png"), text=".png")
tpdf = ttk.Button(frame2, command=lambda: set_type2(type2, "pdf"), text=".pdf")


# Place type buttons
fjpg.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.3)
fpng.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.6)


tjpg.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.3)
tpng.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.5)
tpdf.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.7)

# Define Convert Button
convert_button = ttk.Button(
    frame3, command=lambda: convert(type1, type2), text="Convert"
)
convert_button.place(relwidth=0.4, relheight=0.8, relx=0.3, rely=0.1)

# Define Console1
console1 = tk.Label(
    frame3,
    bg="gray",
    font=("Courier", 9),
    text="File type to\nbe converted\nset to: .jpg",
)
console1.place(relheight=0.8, relwidth=0.3, relx=0, rely=0.1)

# Define Console2
console2 = tk.Label(
    frame3,
    bg="gray",
    font=("Courier", 9),
    text="File type to\nconvert into\n set to: .png",
)
console2.place(relheight=0.8, relwidth=0.3, relx=0.7, rely=0.1)

root.mainloop()
