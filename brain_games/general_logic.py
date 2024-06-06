import prompt


def greet_and_ask_question(task):
    # Приветствие пользователя, cохранение имени и вывод вопроса игры

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    return name


def check_answer(question, correct_answer, name):
    # Проверка ответа на корректность

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


def congratulate_winner(name):
    # Отправка сообщения в случае успешного завершения игры

    print(f'Congratulations, {name}!')


def launch_game(task, game, count_round=3):
    # Запуск игры

    name = greet_and_ask_question(task)
    for _ in range(count_round):
        question, correct_answer = game()
        if not check_answer(question, correct_answer, name):
            return
    congratulate_winner(name)
