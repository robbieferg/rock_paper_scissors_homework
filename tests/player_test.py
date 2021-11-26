import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Barry", "scissors")
        
    def test_player_has_attributes(self):
        self.assertEqual("Barry", self.player_1.name)
        self.assertEqual("scissors", self.player_1.choice)