from constants import *

class Position:

	def __init__(self, last_position=None, last_move=None):
		self.previous = last_position
		self.last_move = last_move
		if not self.previous and not self.move:
			self.board = NEW_BOARD
			self.white_short_castle_rights = True
			self.white_long_castle_rights = True
			self.black_short_castle_rights = True
			self.black_long_castle_rights = True
		else:
			self.white_short_castle_rights = self.previous.white_short_castle_rights
			self.white_long_castle_rights = self.previous.white_long_castle_rights
			self.black_short_castle_rights = self.previous.black_short_castle_rights
			self.black_long_castle_rights = self.previous.black_long_castle_rights
			# self.board = apply self.move to self.position 
			# include update castle rights
			# include remove en passant capture
		self.legal_moves() = []

	def legal_moves(self):
		pass
		# for each piece of color's turn
		# legal_move(board)

	def is_check(self):
		pass

	def is_checkmate(self):
		pass

	def is_stalemate(self):
		pass

class Move:
	
	def __init__(self, color, piece, starting_square, ending_square, promotion, castle):
		self.color = color
		self.piece = piece
		self.starting_square = starting_square
		self.ending_square = ending_square
		self.promotion = promotion # None or the piece promoting to
		self.castle = castle # boolean
