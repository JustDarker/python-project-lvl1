from random import randrange

game_q = "What number is missing in the progression?"


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

    return srtProgr


def rightAnswer(question):
    progression = question.split(" ")

    for (index, element) in enumerate(progression):
        if progression[index] != ".." and progression[index+1] != "..":
            return int(progression[index+1]) - int(progression[index])
