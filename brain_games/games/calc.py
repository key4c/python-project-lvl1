from random import randint
from random import choice


GUIDE = 'What is the result of the expression?'
START_NUMBER = 1
STOP_NUMBER = 100


def generate_round():
    operators = ['+', '-', '*']
    first_operand = randint(START_NUMBER, STOP_NUMBER)
    second_operand = randint(START_NUMBER, STOP_NUMBER)
    random_operator = choice(operators)
    if random_operator == '+':
        correct_answer = first_operand + second_operand
    elif random_operator == '-':
        correct_answer = first_operand - second_operand
    elif random_operator == '*':
        correct_answer = first_operand * second_operand
    question = f'{first_operand} {random_operator} {second_operand}'
    return question, str(correct_answer)
