import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Smithy")
        self.player2 = Player("Kingy")

    

