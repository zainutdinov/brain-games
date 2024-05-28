import math
import random
from ..general_logic import hello, checking_answer, successful_game


def brain_gcd_game():
    name = hello()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        correct_answer = str(math.gcd(random_number_1, random_number_2))
        question = f'{random_number_1} {random_number_2}'

        if not checking_answer(question, correct_answer, name):
            return
    successful_game(name)
