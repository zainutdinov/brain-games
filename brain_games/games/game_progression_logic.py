import random


def generate_progression():
    progression = []
    finish_progression = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    element = random.randint(1, 10)
    progression.append(str(element))
    for _ in range(finish_progression + 1):
        element += progression_step
        progression.append(str(element))
    return progression


def create_progression_question():
    progression = generate_progression()
    hidden_element_id = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_element_id]
    progression[hidden_element_id] = '..'
    question = ' '.join(progression)
    return question, correct_answer
