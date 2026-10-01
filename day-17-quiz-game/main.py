from question_model import Question
from data import question_data

questions = []
for item in question_data:
    questions.append(Question(item["text"],item["answer"]))

for question in questions:
    print(question)