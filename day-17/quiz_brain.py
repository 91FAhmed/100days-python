
class question_brain:
    
    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.curr_score = 0
    
    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        usr_answer = input(f"Q.{self.question_number}:{current_question.text}:(True/False)")
        self.check_answer(usr_answer,current_question.answer)

    def check_answer(self,usr_ans,correct_ans):
        if usr_ans.lower() == correct_ans.lower():
            print("You got right")
            self.curr_score += 1
        else:
            print("you are wrong")
        print(f"The answer was {correct_ans}")
        print(f"Your current score is {self.curr_score}")

