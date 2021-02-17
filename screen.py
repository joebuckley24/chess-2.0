import numpy as np

def coord_to_board_index(coord_str):
    coord = list(coord_str)
    return (ord(coord[0].lower()) - 97, int(coord[1]) - 1)

def init_board():
    white_back_rank = ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"]
    white_pawns = ["\u2659"]*8
    black_back_rank = ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"]
    black_pawns = ["\u265F"]*8
    lists = [white_back_rank, white_pawns, [" "]*8, [" "]*8, [" "]*8, [" "]*8, black_pawns, black_back_rank]
    print(lists)
    board = np.array(lists, dtype="U")
    print(board)
    return board

def main():
    pass

if __name__ == "__main__":
    main()
