import random
from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game

task = 'What number is missing in the progression?'


def progression_generation():
    progression = []
    finish_progression = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    element = random.randint(1, 10)
    progression.append(str(element))
    for _ in range(finish_progression + 1):
        element += progression_step
        progression.append(str(element))
    return progression


def game_progression_logic():
    progression = progression_generation()
    hidden_element_id = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_element_id]
    progression[hidden_element_id] = '..'
    question = ' '.join(progression)
    return question, correct_answer


def launch_game_progression():
    launching_the_game(task, COUNT_ROUND, game_progression_logic)
