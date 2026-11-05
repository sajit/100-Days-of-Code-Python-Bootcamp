BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pathlib import Path
import pandas
import random


displayed_words = []
df = pandas.read_csv(Path(__file__).parent / "data/french_words.csv",index_col=0)
my_dict = df.iloc[:, 0].to_dict()
correct_guess = []
flip_timer = None
current_french_word = None

french_words = list(my_dict.keys())
# -------------------------- DISPLAY WORD ------------------------------#
def get_next_word():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
        flip_timer = None

    next_word = random.choice(french_words)
    canvas.itemconfig(card_id, image=card_front_image)
    canvas.itemconfig(language_id, text="French")
    canvas.itemconfig(word_id, text=f"{next_word}")
    global current_french_word
    current_french_word = next_word
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global flip_timer
    flip_timer = None
    global current_french_word
    french_word = canvas.itemcget(word_id, "text")
    current_french_word = french_word
    canvas.itemconfig(card_id, image=card_back_image)
    canvas.itemconfig(language_id, text="English")
    canvas.itemconfig(word_id, text=my_dict[french_word])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50)

canvas = Canvas(height=526,width=800)
# 1. Get the directory of the current script, then append the file name
card_front_file_path = Path(__file__).parent / "images/card_front.png"
card_front_image = PhotoImage(file=card_front_file_path)
card_back_file_path = Path(__file__).parent / "images/card_back.png"
card_back_image = PhotoImage(file=card_back_file_path)
card_id = canvas.create_image(400, 263, image=card_front_image)
# Keep both pieces of text on the card canvas so their positions are relative
# to the card rather than to the window's grid.
language_id = canvas.create_text(400, 160, text="French", font=("Arial", 24, "italic"))
word_id = canvas.create_text(400, 263, text="", font=("Arial", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_image = PhotoImage(file=Path(__file__).parent / "images/wrong.png")
right_image = PhotoImage(file=Path(__file__).parent / "images/right.png")

def click_correct():
    #Remove the word from french_words . #add it to known words list
    correct_guess.append(current_french_word)
    french_words.remove(current_french_word)
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
