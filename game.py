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

    def getAmounts(self):
        '''
        Возвращает количество черных и белых фишек на доске
        '''
        blacks = len([piece for piece in self.board.pieces if piece.getState() == utils.PieceType.BLACK])
        whites = len([piece for piece in self.board.pieces if piece.getState() == utils.PieceType.WHITE])
        return blacks, whites
    
    def getPossibleMoves(self):
        '''
        Возвращает список возможных ходов для текущего игрока
        '''
        return self.board.getPossibleMoves(self.players[self.current])

    def boardCoords(self, coords):
        '''
        Возвращает представление координаты в координатной сетке доски,
        например, (0, 0) в виде A0
        '''
        return f'{self.board.coords[coords[1]]}{coords[0]}'

    def setFinished(self):
        '''
        Обрабатывает конец игры и выводит победителя
        '''
        blacks, whites = self.getAmounts()
        if blacks > whites:
            self.status = Statuses.BLACK_WON
        elif blacks < whites:
            self.status = Statuses.WHITE_WON
        else:
            self.status = Statuses.DRAW
    
    def nextMove(self):
        '''
        Передача хода следующему игроку
        '''
        self.current = (self.current + 1) % 2
    
    def makeMove(self, pos):
        '''
        Совершение хода и передача его следующему игроку
        '''
        self.board.makeMove(self.players[self.current], self.players[self.current].checkMove(self.board, pos))
        self.nextMove()

    def getState(self):
        '''
        Возвращает состояние игры
        ''' 
        blacks, whites = self.getAmounts()
        return {
            'blacks': blacks,
            'whites': whites,
            'current': self.players[self.current].getColor(),
            'status': self.status
        }