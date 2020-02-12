from brain_games import cli


def run(game):
    name = cli.run()
    print(game.QUESTION)

    for i in range(3):
        question, right_answer = game.main()

        print("Question: {}".format(question))

        answer = cli.answer()

        if answer == right_answer:
            print("Correct!\n")
        elif answer != right_answer:
            template = "\n{} is wrong answer ;(. Correct answer was {}"
            print(template.format(answer, right_answer))
            print("Let's try again, {}".format(name))
            break
    else:
        print("Congratulations, {}".format(name))
