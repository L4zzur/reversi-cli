from settings import PieceType, color_string


class Piece():
    '''Класс, отвечающий за сущность каждой ячейки на доске'''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.state = PieceType.BOARD    # состояние ячейки
        self.color = color
        self.drawings = {
            PieceType.BOARD: self.drawBoard,
            PieceType.BLACK: self.drawBlack,
            PieceType.WHITE: self.drawWhite,
            PieceType.MOVE: self.drawMove
        }

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

    def draw(self):
        '''Возвращает строковое представление текущей ячейки для печати'''
        return self.drawings[self.state]()

    def drawWhite(self):
        '''Возвращает строковое представление ячейки в состоянии WHITE для печати'''
        if self.color:
            return color_string('  ', bg='255;255;255')
        else:
            return self.state + ' '

    def drawBlack(self):
        '''Возвращает строковое представление ячейки в состоянии BLACK для печати'''
        if self.color:
            return color_string('  ', bg='0;0;0')
        else:
            return self.state + ' '

    def drawBoard(self):
        '''Возвращает строковое представление ячейки в состоянии BOARD для печати'''
        if self.color:
            return color_string('  ', bg='78;154;6')
        else:
            return self.state + ' '

    def drawMove(self):
        '''Возвращает строковое представление ячейки в состоянии MOVE для печати'''
        if self.color:
            return color_string('><', fg='204;0;0', bg='78;154;6')
        else:
            return self.state + ' '

    def __repr__(self):
        '''Возвращает информацию о ячейки при попытке печати'''
        return f'{self.state} piece on ({self.x}, {self.y})'
