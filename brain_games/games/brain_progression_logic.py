#!/usr/bin/env python3

import random
from ..general_logic import hello, checking_answer, successful_game


def brain_progression_game():
    name = hello()
    print('What number is missing in the progression?')
    for _ in range(3):
        progression = []
        finish_progression = random.randint(5, 10)
        progression_step = random.randint(1, 10)
        element = random.randint(1, 10)
        progression.append(element)
        for _ in range(finish_progression + 1):
            element += progression_step
            progression.append(element)
        hidden_element_id = random.randint(0, len(progression) - 1)
        correct_answer = str(progression[hidden_element_id])
        progression[hidden_element_id] = '..'
        question = f'{' '.join(map(str, progression))}'

        if not checking_answer(question, correct_answer, name):
            return
    successful_game(name)
