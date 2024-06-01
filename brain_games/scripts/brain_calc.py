#!/usr/bin/env python3

from brain_games.constants import COUNT_ROUND
from brain_games.general_logic import launching_the_game
from brain_games.games.brain_calc_logic import task
from brain_games.games.brain_calc_logic import game_logic_calc


def main():
    launching_the_game(task, COUNT_ROUND, game_logic_calc)


if __name__ == '__main__':
    main()
