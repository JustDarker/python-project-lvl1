from random import randrange

game_q = 'Answer "yes" if number even otherwise answer "no".'

def main():
    return randrange(1, 101)

def rightAnswer(answer):
    if answer % 2 == 0:
        return "yes"
    elif answer % 2 != 0: 
        return "no"  