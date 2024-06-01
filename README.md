<div align="center">
<h1>Игры разума</h1>
</div>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/zainutdinov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/zainutdinov/python-project-49/actions)

### CodeClimate Badges
[![Maintainability](https://api.codeclimate.com/v1/badges/ed9c40c9e61ca711284f/maintainability)](https://codeclimate.com/github/zainutdinov/python-project-49/maintainability)

## Описание проекта

**«Игры разума»** — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. 

Игры:
- Калькулятор. Арифметические выражения, которые необходимо вычислить
- Прогрессия. Поиск пропущенных чисел в последовательности чисел
- Определение четного числа
- Определение наибольшего общего делителя
- Определение простого числа

## Требования

- python ^3.12
- prompt ^0.4.1

## Инструкция по установке

#### Python

> Перед установкой пакета убедитесь, что у вас установлен Python версии 3.12 или выше:

```bash
python --version
# Python 3.12.0+
```
#### Poetry

> Проект использует менеджер зависимостей Poetry. Для установки Poetry используйте его [официальную инструкцию](https://python-poetry.org/docs/#installation).

### Установка пакета

> Чтобы использовать пакет, вам нужно скопировать репозиторий на свой компьютер. Это делается с помощью команды ``git clone``:

```bash
git clone https://github.com/zainutdinov/python-project-49
```

> Далее выполните установку пакета:

```bash
cd python-project-49
```

```bash
poetry build
python3 -m pip install --user dist/*.whl
```

## Запуск игр

### _Игра: «Проверка на чётность»_

Пользователю показывается случайное число. И ему нужно ответить **"yes"**, если число чётное, или **"no"** — если нечётное.

> Для запуска игры используйте команду:
```bash
brain-even
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/bFDDFg1wRgceKEBAJ8FGYf5UD.svg)](https://asciinema.org/a/bFDDFg1wRgceKEBAJ8FGYf5UD)

### _Игра: «Калькулятор»_

Пользователю показывается случайное математическое выражение, например, **35 + 16**, которое нужно вычислить и записать правильный ответ.

> Для запуска игры используйте команду:
```bash
brain-calc
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/CoeQDb8h0w737unzt67CgtUDV.svg)](https://asciinema.org/a/CoeQDb8h0w737unzt67CgtUDV)

### _Игра «НОД»_

Пользователю показывается два случайных числа, например, **25 50**. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

> Для запуска игры используйте команду:
```bash
brain-gcd
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/Swm48l3E3dhjgUghQX2pvjFre.svg)](https://asciinema.org/a/Swm48l3E3dhjgUghQX2pvjFre)

### _Игра «Арифметическая прогрессия»_

Пользователю показывается ряд чисел, который образует арифметическую прогрессию. Одно из чисел скрыто двумя точками. Игрок должен определить это число.

> Для запуска игры используйте команду:
```bash
brain-progression
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/v0GHDfq0lnnneuNam0YVneqot.svg)](https://asciinema.org/a/v0GHDfq0lnnneuNam0YVneqot)

### _Игра «Простое ли число?»_

Пользователю показывается случайное число. И ему нужно ответить **"yes"**, если число простое, или **"no"** — если составное.

> Для запуска игры используйте команду:
```bash
brain-prime
```

> Пример запуска игры:
[![asciicast](https://asciinema.org/a/LeJmFA1dZvJNrvKvkBztJmKS2.svg)](https://asciinema.org/a/LeJmFA1dZvJNrvKvkBztJmKS2)