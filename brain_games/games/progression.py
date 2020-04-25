from random import randrange


QUESTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10


def main():
    progression = []
    progression_start = randrange(1, 100)
    progression_step = randrange(1, 10)

    progression.append(progression_start)

    i = 1

    while i < PROGRESSION_LENGTH:
        progression.append(progression_start + progression_step * i)
        i = i + 1

    unknown_element_pos = randrange(0, 10)

    new_right_answer = right_answer(progression, unknown_element_pos)

    progression[unknown_element_pos] = ".."

    srtProgr = ' '.join(str(x) for x in progression)

    return srtProgr, new_right_answer


def right_answer(question, unknown_element_pos):
    return str(question[unknown_element_pos])
