import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    
    def test_game_has_winner(self):
        self.player_1 = Player("Player 1", "paper")
        self.player_2 = Player("Player 2", "scissors")
        self.game_1 = Game()

        expected = "Player 2"
        actual = self.game_1.play_game(self.player_1, self.player_2).name

        self.assertEqual(expected, actual)

    def test_game_is_draw(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "rock")
        self.game_2 = Game()

        expected = None
        actual = self.game_2.play_game(self.player_1, self.player_2)

    def test_generate_computer_player(self):
        game = Game()
        self.new_computer_player = game.generate_computer_player()
        self.assertEqual("The Computer", self.new_computer_player.name)
        self.assertEqual(True, self.new_computer_player.choice in ["rock", "paper", "scissors"])