#!/usr/bin/env python3

import random
from ..general_logic import hello, checking_answer, successful_game


def brain_prime_game():
    name = hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        random_number = random.randint(1, 100)
        n = 2
        while random_number % n != 0:
            n += 1
        if random_number == n:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question = random_number

        if not checking_answer(question, correct_answer, name):
            return
    successful_game(name)
