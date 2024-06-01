import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    n = 2
    while random_number % n != 0:
        n += 1
    return 'yes' if random_number == n else 'no'


def game_logic_prime():
    random_number = random.randint(1, 100)
    correct_answer = is_prime(random_number)
    return random_number, correct_answer
