from random import randint


GUIDE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def generate_round():
    random_number = randint(1, 10)
    question = f'{random_number}'
    k = 0
    for i in range(2, random_number // 2+1):
        if (random_number % i == 0):
            k += 1
    correct_answer = 'yes' if k <= 0 else "no"
    return question, correct_answer

