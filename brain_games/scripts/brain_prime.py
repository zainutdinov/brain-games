#!/usr/bin/env python3

from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game
from brain_games.games.brain_prime_logic import task
import brain_games.games.brain_prime_logic


def main():
    launching_the_game(task, COUNT_ROUND, brain_games.games.brain_prime_logic)


if __name__ == '__main__':
    main()
