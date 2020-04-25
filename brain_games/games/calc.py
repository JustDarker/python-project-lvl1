from random import choice, randrange
from operator import add, sub, mul


QUESTION = "What is the result of the expression?"


def main():
    number1 = randrange(3, 12)
    number2 = randrange(3, 12)

    operations = [('+', add), ('-', sub), ('*', mul)]
    my_operator, function = choice(operations)

    question = "{} {} {}".format(number1, my_operator, number2)

    return question, str(right_answer(number1, number2, function))


def right_answer(number1, number2, function):
    return function(number1, number2)
