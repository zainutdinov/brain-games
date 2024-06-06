#!/usr/bin/env python3

from brain_games.general_logic import launch_game
from brain_games.games.game_calc_logic import create_calc_question
from brain_games.constants import TASK_CALC


def main():
    launch_game(TASK_CALC, create_calc_question)


if __name__ == '__main__':
    main()
