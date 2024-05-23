#!/usr/bin/env python3

import prompt
import random
import math


# Приветствие пользователя и сохранение имени
def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Проверка ответа на корректность
def checking_answer(answer_user, correct_answer, name):
    if answer_user == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer_user}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


# Отправка сообщения в случае успешного завершения игры
def successful_game(name):
    print(f'Congratulations, {name}!')


# Логика всех игр
def logic_games(game_name):
    name = hello()
    match game_name:
        case 'brain_calc':  # Игра: «Калькулятор»
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
        case 'brain_even':  # Игра: «Проверка на чётность»
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
        case 'brain_gcd':  # Игра «НОД» (наибольший общий делитель)
            print('Find the greatest common divisor of given numbers.')
            for _ in range(3):
                random_number_1 = random.randint(1, 100)
                random_number_2 = random.randint(1, 100)
                correct_answer = str(math.gcd(random_number_1, random_number_2))
                print(f'Question: {random_number_1} {random_number_2}')
                answer_user = prompt.string('Your answer: ')

                if not checking_answer(answer_user, correct_answer, name):
                    return
        case 'brain_progression':  # Игра «Арифметическая прогрессия»
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
                print(f'Question: {' '.join(map(str, progression))}')
                answer_user = prompt.string('Your answer: ')

                if not checking_answer(answer_user, correct_answer, name):
                    return
        case 'brain_prime':  # Игра «Простое ли число?»
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
                print(f'Question: {random_number}')
                answer_user = prompt.string('Your answer: ')
                if not checking_answer(answer_user, correct_answer, name):
                    return
    successful_game(name)
