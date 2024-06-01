import random
from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    n = 2
    while random_number % n != 0:
        n += 1
    return 'yes' if random_number == n else 'no'


def game_prime_logic():
    random_number = random.randint(1, 100)
    correct_answer = is_prime(random_number)
    return random_number, correct_answer


def launch_game_prime():
    launching_the_game(task, COUNT_ROUND, game_prime_logic)
