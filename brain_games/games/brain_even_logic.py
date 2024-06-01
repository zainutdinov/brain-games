import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def game_logic():
    random_number = random.randint(1, 100)
    correct_answer = is_even(random_number)
    question = random_number
    return question, correct_answer
