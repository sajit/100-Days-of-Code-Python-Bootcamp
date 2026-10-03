#TODO ask questions
# TODO : check if answer is correct
# TODO : exit at end
from question_model import Question
class QuizBrain:

    def __init__(self,question_bank:list[Question]):
        self.question_bank = question_bank

    def play_game(self):
        score = 0
        for question in self.question_bank:
          
            user_response = input(f"Question: {question.text} (True/False)")
            if user_response == question.answer:
                score +=1
                print("Correct!")
            else:
                print("Sorry wrong.")
        print(f"You got {score} right out of {len(self.question_bank)}")
        return