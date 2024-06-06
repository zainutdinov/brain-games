import random


def is_prime(random_number):
    n = 2
    while random_number % n != 0:
        n += 1
    return random_number == n


def create_prime_question():
    random_number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(random_number) else "no"
    return random_number, correct_answer
