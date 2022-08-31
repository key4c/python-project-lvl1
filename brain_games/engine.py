from prompt import string


NUMBER_OF_ATTEMPTS = 3


def start_the_game(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GUIDE)
    for i in range(NUMBER_OF_ATTEMPTS):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
