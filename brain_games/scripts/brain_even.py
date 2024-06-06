#!/usr/bin/env python3

from brain_games.general_logic import launch_game
from brain_games.games.game_even_logic import create_even_question
from brain_games.constants import TASK_EVEN


def main():
    launch_game(TASK_EVEN, create_even_question)


if __name__ == '__main__':
    main()
