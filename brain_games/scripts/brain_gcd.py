#!/usr/bin/env python3

from brain_games.games import brain_gcd
from brain_games.scripts import engine


def main():
    engine.run(brain_gcd)


if __name__ == '__main__':
    main()
