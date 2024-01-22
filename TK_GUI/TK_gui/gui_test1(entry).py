import tkinter as tk
import random as r
root = tk.Tk()
root.title("my application")
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
print(h,w)
root.geometry(f"{w}x{h}+{0}+{0}")

def fun():
    input_t = e.get()
    print(input_t)
    e.delete(0,"end")

tk.Label(text="name",bg="purple",fg="white",font=("monaco",30)).pack(pady=20)
e = tk.Entry(font=("monaco",30),fg="purple")
e.pack(pady=20)
b2 = tk.Button(text="click me to print",font=("monaco",30),
               command=fun)
b2.pack(pady=20)
root.mainloop()