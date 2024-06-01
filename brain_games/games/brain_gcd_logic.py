import math
import random

task = 'Find the greatest common divisor of given numbers.'


def game_logic():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    correct_answer = str(math.gcd(random_number_1, random_number_2))
    question = f'{random_number_1} {random_number_2}'
    return question, correct_answer
