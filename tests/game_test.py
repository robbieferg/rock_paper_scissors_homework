import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    
    def test_game_can_play(self):
        self.player_1 = Player("Player 1", "paper")
        self.player_2 = Player("Player 2", "scissors")
        self.game_1 = Game(self.player_1, self.player_2)

        expected = "The winner is Player 2!"
        actual = self.game_1.play_game()

        self.assertEqual(expected, actual)