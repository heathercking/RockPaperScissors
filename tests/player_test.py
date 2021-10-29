import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Smithy")
        self.player2 = Player("Kingy")

    def test_player_has_name(self):
        self.assertEqual("Smithy", self.player1.name)

    def test_assign_choice_to_player(self):
        self.player1.assign_choice_to_player("rock")
        self.assertEqual("rock", self.player1.choice)


