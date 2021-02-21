import re

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

# MOVES_DICT = {
#   ("w", "K"): "\u2654",
#   ("w", "Q"): "\u2655",
#   ("w", "R"): "\u2656",
#   ("w", "B"): "\u2657",
#   ("w", "N"): "\u2658",
#   ("w", ""): "\u2659",
# }