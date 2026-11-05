from tkinter import *
from tkinter import messagebox
import random
import string
import json

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

    password_entry = password.get()
    if password_entry == "":
        messagebox.showerror(title="Error",message="Password required")
        return
    entry = {
        "email": email_entry,
        "password": password_entry
    }
    password_data = get_password_data()

    with open("password_data.json",mode="w") as f:    
        password_data.update({website_entry:entry})
        f.write(json.dumps(password_data))
        messagebox.showinfo(title="Save",message="Added password to manager")

    website.delete(0,END)
    email.delete(0,END)
    password.delete(0,END) 

def get_password_data():
    try:
        with open("password_data.json") as f:
            try:
                password_data = json.load(f)
            except json.decoder.JSONDecodeError:
                print("Empty file or not json")
                return {}
    except FileNotFoundError:
            return {}
    return password_data   

# ---------------------------LOOKUP WEBSITE ----------------------------------#
def lookup_website():
    email.delete(0,END)
    password.delete(0,END) 
    website_entry = website.get()
    if website_entry == "":
        return
    password_data = get_password_data()
    keys_list = list(password_data.keys())
    if website_entry in keys_list:
        username = password_data[website_entry]['email']
        pwd_string = password_data[website_entry]['password']
        password.insert(0,pwd_string)
        email.insert(0,username)
    else:
        messagebox.showinfo(title="Result",message="Site not found")



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

search_button=Button(text="Search",command=lookup_website)
search_button.grid(row=1,column=2)

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