from random import randrange


game_q = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    return randrange(1, 102)


def rightAnswer(question):
    primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    if question in primes:
        return "yes"
    else:
        return "no"
