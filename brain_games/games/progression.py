from random import randrange


QUESTION = "What number is missing in the progression?"


def main():
    progression = []
    progression_start = randrange(1, 100)
    progression_step = randrange(1, 10)

    progression.append(progression_start)

    i = 1

    while i < 10:
        progression.append(progression[i - 1] + progression_step)
        i = i + 1

    unknownElementPos = randrange(0, 10)
    progression[unknownElementPos] = ".."

    srtProgr = ' '.join(str(x) for x in progression)

    return srtProgr, right_answer(progression)


def right_answer(question):
    return str(question[1] - question[0])
