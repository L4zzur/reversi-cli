import argparse
from time import sleep
from game import Game
from player import Human, Random

def main():
    parser = argparse.ArgumentParser(description='Игра Отелло/Реверси против другого человека или бота.')
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--color', action="store_true", help='Включает цветной режим игры')
    parser.add_argument('--sleep', default=0, type=float, help='Задаёт время паузы между ходами игроков')
    group.add_argument('--human', action="store_true", help='Запускает игру с другим человеком')
    group.add_argument('--random', action="store_true", help='Запускает игру с ботом-рандомизатором')
    group.add_argument('--test', action="store_true", help='Запускает игру с двумя ботами-рандомизаторами')

    args = parser.parse_args()

    players = None
    if args.human:
        players = [Human(1), Human(2)]
    elif args.random:
        players = [Human(1), Random(2)]
    elif args.test:
        players = [Random(1), Random(2)]
    
    if players is None:
        players = [Random(1), Random(2)]
    
    game = Game(players=players, color=args.color, sleep=args.sleep)

    game.gameLoop()

if __name__ == '__main__':
    main()