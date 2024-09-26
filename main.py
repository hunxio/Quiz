from api import Api
from quiz import Question


def main():

    api = Api()
    questions = api.quiz_request()
    quiz_list = []

    for item in questions:
        quiz_list.append(item)

    question = Question()
    game = question.game(quiz_list)


if __name__ == "__main__":
    main()
