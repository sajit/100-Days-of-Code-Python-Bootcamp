from tkinter import *

window = Tk()
window.title("My first TK GUI")
window.minsize(width=500,height=300)

label = Label(text="Label text")

def button_click_handler():
    label.config(text="Button got clicked")

def clear_handler():
    label.config(text="")

button = Button(text="Click Me",command=button_click_handler)

clear_button = Button(text="Clear",command=clear_handler)

label.pack()

button.pack()
clear_button.pack()

window.mainloop()