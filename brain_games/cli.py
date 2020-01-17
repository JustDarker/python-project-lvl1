import prompt


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!\n")
    return name


def answer():
    answer = input("Your answer: ")
    return answer


def greeting():
    print("Welcome to the Brain Games!\n")
