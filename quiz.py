from api import Api
class Question:

    def __init__(self):
        self.question_number = 0
        self.user_score = 0
    

    def game(self, question):
        while self.question_number < len(question):
            text = question[self.question_number]["question"]
            correct_answer = question[self.question_number]["correct_answer"]
            self.question_number += 1
            user_input = input(f"Q.{self.question_number}: {text}")
            check_answer(user_input, correct_answer)


    def check_answer(self, user_asnwer, correct_answer):
        if user_answer.capitalize() == correct_answer:
            self.user_score += 1
            return f"Good job! Score: {self.user_score} / {self.question_number}"
        else:
            return f"Sorry, wrong answer.\nScore: {self.user_score} / {self.question_number}"
    


if __name__ == "__main__":
    main()
