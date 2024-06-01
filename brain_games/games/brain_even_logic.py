import random
from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def game_even_logic():
    random_number = random.randint(1, 100)
    correct_answer = is_even(random_number)
    return random_number, correct_answer


def launch_game_even():
    launching_the_game(task, COUNT_ROUND, game_even_logic)
