from tkinter import *

window = Tk()
window.title("My first TK GUI")
window.minsize(width=500,height=300)

label = Label(text="Label text")

def button_click_handler():
    input = entry.get()
    label.config(text=input)

def clear_handler():
    entry.delete(0,END)
    label.config(text="")

button = Button(text="Click Me",command=button_click_handler)

clear_button = Button(text="Clear",command=clear_handler)

label.pack()

button.pack()
entry = Entry(width=20)
entry.pack()
clear_button.pack()

window.mainloop()