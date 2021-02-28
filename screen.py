from constants import *

def coord_to_index(coord_str):
    coord = list(coord_str)
    return (int(coord[1]) - 1, ord(coord[0].lower()) - 97)

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

def get_starting_squares(board, color, piece_char):
    unicode_piece_char = PIECES_DICT[color, piece_char]
    return np.where(board == unicode_piece_char)

def check_legal_move(board, color, move):
    i, j = get_starting_squares()

if __name__ == "__main__":
    b = NEW_BOARD
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
            elif user_in == "q" or user_in == "quit" or user_in == "exit":
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
