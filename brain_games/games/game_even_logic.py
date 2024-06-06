import random


def is_even(random_number):
    return random_number % 2 == 0


def create_even_question():
    random_number = random.randint(1, 100)
    correct_answer = "yes" if is_even(random_number) else "no"
    return random_number, correct_answer
