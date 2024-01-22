import tkinter as tk
import random as r
root = tk.Tk()
root.title("my application")
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
print(h,w)
root.geometry(f"{w}x{h}+{0}+{0}")
tk.Label(text="heading",bg="purple",fg="white",font=("monaco",30)).pack(fill="x")

def fun1():
    global f1,f2
    f1.pack_forget()
    f2.pack(expand=True)

def fun2():
    global f1,f2
    f2.pack_forget()
    f1.pack(expand=True)

f1 = tk.Frame(root,bg="red",height=300,width=300)
f1.pack(expand=True)

f2 = tk.Frame(root,bg="blue",height=300,width=300)

b1 = tk.Button(f1,text="goto f2",command=fun1)
b1.place(x=120,y=130)

b2 = tk.Button(f2,text="back to f1",command=fun2)
b2.place(x=105,y=130)


root.mainloop()