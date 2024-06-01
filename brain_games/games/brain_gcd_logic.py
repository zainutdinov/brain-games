import math
import random
from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game

task = 'Find the greatest common divisor of given numbers.'


def game_gcd_logic():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    correct_answer = str(math.gcd(random_number_1, random_number_2))
    question = f'{random_number_1} {random_number_2}'
    return question, correct_answer


def launch_game_gcd():
    launching_the_game(task, COUNT_ROUND, game_gcd_logic)
