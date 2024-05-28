#!/usr/bin/env python3

import random
from ..general_logic import hello, checking_answer, successful_game


def brain_calc_game():
    name = hello()
    print('What is the result of the expression?')
    for _ in range(3):
        operators = ['+', '-', '*']
        random_operator = random.choice(operators)
        random_num_1 = random.randint(1, 100)
        random_num_2 = random.randint(1, 100)
        question = f'{random_num_1} {random_operator} {random_num_2}'
        correct_answer = str(eval(question))

        if not checking_answer(question, correct_answer, name):
            return
    successful_game(name)
