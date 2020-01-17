from brain_games import cli
from random import randrange
#from brain_games.scripts import engine


def main():
    name = cli.run()
    print('Answer "yes" if number even otherwise answer "no".')

    count = 0

    for i in range(3):
        number = randrange(1, 101)
        print('Question: ' + str(number))
        answer = cli.answer()

        if number % 2 == 0 and answer == 'yes':
            print('Correct!\n')
            count = count + 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!\n')
            count = count + 1
        else:
            print(str(answer) + " is wrong answer ;(. Correct answer was " + ("'yes'" if number % 2 == 0 else "'no'"))
            break

    if count == 3:
        print("Congratulations, " + name + "!")
