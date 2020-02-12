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

    new_right_answer = right_answer(progression)

    unknown_element_pos = randrange(0, 10)
    progression[unknown_element_pos] = ".."

    srtProgr = ' '.join(str(x) for x in progression)

    return srtProgr, new_right_answer


def right_answer(question):
    return str(question[1] - question[0])
