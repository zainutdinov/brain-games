import random
import operator
from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game

task = 'What is the result of the expression?'


def game_calc_logic():
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    random_num_1 = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    question = f'{random_num_1} {random_operator} {random_num_2}'
    match random_operator:
        case '+':
            correct_answer = operator.add(random_num_1, random_num_2)
        case '-':
            correct_answer = operator.sub(random_num_1, random_num_2)
        case '*':
            correct_answer = operator.mul(random_num_1, random_num_2)
    correct_answer = str(correct_answer)
    return question, correct_answer


def launch_game_calc():
    launching_the_game(task, COUNT_ROUND, game_calc_logic)
