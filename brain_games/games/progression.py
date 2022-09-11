from random import randint, choice


GUIDE = 'What number is missing in the progression?'

def generate_round():
    increment = randint(2, 10)
    start_number = randint(1, 10)

    question = [start_number]
    i = 0
    num = start_number
    while i < 10:
        num += increment
        question.append(num)
        i += 1
    correct_answer = choice(question)
    index_correct_answer = question.index(correct_answer)
    question[index_correct_answer] = '..'
    question = ' '.join(map(str, question))

    return question, str(correct_answer)

