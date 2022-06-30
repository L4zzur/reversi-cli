import random
from utils import PieceType
from reversi_cli import exceptions

class Player():
	
	def __init__(self, color):
		self.color = color

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

	def checkMove(self, board, pos):
		move = (int(pos[0]), int(pos[1]))
		possible_moves = [piece.getCoords() for piece in board.getPossibleMoves(self)]

		if not possible_moves:
			raise exceptions.NoMoves
		if move not in possible_moves:
			raise exceptions.WrongMove

		return move