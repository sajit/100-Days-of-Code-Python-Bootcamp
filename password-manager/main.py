from tkinter import *
from pathlib import Path

# 1. Get the directory of the current script, then append the file name
file_path = Path(__file__).parent / "logo.png"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
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