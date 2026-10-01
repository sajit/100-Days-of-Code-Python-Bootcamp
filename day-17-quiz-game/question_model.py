class Question:

    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

    def get_text(self):
        return self.text

    def get_answer(self):
        return self.answer

    def __str__(self):
        return f"Q: {self.text}, A:{self.answer}"