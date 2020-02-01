from brain_games import cli


def run(game):
    name = cli.run()
    print(game.QUESTION)

    count = 0

    for i in range(3):
        question = game.main()
        print('Question: ' + str(question))

        answer = cli.answer()

        right_answer = game.right_answer(question)

        if answer == str(right_answer):
            print("Correct!\n")
            count = count + 1
        elif answer != right_answer:
            template = "\n{} is wrong answer ;(. Correct answer was {}"
            print(template.format(str(answer), str(right_answer)))
            print("Let's try again, " + str(name))
            break

    if count == 3:
        print("Congratulations, " + name)
