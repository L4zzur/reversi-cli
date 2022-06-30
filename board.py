import utils
from piece import Piece

class Board():

    def __init__(self):
        self.n = 8
        self.center = self.n // 2
        self.coords = [chr(i) for i in range(ord('A'), ord('Z')+1)][0:self.n]
        
        self.pieces = [ # одномерный список фишек
            Piece(x, y)
            for x in range(0, self.n)
            for y in range(0, self.n)
        ]
    
    def asList(self):
        '''Возвращает список состояний доски'''
        return [piece.getState() for piece in self.pieces]

    def start(self):
        '''
        Подготавливает доску к началу игры,
        расставляет в центре доски 4 фишки: 2 белые и 2 черные
        '''
        self.pieces[(self.n * (self.center - 1)) + self.center - 1].setWhite()
        self.pieces[(self.n * (self.center - 1)) + self.center].setBlack()
        self.pieces[(self.n * self.center) + self.center - 1].setBlack()
        self.pieces[(self.n * self.center) + self.center].setWhite()

    def markPossibleMove(self, player, piece, direction):
        '''
        Отмечает возможной ход от текущей фишки в заданном
        направлении статусом MOVE
        '''
        x, y = piece.getCoords()
        opponent_color = player.getOpponentColor()

        if utils.out_of_bounds((x * self.n) + y, direction):
            return

        block = (x * self.n) + y + direction

        if self.pieces[block].getState() == opponent_color:
            while self.pieces[block].getState() == opponent_color:
                if utils.out_of_bounds(block, direction):
                    break
                else:
                    block += direction

            if self.pieces[block].getState() == utils.PieceType.BOARD:
                self.pieces[block].setMove()


    def markPossibleMoves(self, player):
        '''
        Отмечает все возможные ходы для текущего игрока статусом MOVE
        '''
        for piece in self.pieces:
            for direction in utils.DIRECTIONS:
                if piece.getState() == player.getColor():
                    self.markPossibleMove(player, piece, direction)

    def clearMoves(self):
        '''Очищает поле от ячеек со статусом MOVE'''
        [piece.setBoard() for piece in self.pieces if piece.getState() == utils.PieceType.MOVE]

    def getPossibleMoves(self, player):
        '''Возвращает список возможных ходов для текущего игрока'''
        self.markPossibleMoves(player)
        moves = [piece for piece in self.pieces if piece.getState() == utils.PieceType.MOVE]
        self.clearMoves()
        return moves

    def makeMove(self, player, coordinates):
        '''Обрабатывает введённый шаг игрока и совершает его'''
        moves = [piece.getCoords() for piece in self.getPossibleMoves(player)]
        if coordinates not in moves:
            raise Exception('Совершён неверный ход. Попробуйте ещё раз.')

        move = coordinates[0] * self.n + coordinates[1]

        piece = self.pieces[move]
        if player.getColor() == utils.PieceType.BLACK:
            piece.setBlack()
        else:
            piece.setWhite()

        for direction in utils.DIRECTIONS:
            if utils.out_of_bounds(move, direction):
                continue

            cursor = move + direction

            flip_pieces = []

            while self.pieces[cursor].getState() != utils.PieceType.BOARD:
                if self.pieces[cursor].getState() == player.getColor() or utils.out_of_bounds(cursor, direction):
                    break
                else:
                    flip_pieces.append(self.pieces[cursor])
                    cursor += direction

            if self.pieces[cursor].getState() == player.getColor():
                for piece in flip_pieces:
                    if player.getColor() == utils.PieceType.BLACK:
                        piece.setBlack()
                    else:
                        piece.setWhite()
