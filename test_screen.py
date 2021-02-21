import unittest
import screen

class TestScreen(unittest.TestCase):

    def test_regex(self):
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Ke4"), 
                         ("K", "", "", "e4"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qf6"), 
                         ("Q", "", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qxf6"), 
                         ("Q", "", "x", "f6"))
        # pawn promoted at some point; one queen on a1, one queen on f3
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qaf6"), 
                         ("Q", "a", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qaxf6"), 
                         ("Q", "a", "x", "f6"))
        # pawn promoted at some point; one queen on f3, one queen on f7
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Q3f6"), 
                         ("Q", "3", "", "f6"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Q3xf6"), 
                         ("Q", "3", "x", "f6"))
        # pawns promoted at some point; one queen on a1, one queen on e1, one queen on e5
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qe5c3"), 
                         ("Q", "e5", "", "c3"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Qe5xc3"), 
                         ("Q", "e5", "x", "c3"))
        # king shouldn't need disambiguation
        # no regex match causes AttributeError: 'NoneType' object has no attribute 'groups'
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "K5c7")
        # bishop going off board
        with self.assertRaises(AttributeError):
            screen.regex_groups(screen.PIECE_MOVE_REGEX, "Bc9")

        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Ba2"), 
                         ("B", "", "", "a2"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Nc3"), 
                         ("N", "", "", "c3"))
        self.assertEqual(screen.regex_groups(screen.PIECE_MOVE_REGEX, "Rxh8"), 
                         ("R", "", "x", "h8"))


        self.assertEqual(screen.regex_groups(screen.PAWN_MOVE_REGEX, "a2"), 
                         ("", "", "a2"))

if __name__ == "__main__":
    unittest.main()