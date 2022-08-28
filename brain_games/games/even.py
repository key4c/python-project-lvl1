import prompt
from random import randint


def even_game():
    user_name = prompt.string('Welcome to the Brain Games!\
                              \nMay I have your name? ')
    print(
        f'Hello, {user_name}!\
        \nAnswer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = str(input('Your answer: '))
        correct_answer = ('no' if random_number % 2 != 0 else 'yes')
        if user_answer != correct_answer:
            print(f'{user_answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {user_name}')
            break
        else:
            print("Correct!")
            i += 1
        if i == 3:
            print(f'Congratulations, {user_name}!')
            break
