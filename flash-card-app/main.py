BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pathlib import Path

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50)

canvas = Canvas(height=526,width=800)
# 1. Get the directory of the current script, then append the file name
card_front_file_path = Path(__file__).parent / "images/card_front.png"
card_front_image = PhotoImage(file=card_front_file_path)
canvas.create_image(400, 263, image=card_front_image)
# Keep both pieces of text on the card canvas so their positions are relative
# to the card rather than to the window's grid.
language_id = canvas.create_text(400, 160, text="French", font=("Arial", 24, "italic"))
word_id = canvas.create_text(400, 263, text="", font=("Arial", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_image = PhotoImage(file=Path(__file__).parent / "images/wrong.png")
right_image = PhotoImage(file=Path(__file__).parent / "images/right.png")

def click_correct():
    pass

def click_wrong():
    pass

wrong_button = Button(image=wrong_image, command=click_wrong)
wrong_button.grid(row=2, column=0, sticky="w")

correct_button = Button(image=right_image, command=click_correct)
correct_button.grid(row=2, column=1, sticky="e")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


window.mainloop()
