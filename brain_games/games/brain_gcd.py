from random import randrange
from math import gcd

QUESTION = "Find the greatest common divisor of given numbers."


def main():
    return str(randrange(10, 50)) + " " + str(randrange(10, 50))


def right_answer(question):
    number1, number2 = question.split()
    return gcd(int(number1), int(number2))
