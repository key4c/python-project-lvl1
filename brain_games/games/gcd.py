from random import randint
from math import gcd


GUIDE = 'Find the greatest common divisor of given numbers.'
TART_NAMBER = 1
STOP_NAMBER = 100


def generate_round():
    random_number1 = randint(START_NAMBER, STOP_NAMBER)
    random_number2 = randint(START_NAMBER, STOP_NAMBER)
    question = f'{random_number1} {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return question, correct_answer
