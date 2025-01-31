import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board_setup(self):
        expected_board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'W', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.assertEqual(self.board.get_board(), expected_board)

    def test_valid_move(self):
        self.board.make_move(2, 3, 'B')
        self.assertEqual(self.board.get_board()[2][3], 'B')

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            self.board.make_move(0, 0, 'B')

    def test_winner(self):
        self.board.make_move(2, 3, 'B')
        self.board.make_move(3, 2, 'W')
        self.assertEqual(self.board.get_winner(), None)  # Assuming no winner yet

if __name__ == '__main__':
    unittest.main()