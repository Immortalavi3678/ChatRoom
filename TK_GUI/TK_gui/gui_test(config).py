import tkinter as tk
import random as r
root = tk.Tk()
root.title("my application")
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
x = 0
y = 0
print(h,w)
root.geometry(f"{w}x{h}+{x}+{y}")

l1 = tk.Label(root,text="heading",
              bg="purple",fg="white",font=("monaco",30))
l1.pack(side="top",fill="x")

l2 = tk.Label(root,text="this will show otp",bg="purple",fg="white",font=("monaco",30))
l2.place(x=250,y=h*0.2,height=100,width=500)
def fun():
    l2.config(text=f"otp: {r.randint(1000,9999)}")
b2 = tk.Button(text="click me to print",font=("monaco",30),
               command=fun)
b2.pack()
root.mainloop()