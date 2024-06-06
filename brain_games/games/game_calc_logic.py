import random
import operator


def calculate_operation(rand_operator, rand_num_1, rand_num_2):
    match rand_operator:
        case '+':
            correct_answer = operator.add(rand_num_1, rand_num_2)
        case '-':
            correct_answer = operator.sub(rand_num_1, rand_num_2)
        case '*':
            correct_answer = operator.mul(rand_num_1, rand_num_2)
    return correct_answer


def create_calc_question():
    operators = ['+', '-', '*']
    rand_operator = random.choice(operators)
    rand_num_1 = random.randint(1, 100)
    rand_num_2 = random.randint(1, 100)
    question = f'{rand_num_1} {rand_operator} {rand_num_2}'
    correct_answer = calculate_operation(rand_operator, rand_num_1, rand_num_2)
    correct_answer = str(correct_answer)
    return question, correct_answer
