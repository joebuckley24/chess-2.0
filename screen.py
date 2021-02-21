import numpy as np
from constants import *

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

def get_move(trimmed_input):
    # return groups: 0 piece 1 disambiguation 2 capture 3 end 4 promotion 5 check
    if m := PAWN_MOVE_CHECK_REGEX.match(trimmed_input):
        # groups: 0 disambiguation 1 end 2 promotion 3 check
        if m[0] == "":
            return ("", "", "", m[1], m[2], m[3])
        return ("", m[0][0], "x", m[1], m[2], m[3])
    elif m := PIECE_MOVE_CHECK_REGEX.match(trimmed_input):
        # groups: 0 piece 1 disambiguation 2 capture 3 end 4 check
        return (m[0], m[1], m[2], m[3], "", m[4])
    elif m := CASTLE_CHECK_REGEX.match(trimmed_input):
        # groups: 0 check
        if len(m.string) == 3:
            return ("0-0", "", "", "", "", m[0])
        return ("0-0-0", "", "", "", "", m[0])
    raise ValueError("malformed algebraic notation")


if __name__ == "__main__":
    b = init_board()
    print(printable_board(b))
    white = True
    game = True
    while game:
        user_in = input("Enter a move in algebraic notation, " 
                        + "white" if white else "black"
                        + " to play (h for help, q to quit): ").strip()
        try:
            move = get_move(user_in)
            # move_board(move)
            white = not white
        except ValueError as ve:
            user_in = user_in.lower
            if user_in == "h" or user_in == "help":
                call_help()
            if m == "q" or m == "quit" or m == "exit":
                game = not game
    print("Thanks for playing!")

    # while True:
    #     s = input("square from which piece should move (e.g. e2): ")
    #     if s == "q":
    #         break
    #     e = input("square to which piece should move (e.g. e4): ")
    #     if e == "q":
    #         break
    #     move_piece(b, s, e)
    #     print(printable_board(b))
    # regex_loop()
