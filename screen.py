import numpy as np
import re

## add lookbehind for first set of digits and x, a number or x shouldn't be first character
CASTLE = "[0Oo](?:-[0Oo]){1,2}"
CASTLE_REGEX = re.compile(CASTLE)
# KING_MOVE = "K(x?)([a-h][1-8])" # 1.capture 2.end
PIECE_MOVE = "([RNBQK])(?:(?<!K)([a-h]?[1-8]?))?(x?)([a-h][1-8])" # 1.piece 2.disambiguation 3.capture 4.end
PAWN_MOVE = "([a-h]x?)?([a-h][1-8])(?<=[18])(?:=?([RNBQ]))" # 1.disambiguation 2.end 3.promotion
ALGEBRAIC_NOTATION_REGEX = re.compile("([KQRNB]?[a-h]?[1-8]?x?[a-h][1-8](\\=[QRNB])?|[O0]-[O0](-[O0])?)[+#]?")
PIECE_MOVE_REGEX = re.compile(PIECE_MOVE)
PAWN_MOVE_REGEX = re.compile(PAWN_MOVE)
## trim all whitespace
## make sure to add optional check/checkmate to all moves

def coord_to_index(coord_str):
    coord = list(coord_str)
    return (int(coord[1]) - 1, ord(coord[0].lower()) - 97)

def init_board():
    white_back_rank = ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"]
    white_pawns = ["\u2659"]*8
    black_back_rank = ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"]
    black_pawns = ["\u265F"]*8
    board = np.array([white_back_rank, 
                      white_pawns, 
                      [" "]*8, [" "]*8, [" "]*8, [" "]*8, 
                      black_pawns, 
                      black_back_rank], 
                     dtype="U")
    return board

def printable_board(board):
    printable = ["| " + " | ".join(row) + " |" for row in reversed(board)]
    return " " + "--- "*8 + "\n" + ("\n " + "--- "*8 + "\n").join(printable) + "\n " + "--- "*8

def move_piece(board, start_coord, end_coord):
    start, end = coord_to_index(start_coord), coord_to_index(end_coord)
    board[end] = board[start]
    board[start] = " "

def regex_loop():
    user_in = ""
    while True:
        user_in = input("Enter algebraic notation (or 'quit'): ")
        if user_in.lower() == "quit":
            print("Quitting")
            break
        if ALGEBRAIC_NOTATION_REGEX.match(user_in):
            print("match")
        else:
            print("invalid")

def regex_groups(compiled, notation_str):
    return compiled.match(notation_str).groups(default="")

def process(string_move):
    # if castle:
    #     castle_logic()
    # elif king_move:
    #     king_logic()
    # elif pawn_move:
    #     pawn_logic()
    # elif queen_move:
    #     queen_logic()
    # elif rook_move:
    #     rook_logic()
    # elif bishop_move:
    #     bishop_logic()
    # elif knight_move:
    #     knight_logic()
    pass

if __name__ == "__main__":
    # b = init_board()
    # print(printable_board(b))
    # while True:
    #     s = input("square from which piece should move (e.g. e2): ")
    #     if s == "q":
    #         break
    #     e = input("square to which piece should move (e.g. e4): ")
    #     if e == "q":
    #         break
    #     move_piece(b, s, e)
    #     print(printable_board(b))
    regex_loop()
