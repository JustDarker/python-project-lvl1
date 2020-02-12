from random import randrange

QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    question = randrange(1, 101)
    return question, right_answer(question)


def right_answer(question):
    if question % 2 == 0:
        return "yes"
    elif question % 2 != 0:
        return "no"
