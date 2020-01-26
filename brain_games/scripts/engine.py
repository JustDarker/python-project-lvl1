from brain_games import cli


def run(game):
    name = cli.run()
    print(game.game_q)

    count = 0

    for i in range(3):
        question = game.main()
        print('Question: ' + str(question))

        answer = cli.answer()

        rightAnswer = game.rightAnswer(question)

        if answer == str(rightAnswer):
            print("Correct!\n")
            count = count + 1
        elif answer != rightAnswer:
            print("\n" + str(answer) + " is wrong answer ;(. Correct answer was " + str(rightAnswer))
            print("Let's try again, " + str(name))
            break

    if count == 3:
        print("Congratulations, " + name)
