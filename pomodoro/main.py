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

window = Tk()
window.title("Pomodoro")
window.minsize(width=300,height=300)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/pomodoro/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(110, 130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)
window.after_id = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button_handler():
    if window.after_id is not None:
        window.after_cancel(window.after_id)
        window.after_id = None
        print("Stopping execution")
    canvas.itemconfig(text_id, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


def update_timer(elapsed,TIMER_LIMIT,countUp):
    if elapsed > TIMER_LIMIT * 60:
        return
    if countUp:
        minutes, seconds = divmod(elapsed,60)
    else:
        minutes, seconds = divmod((TIMER_LIMIT*60)-elapsed,60)
    canvas.itemconfig(text_id, text=f"{minutes:02d}:{seconds:02d}")

    if elapsed < TIMER_LIMIT * 60:
        window.after_id = window.after(1000, update_timer, elapsed + 1, TIMER_LIMIT,countUp)

def start_button_handler():
    update_timer(0,WORK_MIN,True)

def short_break_handler():
    update_timer(0,SHORT_BREAK_MIN,False)

def long_break_handler():
    update_timer(0,LONG_BREAK_MIN,False)


    
start_button = Button(text="Start",command=start_button_handler)

start_button.grid(row=3,column=0)

reset_button = Button(text="Reset",command=reset_button_handler)

reset_button.grid(row=3,column=1)

short_break_button = Button(text="Short break",command=short_break_handler)

short_break_button.grid(row=3,column=2)

long_break_button = Button(text="Long break",command=long_break_handler)

long_break_button.grid(row=3,column=3)


window.mainloop()
