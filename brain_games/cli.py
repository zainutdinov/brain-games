import prompt


def welcome_user():
    # Приветствие пользователя и сохранение имени

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
