THEME_COLOR = "#375362"

from tkinter import *
from pathlib import Path
class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.columnconfigure((0, 1), weight=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}",background=THEME_COLOR,fg="white")
        self.score_label.grid(row=0, column=1, sticky="e")
        self.right_button_image = PhotoImage(file=Path(__file__).parent / "images/true.png")

        self.right_button = Button(image=self.right_button_image, command=self.click_true)
        self.right_button.grid(row=2, column=0, pady=(0, 10))
        self.false_button_image = PhotoImage(file=Path(__file__).parent / "images/false.png")
        self.wrong_button = Button(image=self.false_button_image, command=self.click_false)
        self.wrong_button.grid(row=2, column=1, pady=(0, 10))

        self.display_next_question()
        self.window.mainloop()

    def click_true(self):
        self.check_answer("True")

    def click_false(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        # if not self.quiz.still_has_questions():
        #     return
        self.quiz.check_answer(user_answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.display_next_question()

    def display_next_question(self):
        self.canvas.delete("all")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.create_text(
                150, 125, width=280, text=question.text,
                font=("Arial", 20, "italic"), fill=THEME_COLOR,
            )
        else:
            self.canvas.create_text(
                150, 125, width=280, text="You've completed the quiz!",
                font=("Arial", 20, "italic"), fill=THEME_COLOR,
            )
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        
