def brain_calc():
    game_q = "What is the result of the expression?"
    number1 = randrange(1, 101)
    number2 = randrange(1, 101)
    operator = rand('+', '-', '*')
    q = str(number1) + operator + str(number2)

    if operator == '+':
        answer = number1 + number2
    if operator == '-':
        answer = number1 - number2
    if operator == '*':
        answer = number1 * number2
    