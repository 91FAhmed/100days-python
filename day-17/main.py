from question_model import question_initializer
from data import question_data
from quiz_brain import question_brain

question_bank = []

for question in question_data:
    newQuestion = question_initializer(question['text'],question['answer'])
    question_bank.append(newQuestion)
    
question_brain = question_brain(question_bank)

while question_brain.has_questions():
    question_brain.next_question()


print("You've completed the quiz")
print(f"Your final score was {question_brain.curr_score}/10")