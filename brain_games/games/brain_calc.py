from random import choice, randrange

game_q = "What is the result of the expression?"

def main():
    number1 = randrange(3, 12)
    number2 = randrange(3, 12)
    operator = choice('+-*')
    question = str(number1) + " " + operator + " " + str(number2)
    return question

def rightAnswer(question):
    number1, operator, number2 = question.split()

    if operator == '+':
        return int(number1) + int(number2)
    if operator == '-':
        return int(number1) - int(number2)
    if operator == '*':
        return int(number1) * int(number2)
    