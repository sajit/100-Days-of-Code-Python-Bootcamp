BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pathlib import Path
import pandas
import random


displayed_words = []
df = pandas.read_csv('data/french_words.csv',index_col=0)
my_dict = df.iloc[:, 0].to_dict()
correct_guess = []

french_words = list(my_dict.keys())
# -------------------------- DISPLAY WORD ------------------------------#
def get_next_word():
    next_word = random.choice(french_words)
    canvas.itemconfig(word_id, text=f"{next_word}")


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
    #Remove the word from french_words . #add it to known words list
    current_word = canvas.itemcget(word_id, "text")
    correct_guess.append(current_word)
    french_words.remove(current_word)
    get_next_word()

def click_wrong():
    get_next_word()

wrong_button = Button(image=wrong_image, command=click_wrong)
wrong_button.grid(row=2, column=0, sticky="w")

correct_button = Button(image=right_image, command=click_correct)
correct_button.grid(row=2, column=1, sticky="e")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

get_next_word()
window.mainloop()
