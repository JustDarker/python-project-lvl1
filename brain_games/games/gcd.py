from random import randrange

QUESTION = "Find the greatest common divisor of given numbers."


def main():
    number1 = randrange(10, 50)
    number2 = randrange(10, 50)
    return "{} {}".format(number1, number2), my_gcd(number1, number2)


def my_gcd(a, b):
    while b:
        a, b = b, a % b
    return str(abs(a))
