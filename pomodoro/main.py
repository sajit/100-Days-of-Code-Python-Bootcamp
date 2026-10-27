from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=300,height=300)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/pomodoro/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(110, 130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()
window.after_id = None

def update_timer(elapsed):
    if elapsed > WORK_MIN * 60:
        return
    minutes, seconds = divmod(elapsed,60)
    canvas.itemconfig(text_id, text=f"{minutes:02d}:{seconds:02d}")

    if elapsed < WORK_MIN * 60:
        window.after_id = window.after(1000, update_timer, elapsed + 1)

def start_button_handler():
    update_timer(0)


def reset_button_handler():
    if window.after_id is not None:
        window.after_cancel(window.after_id)
        window.after_id = None
        print("Stopping execution")
    canvas.itemconfig(text_id, text="00:00")
    
start_button = Button(text="Start",command=start_button_handler)

start_button.pack()

reset_button = Button(text="Reset",command=reset_button_handler)

reset_button.pack()


window.mainloop()
