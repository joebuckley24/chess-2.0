import numpy as np
import re
from itertools import permutations

CASTLE = "[0Oo](?:-[0Oo]){1,2}"
CASTLE_REGEX = re.compile(CASTLE)
# groups: 0 check
CASTLE_CHECK = CASTLE + "([+#])?"
CASTLE_CHECK_REGEX = re.compile(CASTLE_CHECK)

# groups: 0 piece 1 disambiguation 2 capture 3 end
PIECE_MOVE = "([RNBQK])(?:(?<!K)([a-h]?[1-8]?))?(x?)([a-h][1-8])" 
PIECE_MOVE_REGEX = re.compile(PIECE_MOVE)
# groups: 0 piece 1 disambiguation 2 capture 3 end 4 check
PIECE_MOVE_CHECK = PIECE_MOVE + "([+#])?"
PIECE_MOVE_CHECK_REGEX = re.compile(PIECE_MOVE_CHECK)

# groups: 0 disambiguation 1 end 2 promotion
PAWN_MOVE = "([a-h]x?)?([a-h][1-8])(?:(?<=[18])(?:=?([RNBQ])))?"
PAWN_MOVE_REGEX = re.compile(PAWN_MOVE)
# groups: 0 disambiguation 1 end 2 promotion 3 check
PAWN_MOVE_CHECK = PAWN_MOVE + "([+#])?"
PAWN_MOVE_CHECK_REGEX = re.compile(PAWN_MOVE_CHECK)

# ALGEBRAIC_NOTATION_REGEX = re.compile("([KQRNB]?[a-h]?[1-8]?x?[a-h][1-8](\\=[QRNB])?|[O0]-[O0](-[O0])?)[+#]?")

PIECES_DICT = {
    (True, "K"): "\u2654",
    (True, "Q"): "\u2655",
    (True, "R"): "\u2656",
    (True, "B"): "\u2657",
    (True, "N"): "\u2658",
    (True, " "): "\u2659",
    (False, "K"): "\u265A",
    (False, "Q"): "\u265B",
    (False, "R"): "\u265C",
    (False, "B"): "\u265D",
    (False, "N"): "\u265E",
    (False, " "): "\u265F"
}

NEW_BOARD = np.array(
    [
        ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"],
        ["\u2659"]*8,
        [" "]*8, 
        [" "]*8, 
        [" "]*8, 
        [" "]*8,
        ["\u265F"]*8,
        ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"]
    ],
    dtype="U"
)
