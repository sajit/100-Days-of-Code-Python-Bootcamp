from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))

# for question in question_bank:
#     print(question)

quizbrain = QuizBrain(question_bank)

quizbrain.play_game()