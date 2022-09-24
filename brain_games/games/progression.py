from random import randint, choice


GUIDE = 'What number is missing in the progression?'
INCREMENT_START_NUMBER, INCREMENT_STOP_NUMBER = 2, 10
START_NUMBER, STOP_NUMBER = 1, 100


def generate_round():
    increment = randint(INCREMENT_START_NUMBER, INCREMENT_STOP_NUMBER)
    first_number = randint(START_NUMBER, STOP_NUMBER)

    question = [first_number]
    i = 0
    num = first_number
    while i < 10:
        num += increment
        question.append(num)
        i += 1
    correct_answer = choice(question)
    index_correct_answer = question.index(correct_answer)
    question[index_correct_answer] = '..'
    question = ' '.join(map(str, question))

    return question, str(correct_answer)
