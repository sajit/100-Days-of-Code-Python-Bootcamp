from tkinter import *

window = Tk()

window.title("Miles to Km converter")
window.minsize(width=500,height=300)

label = Label(text="Enter miles")
label.pack()
entry = Entry(width=20)

entry.pack()

def button_click():
    miles = entry.get()
    km = float(miles) * 1.6
    km_label = Label(text=f"{km:.2f} km")
    km_label.pack()

button = Button(text="Convert",command=button_click)
button.pack()

window.mainloop()