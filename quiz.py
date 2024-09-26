from api import Api
import time

class Question:

    def __init__(self):
        self.question_number = 0
        self.user_score = 0

    def game(self, question):
        print("Welcome! Please answer the questions with True or False\n")
        while self.question_number < len(question):
            text = question[self.question_number]["question"]
            correct_answer = question[self.question_number]["correct_answer"]
            self.question_number += 1
            user_input = input(f"Q.{self.question_number}: {text}\nAnswer: ")
            self.check_answer(user_input, correct_answer)
        print(
            f"Game is over!\nYour final score is: {self.user_score} / {self.question_number}"
        )
        time.sleep(5)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.capitalize() == correct_answer:
            self.user_score += 1
            print(
                f"Good job!\nScore: {self.user_score} / {self.question_number}\n"
            )
        else:
            print(
                f"Sorry, wrong answer.\nScore: {self.user_score} / {self.question_number}\n"
            )


if __name__ == "__main__":
    main()
