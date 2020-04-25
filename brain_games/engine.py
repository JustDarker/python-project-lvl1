from brain_games import cli


QUESTION_COUNT = 3


def run(game):
    name = cli.run()
    print(game.QUESTION)

    for _ in range(QUESTION_COUNT):
        question, right_answer = game.main()

        print("Question: {}".format(question))

        answer = cli.answer()

        if right_answer is True:
            right_answer = "yes"

        if right_answer is False:
            right_answer = "no"

        if answer != right_answer:
            template = "\n{} is wrong answer ;(. Correct answer was {}"
            print(template.format(answer, right_answer))
            print("Let's try again, {}".format(name))
            break

        print("Correct!\n")

    else:
        print("Congratulations, {}".format(name))
