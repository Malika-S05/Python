from ques_bank import question_bank

question_list = question_bank


class QuizBrain:
    def __init__(self, questionlist):
        self.question_number = 0
        self.question_list = questionlist
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(ans,current_question.answer)
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, usr, crt):
        if usr.lower() == crt.lower():
            print("You got it right🏆😁!.")
            self.score += 1
        else:
            print("That's wrong😔")
        print(f"The correct answer was: {crt}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")


quiz = QuizBrain(question_list)
is_correct = True
while quiz.still_has_question():
    quiz.next_question()

print(f"""You've completed the quiz
Your final score was: {quiz.score}/{quiz.question_number}""")