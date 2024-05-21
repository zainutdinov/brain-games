import prompt
import random


# Функция игры «Проверка на чётность»
def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        random_number = random.randint(1, 100)

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f'Question: {random_number}')
        answer_user = prompt.string('Your answer: ')

        if answer_user == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            i = 5

    if i == 4:
        print(f'Congratulations, {name}!')
