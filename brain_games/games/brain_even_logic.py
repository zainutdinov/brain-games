import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def game_logic_even():
    random_number = random.randint(1, 100)
    correct_answer = is_even(random_number)
    return random_number, correct_answer
