import prompt


# Приветствие пользователя и сохранение имени
def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Проверка ответа на корректность
def checking_answer(question, correct_answer, name):
    print(f'Question: {question}')
    answer_user = prompt.string('Your answer: ')

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