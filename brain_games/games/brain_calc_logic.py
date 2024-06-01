import random
import operator

task = 'What is the result of the expression?'


def game_logic():
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
