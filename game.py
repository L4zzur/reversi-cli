import utils
from board import Board
from player import Player


class Statuses:
    CONTINUES = 0
    BLACK_WON = 1
    WHITE_WON = 2
    DRAW = 3

class Game:

    def __init__(self):
        self.board = Board()
        self.players = (Player(utils.PieceType.BLACK), Player(utils.PieceType.WHITE))
        self.board.start()
        self.current = 0
        self.board.markPossibleMoves(self.players[self.current])
        self.status = Statuses.CONTINUES
        self.prev_move_fail = False

    def getAmounts(self):
        '''Возвращает количество черных и белых фишек на доске'''
        blacks = len([piece for piece in self.board.pieces if piece.getState() == utils.PieceType.BLACK])
        whites = len([piece for piece in self.board.pieces if piece.getState() == utils.PieceType.WHITE])
        return blacks, whites

    def moveFailed(self):
        '''Выводит информацию о невозможности хода'''
        print('Нет возможных ходов!\nХод переходит другому игроку.')
        self.prev_move_fail = True

    def boardCoords(self, coords):
        '''Возвращает представление координаты в координатной сетке доски,
        например, (0, 0) в виде A0'''
        return f'{self.board.coords[coords[1]]}{coords[0]}'

    def isFinished(self):
        '''Обрабатывает конец игры и выводит победителя'''
        if self.blacks > self.whites:
            if self.players[0].getColor() == utils.PieceType.BLACK:
                self.status = Statuses.BLACK_WON
            else:
                self.status = Statuses.WHITE_WON
        elif self.blacks < self.whites:
            if self.players[0].getColor() == utils.PieceType.WHITE:
                self.status = Statuses.WHITE_WON
            else:
                self.status = Statuses.BLACK_WON
        else:
            self.status = Statuses.DRAW
    
    def nextMove(self):
        self.current = (self.current + 1) % 2

    def gameLoop(self):
        '''Основной игровой цикл'''
        while True:
            try:
                self.amountUpdate()
                move = self.players[self.current].move(self.board)
                self.board.makeMove(self.players[self.current], move)

            except utils.NoMoves:
                self.isFinished() if self.prev_move_fail else self.moveFailed()

            self.current = (self.current + 1) % 2
        
    def getState(self):
        '''Возвращает состояние игры''' 
        blacks, whites = self.getAmounts()
        return {
            'blacks': blacks,
            'whites': whites,
            'current': self.players[self.current].getColor(),
            'status': self.status
        }