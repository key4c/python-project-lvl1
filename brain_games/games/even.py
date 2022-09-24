from random import randint


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NAMBER = 1
STOP_NAMBER = 100


def generate_round():
    random_number = randint(START_NAMBER, STOP_NAMBER)
    question = f'{random_number}'
    correct_answer = 'no' if random_number % 2 != 0 else "yes"
    return question, correct_answer
