from api import Api
from quiz import Question

def main():

    initialize_api = Api()
    questions = initialize_api.quiz_request()
    quiz_list = []

    for item in questions:
        quiz_list.append(item)


    initialize_question = Question()
    test = initialize_question.test(quiz_list)
    print(test)


if __name__ == "__main__":
    main()