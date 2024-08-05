from data import question_data

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


question_bank =[]
for item in question_data:
   question_bank.append(Question(item["text"],item["answer"]))


