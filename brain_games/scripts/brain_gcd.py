#!/usr/bin/env python3

from brain_games.general_logic import launch_game
from brain_games.games.game_gcd_logic import create_gcd_question
from brain_games.constants import TASK_GCD


def main():
    launch_game(TASK_GCD, create_gcd_question)


if __name__ == '__main__':
    main()
