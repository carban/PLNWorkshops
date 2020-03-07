from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('550x500')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)

window.mainloop()
