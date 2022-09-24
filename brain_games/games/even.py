from random import randint


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUMBER = 1
STOP_NUMBER = 100


def generate_round():
    random_number = randint(START_NUMBER, STOP_NUMBER)
    question = f'{random_number}'
    correct_answer = 'no' if random_number % 2 != 0 else "yes"
    return question, correct_answer
