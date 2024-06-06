#!/usr/bin/env python3

from brain_games.general_logic import launch_game
from brain_games.games.game_prime_logic import create_prime_question
from brain_games.constants import TASK_PRIME


def main():
    launch_game(TASK_PRIME, create_prime_question)


if __name__ == '__main__':
    main()
