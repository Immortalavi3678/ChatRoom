import tkinter as tk
import random as r
from PIL import Image,ImageTk

root = tk.Tk()
root.title("my application")
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
# print(h,w)
# root.geometry(f"{w}x{h}+{0}+{0}")

img = Image.open("image1.jpeg")
img = img.resize((500,499))
imgtk = ImageTk.PhotoImage(img)
l1 = tk.Label(bg="purple",image=imgtk)
l1.image=imgtk
l1.pack()

root.mainloop()