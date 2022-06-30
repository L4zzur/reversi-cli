import os
import platform
import time
from settings import *
from board import Board
from player import Human, Random


class Game():
    '''Основной объект игры, создающий игроков и доску с фишками на ней'''
    def __init__(self, players=[Human(1), Random(2)], color=False, sleep=0):
        self.board = Board(color)
        self.players = players
        #self.show_moves = show_moves
        self.board.start()
        self.board.markPossibleMoves(players[0])
        self.blacks = 2
        self.whites = 2
        self.clear = 'cls' if platform.system() == 'Windows' else 'clear'
        self.prev_move_fail = False
        self.sleep = sleep

    def amountUpdate(self):
        '''Обновляет количество черных и белых фишек на доске'''
        self.blacks = len([piece for piece in self.board.pieces if piece.getState() == PieceType.BLACK])
        self.whites = len([piece for piece in self.board.pieces if piece.getState() == PieceType.WHITE])

    def moveFailed(self):
        '''Выводит информацию о невозможности хода'''
        print('Нет возможных ходов!\nХод переходит другому игроку.')
        time.sleep(1.5)
        self.prev_move_fail = True

    def boardCoords(self, coords):
        '''Возвращает представление координаты в координатной сетке доски,
        например, (0, 0) в виде A0'''
        return f'{self.board.coords[coords[1]]}{coords[0]}'

    def showBoard(self):
        '''Выводит доску с возможными ходами для текущего игрока'''
        self.board.markPossibleMoves(self.players[0])
        self.board.draw()

    def showInfo(self):
        '''Выводит информацию на момент текущего хода'''
        print(f'Текущий ход: {self.players[0].getSide()}')
        print(f'Осталось фишек: {self.players[0].getRemaining()}')
        print(f'Количество черных фишек на поле: {self.blacks}')
        print(f'Количество белых фишек на поле: {self.whites}')

    def showMoves(self):
        '''Выводит возможные ходы для текущего игрока в текстовом формате'''
        print(f'Возможные ходы: {[self.boardCoords(piece.getCoords()) for piece in self.board.getPossibleMoves(self.players[0])]}')

    def gameFinished(self):
        '''Обрабатывает конец игры и выводит победителя'''
        if self.blacks > self.whites:
            if self.players[0].getColor() == PieceType.BLACK:
                winner = self.players[0]
            else:
                winner = self.players[1]
            print(f'Игрок {winner.name}, играющий за черных победил!')
        elif self.blacks < self.whites:
            if self.players[0].getColor() == PieceType.WHITE:
                winner = self.players[0]
            else:
                winner = self.players[1]
            print(f'Игрок {winner.name}, играющий за белых победил!')
        else:
            print(f'Между игроками {self.players[0]} и {self.players[1]} ничья!')
        exit()

    def gameLoop(self):
        '''Основной игровой цикл'''
        while True:
            try:
                os.system(self.clear)
                self.amountUpdate()
                self.showInfo()
                self.showBoard()

                self.showMoves()
                move = self.players[0].currentMove(self.board)
                self.board.makeMove(self.players[0], move)
                time.sleep(self.sleep)

            except NoMoves:
                self.gameFinished() if self.prev_move_fail else self.moveFailed()

            self.players.reverse()
