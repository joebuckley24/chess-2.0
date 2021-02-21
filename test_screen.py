import unittest
import screen

class TestScreen(unittest.TestCase):

    def test_piece_regex(self):
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Ke4"), ("K", "", "", "e4"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qf6"), ("Q", "", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qxf6"), ("Q", "", "x", "f6"))
        # pawn promoted at some point; one queen on a1, one queen on f3
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qaf6"), ("Q", "a", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qaxf6"), ("Q", "a", "x", "f6"))
        # pawn promoted at some point; one queen on f3, one queen on f7
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Q3f6"), ("Q", "3", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Q3xf6"), ("Q", "3", "x", "f6"))
        # pawns promoted at some point; one queen on a1, one queen on e1, one queen on e5
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qe5c3"), ("Q", "e5", "", "c3"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qe5xc3"), ("Q", "e5", "x", "c3"))
        # king shouldn't need disambiguation
        # no regex match causes AttributeError: 'NoneType' object has no attribute 'groups'
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "K5c7")
        # bishop going off board
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "Bc9")

        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Ba2"), ("B", "", "", "a2"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Nc3"), ("N", "", "", "c3"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Rxh8"), ("R", "", "x", "h8"))
        # can't have spaces in middle
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "B c8")
        # with self.assertRaises(AttributeError):
        #     screen.regex_groups(screen.PIECE_MOVE_REGEX, " Bc8")
        # with self.assertRaises(AttributeError):
        #     screen.regex_groups(screen.PIECE_MOVE_REGEX, "Bc8 ")

    def test_pawn_regex(self):
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "a2"), ("", "a2", ""))
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "h7"), ("", "h7", ""))
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "e4"), ("", "e4", ""))
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "ed3"), ("e", "d3", ""))
        # test promotion
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "d1Q"), ("", "d1", "Q"))
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "d1=Q"), ("", "d1", "Q"))
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "cxd1=N"), ("cx", "d1", "N"))
        # can't promote to king
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "d2=K")
        # can't capture over two squares, unfortunately should still work -- catch later
        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "ec5"), ("e", "c5", ""))

        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "d2=Q")
        # can't have spaces in middle
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "cxd1= N")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "cxd1 =N")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "cxd 1=N")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "cx d 1=N")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "c xd1=N")

    def test_castle_regex(self):
        # same symbol
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "o-o"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "o-o-o"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "0-0"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "0-0-0"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "O-O"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "O-O-O"), ())
        # mixing symbols
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "O-o"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "o-0-o"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "0-o"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "0-0-O"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "O-0"), ())
        self.assertEqual(screen.regex_groups(screen.CASTLE_REGEX, "o-O-O"), ())
        # can't have spaces in middle
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "o-O- O")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "o -O-O")
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "o- O- O")


if __name__ == "__main__":
    unittest.main()