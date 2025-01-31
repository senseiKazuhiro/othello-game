import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertEqual(self.game.current_turn, 'black')
        self.assertEqual(len(self.game.board.get_valid_moves('black')), 4)

    def test_player_turn(self):
        self.game.play_move(2, 3)  # Example move
        self.assertEqual(self.game.current_turn, 'white')

    def test_valid_move(self):
        valid_moves = self.game.board.get_valid_moves('black')
        self.assertIn((2, 3), valid_moves)

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            self.game.play_move(0, 0)  # Invalid move

    def test_game_over(self):
        # Simulate a game over scenario
        self.game.play_move(2, 3)
        self.game.play_move(3, 2)
        # Add more moves to reach game over
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()