from random import randrange

QUESTION = "Find the greatest common divisor of given numbers."


def main():
    question = str(randrange(10, 50)) + " " + str(randrange(10, 50))
    return question, right_answer(question)


def right_answer(question):
    number1, number2 = question.split()

    def my_gcd(a, b):
        while b:
            a, b = b, a % b
        return str(abs(a))

    return my_gcd(int(number1), int(number2))
