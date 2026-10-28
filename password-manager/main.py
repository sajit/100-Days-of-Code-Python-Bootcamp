from tkinter import *
from pathlib import Path

# 1. Get the directory of the current script, then append the file name
file_path = Path(__file__).parent / "logo.png"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
print(file_path)
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file=file_path)
canvas.create_image(100,100,image=logo_image)
canvas.pack()


window.mainloop()