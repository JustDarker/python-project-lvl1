from random import randrange

QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    question = randrange(1, 101)
    return question, is_even(question)


def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False
