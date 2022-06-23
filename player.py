import random
from settings import WIDTH, PieceType, COLORS, NoMoves, WrongMove


class Player():
    '''Класс, отвечающий за сущность игрока и его действия'''
    def __init__(self, number):
        self.number = number
        self.color = PieceType.BLACK if number == 1 else PieceType.WHITE
        self.remaining = 30

    def getRemaining(self):
        '''Возвращает количество оставшихся фишек'''
        return self.remaining

    def dropPiece(self):
        '''Уменьшает количество оставшихся фишек после хода текущего игрока'''
        self.remaining -= 1

    def getSide(self):
        '''Возвращает полное название цвета фишек текущего игрока'''
        return COLORS[self.color]

    def getColor(self):
        '''Возвращает цвет фишек текущего игрока'''
        return self.color

    def getOpponentColor(self):
        '''Возвращает цвет фишек оппонента текущего игрока'''
        if self.color == PieceType.WHITE:
            return PieceType.BLACK
        elif self.color == PieceType.BLACK:
            return PieceType.WHITE
        else:
            raise ValueError


class Human(Player):
    '''Класс-наследник игрока для реального человека'''
    def __init__(self, number):
        super().__init__(number)
        self.name = 'Human'

    def currentMove(self, board):
        move = None
        while move is None:
            selected = input('Введите координату Вашего хода, например, A0: ')
            try:
                if selected != selected[0] not in board.coords and selected[1] not in range(WIDTH):
                    raise ValueError

                x, y = int(selected[1]), board.coords.index(selected[0])
                move = (x, y)
                possible_moves = [piece.getCoords() for piece in board.getPossibleMoves(self)]

                if not possible_moves:
                    raise NoMoves
                print(move in possible_moves)
                if move not in possible_moves:
                    raise WrongMove

            except (ValueError, WrongMove):
                move = None
                print('Неверный ход. Попробуйте ещё раз.')

        return move


class Random(Player):
    '''Создаёт игрока-бота, выполняющего случайные ходы'''
    def __init__(self, number):
        super().__init__(number)
        self.name = 'Random'

    def currentMove(self, board):
        move = None
        while move is None:
            try:
                possible_moves = [piece.getCoords() for piece in board.getPossibleMoves(self)]

                if not possible_moves:
                    raise NoMoves

                move = random.choice(possible_moves)

                if move not in possible_moves:
                    raise WrongMove

            except (ValueError, WrongMove):
                move = None
                print('Неверный ход. Попробуйте ещё раз.')

        return move
