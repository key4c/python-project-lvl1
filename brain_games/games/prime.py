from random import randint


GUIDE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Воженная функция проверяет является ли число простым.
def is_prime(random_number):
    if random_number <= 1:
        return False
    else:
        for i in range(2, random_number // 2 + 1):
            if random_number % i == 0:
                return False
    return True


def generate_round():
    random_number = randint(0, 100)
    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
