from reversi_cli.utils import PieceType

class Piece():
    '''Класс, отвечающий за сущность каждой ячейки на доске'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = PieceType.BOARD    # состояние ячейки

    def getState(self):
        '''Возвращает состояние текущей ячейки'''
        return self.state

    def setWhite(self):
        '''Устанавливает состояние текущей ячейки на WHITE'''
        self.state = PieceType.WHITE

    def setBlack(self):
        '''Устанавливает состояние текущей ячейки на BLACK'''
        self.state = PieceType.BLACK

    def setMove(self):
        '''Устанавливает состояние текущей ячейки на MOVE '''
        self.state = PieceType.MOVE

    def setBoard(self):
        '''Устанавливает состояние текущей ячейки на WHITE'''
        self.state = PieceType.BOARD

    def flip(self):
        '''Меняет состояние текущей ячейки на противоположное
        BLACK <--> WHITE'''
        if self.state == PieceType.BLACK:
            self.state = PieceType.WHITE
        elif self.state == PieceType.WHITE:
            self.state = PieceType.BLACK

    def getCoords(self):
        '''Возвращает координаты позиции текущей ячейки'''
        return self.x, self.y

    def __repr__(self):
        '''Возвращает информацию о ячейки при попытке печати'''
        return f'{self.state} piece on ({self.x}, {self.y})'
