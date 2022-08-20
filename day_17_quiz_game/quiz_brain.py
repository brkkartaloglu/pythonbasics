class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {item.text} (True/False)?: ")
        self.check_answer(answer, item.answer)

    def check_answer(self, answer, corrrect_answer):
        if answer.lower() == corrrect_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"Current score is: {self.score}/{self.question_number}\n")
