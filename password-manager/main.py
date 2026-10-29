from tkinter import *
from tkinter import messagebox
import random
import string

from pathlib import Path


# 1. Get the directory of the current script, then append the file name
file_path = Path(__file__).parent / "logo.png"
# Comprehensive list of standard password special characters
password_symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', 
    ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`', 
    '"', "'"
]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = random.sample(list(string.ascii_letters),random.randint(4,6))
    digits = random.sample(['0','1','2','3','4','5','6','7','8','9'],random.randint(4,6))
    symbols = random.sample(password_symbols,random.randint(4,6))
    password_content = letters + digits + symbols
    random.shuffle(password_content)
    pwd_string = "".join(password_content)
    password.insert(0,pwd_string)
    

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_entry = website.get()
    if website_entry == "":
        messagebox.showerror(title="Error",message="Website required")
        return

    email_entry = email.get()
    if email_entry == "":
        messagebox.showerror(title="Error",message="Email required")
        return
    

    pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
print(file_path)
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file=file_path)
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)
website = Entry()
website.grid(row=1,column=1)

email_label = Label(text="Email")
email_label.grid(row=2,column=0)
email = Entry()
email.grid(row=2,column=1)

password_label = Label(text="Password")
password_label.grid(row=3,column=0)

password = Entry()
password.grid(row=3,column=1)

password_gen_button=Button(text="Generate",command=generate_password)
password_gen_button.grid(row=3,column=2)

save_button=Button(text="Save",command=save_password)
save_button.grid(row=4,column=1)


window.mainloop()