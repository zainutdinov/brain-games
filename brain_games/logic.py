#!/usr/bin/env python3

import prompt
import random
import math


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def checking_answer(answer_user, correct_answer, name):
    if answer_user == correct_answer:
            print('Correct!')
            return True
    else:
        print(f"'{answer_user}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def successful_game(name):
     print(f'Congratulations, {name}!')
     

def logic_games(game_name):
    name = hello()
    match game_name:
        case 'brain_calc':
            print('What is the result of the expression?')
            for _ in range(3):
                operators = ['+', '-', '*']
                random_operator = random.choice(operators)
                random_number_1 = random.randint(1, 100)
                random_number_2 = random.randint(1, 100)
                question = f'{random_number_1} {random_operator} {random_number_2}'
                correct_answer = str(eval(question))
                print(f'Question: {question}')
                answer_user = prompt.string('Your answer: ')
                
                if not checking_answer(answer_user, correct_answer, name):
                    return
        case 'brain_even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
            for _ in range(3):
                random_number = random.randint(1, 100)
                if random_number % 2 == 0:
                    correct_answer = 'yes'
                else:
                    correct_answer = 'no'
                print(f'Question: {random_number}')
                answer_user = prompt.string('Your answer: ')

                if not checking_answer(answer_user, correct_answer, name):
                    return
        case 'brain_gcd':
            print('Find the greatest common divisor of given numbers.')
            for _ in range(3):
                random_number_1 = random.randint(1, 100)
                random_number_2 = random.randint(1, 100)
                correct_answer = str(math.gcd(random_number_1, random_number_2))
                print(f'Question: {random_number_1} {random_number_2}')
                answer_user = prompt.string('Your answer: ')

                if not checking_answer(answer_user, correct_answer, name):
                        return
    successful_game(name)
