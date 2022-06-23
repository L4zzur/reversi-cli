from settings import *
from piece import Piece
from player import Player


class Board():
    '''Класс, отвечающий за доску и действия с ней'''
    def __init__(self, color=False):
        self.n = WIDTH
        self.center = self.n // 2
        self.coords = [chr(i) for i in range(ord('A'), ord('Z')+1)][0:WIDTH]
        self.pieces = [                             # одномерный список фишек
                        Piece(x, y, color)
                        for x in range(0, self.n)
                        for y in range(0, self.n)
                    ]

    def draw(self):
        '''Отрисовывает (выводит в консоль) текущее состояние доски '''
        brd = '  A B C D E F G H\n'
        for i, row in enumerate(chunks(self.pieces, 8)):
            brd += str(i) + ' '
            for piece in row:
                brd += piece.draw()
            brd += '\n'
        print(brd)

    def start(self):
        '''Подготавливает доску к началу игры, \
        расставляет в центре доски 4 фишки: 2 белые и 2 черные'''
        self.pieces[(self.n * (self.center - 1)) + self.center - 1].setWhite()
        self.pieces[(self.n * (self.center - 1)) + self.center].setBlack()
        self.pieces[(self.n * self.center) + self.center - 1].setBlack()
        self.pieces[(self.n * self.center) + self.center].setWhite()

    def markPossibleMove(self, Player, piece, direction):
        '''Отмечает возможной ход от текущей фишки в заданном \
        направлении статусом MOVE'''
        x, y = piece.getCoords()
        opponent_color = Player.getOpponentColor()

        if out_of_bounds((x * WIDTH) + y, direction):
            return

        block = (x * WIDTH) + y + direction

        if self.pieces[block].getState() == opponent_color:
            while self.pieces[block].getState() == opponent_color:
                if out_of_bounds(block, direction):
                    break
                else:
                    block += direction

            if self.pieces[block].getState() == PieceType.BOARD:
                self.pieces[block].setMove()

    def markPossibleMoves(self, Player):
        '''Отмечает все возможные ходы для текущего игрока статусом MOVE'''
        [
            self.markPossibleMove(Player, piece, direction)
            for piece in self.pieces
            for direction in DIRECTIONS
            if piece.getState() == Player.getColor()
        ]

    def clearMoves(self):
        '''Очищает поле от ячеек со статусом MOVE'''
        [piece.setBoard() for piece in self.pieces if piece.getState() == PieceType.MOVE]

    def getPossibleMoves(self, Player):
        '''Возвращает список возможных ходов для текущего игрока'''
        self.markPossibleMoves(Player)
        moves = [piece for piece in self.pieces if piece.getState() == PieceType.MOVE]
        self.clearMoves()
        return moves

    def makeMove(self, Player, coordinates):
        '''Обрабатывает введённый шаг игрока и совершает его'''
        moves = [piece.getCoords() for piece in self.getPossibleMoves(Player)]
        if coordinates not in moves:
            raise Exception('Совершён неверный ход. Попробуйте ещё раз.')

        move = coordinates[0] * WIDTH + coordinates[1]

        piece = self.pieces[move]
        if Player.getColor() == PieceType.BLACK:
            piece.setBlack()
        else:
            piece.setWhite()

        Player.dropPiece()

        for direction in DIRECTIONS:
            if out_of_bounds(move, direction):
                continue

            cursor = move + direction

            flip_pieces = []

            while self.pieces[cursor].getState() != PieceType.BOARD:
                if self.pieces[cursor].getState() == Player.getColor() or out_of_bounds(cursor, direction):
                    break
                else:
                    flip_pieces.append(self.pieces[cursor])
                    cursor += direction

            if self.pieces[cursor].getState() == Player.getColor():
                for piece in flip_pieces:
                    if Player.getColor() == PieceType.BLACK:
                        piece.setBlack()
                    else:
                        piece.setWhite()
