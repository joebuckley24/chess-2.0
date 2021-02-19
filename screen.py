import numpy as np
# import re

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

if __name__ == "__main__":
    b = init_board()
    print(printable_board(b))
    while True:
        s = input("square from which piece should move (e.g. e2): ")
        if s == "q":
            break
        e = input("square to which piece should move (e.g. e4): ")
        if e == "q":
            break
        move_piece(b, s, e)
        print(printable_board(b))
