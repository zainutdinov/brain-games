#!/usr/bin/env python3

from brain_games.general_logic import launch_game
from brain_games.games.game_progression_logic import create_progression_question
from brain_games.constants import TASK_PROGRESSION


def main():
    launch_game(TASK_PROGRESSION, create_progression_question)


if __name__ == '__main__':
    main()
