#!/usr/bin/env python3

from brain_games import cli
from random import randrange


def main():
    name = cli.run()
    print('Answer "yes" if number even otherwise answer "no".')

    count = 0

    for i in range(3):
        number = randrange(1, 101)
        print('Question: ' + str(number))
        answer = input("Your answer: ")

        if number % 2 == 0 and answer == 'yes':
            print('Correct!\n')
            count = count + 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!\n')
            count = count + 1
        else:
            print('Uncorrect( \n')

    if count == 3:
        print("3 out of 3! Congratulations, " + name + "!")
    else:
        print(str(count) + " out of 3. Better luck next time.")


if __name__ == '__main__':
    main()
