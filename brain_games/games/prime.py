from random import randrange


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    question = randrange(1, 102)
    return question, is_prime(question)


def is_prime(question):

    divider_count = 0

    for number in range(1, question+1):
        if int(question) % number == 0.0:
            divider_count = divider_count + 1

    if divider_count == 2 and question != 1:
        return "yes"
    else:
        return "no"
