from random import randint


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(1, 100)
    question = f'{random_number}'
    correct_answer = 'no' if random_number % 2 != 0 else "yes"
    return question, correct_answer
