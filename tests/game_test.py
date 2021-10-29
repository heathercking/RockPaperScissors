import unittest


import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Smithy")
        self.player2 = Player("Kingy")
        self.game1 = Game(self.player1, self.player2)

    def test_game_has_player1(self):
        self.assertEqual("Smithy", self.game1.player1.name)
    
    def test_game_has_player2(self):
        self.assertEqual("Kingy", self.game1.player2.name)
    
