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
            self.apply_move()
            # self.board = apply self.move to self.position 
            # include update castle rights
            # include remove en passant capture
        self.legal_moves = []

    def legal_moves(self):
        pass
        # for each piece of color's turn
        # legal_move(board)

    def is_check(self):
        if self.last_move.color: # white is True, black is False
            enemies = ["\u2655", "\u2656", "\u2657", "\u2658", "\u2659"]
            king = "\u265A"
        else:
            enemies = ["\u265B", "\u265C", "\u265D", "\u265E", "\u265F"]
            king = "\u2654" 
        for i, j in zip(*np.where(np.isin(self.board, enemies))):
            if self.board[i, j] == "\u2659" or self.board[i, j] == "\u265F": # pawn
                for dj in [-1, 1]:
                    try:
                        if board[i+1 if self.last_move.color else i-1, j+dj] == king:
                            return True
                    except IndexError:
                        pass
            elif self.board[i, j] == "\u2658" or self.board[i, j] == "\u265E": # knight
                for di, dj in permutations([-2, -1, 1, 2], 2):
                    try: 
                        if board[i+di, j+dj] == king:
                            return True
                    except IndexError:
                        pass
            elif self.board[i, j] == "\u2657" or self.board[i, j] == "\u265D": # bishop
                while :
                    pass
            elif self.board[i, j] == "\u2657" or self.board[i, j] == "\u265D": # rook
                while :
                    pass
            elif self.board[i, j] == "\u2657" or self.board[i, j] == "\u265D": # queen
                while :
                    pass

        # 1. get the color from last_move
        # 2. locate those color's pieces on the board
        # 3. see if any of those color's pieces are attacking the king
        return False

        def is_check(self):
            # 1. get the color from last_move
            # 2. locate opposite king
            # 3. check all potential checking squares for opposing color pieces
            if self.last_move.color: # white just moved
                king_at = np.where(self.board == "\u265A") # find black king
                i, j = king_at[0].item(), king_at[1].item()
                for di in [-1, 1]:
                    try:
                        if self.board[i+di, j+1] == "\u2659":
                            return True
                    except IndexError:
                        pass
            else: # black just moved
                king_at = np.where(self.board == "\u2654") # find white king
                i, j = king_at[0].item(), king_at[1].item()
                for di in [-1, 1]:
                    try:
                        if self.board[i+di, j-1] == "\u265F":
                            return True
                    except IndexError:
                        pass
            for d in range(7): # distance away from king
                # pawn diagonal
                # other pawn diagonal
                # opposite diagonal
                # other opposite diagonal
                # north
                # east
                # south
                # west
                # knights

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
