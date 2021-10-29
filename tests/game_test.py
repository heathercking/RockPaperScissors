import unittest


import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Smithy")
        self.player2 = Player("Kingy")
        self.game1 = Game("Rock Paper Scissors")

    # def test_game_has_player1(self):
    #     self.assertEqual("Smithy", self.game1.player1.name)
    
    # def test_game_has_player2(self):
    #     self.assertEqual("Kingy", self.game1.player2.name)

    def test_game_has_name(self):
        self.assertEqual("Rock Paper Scissors", self.game1.name)

    
    def test_game_compares_player_choices_and_returns_winner__rock_beats_scissors(self):
        self.player1.assign_choice_to_player("rock")
        self.player2.assign_choice_to_player("scissors")
        self.assertEqual(self.player1, self.game1.determine_winner(self.player1, self.player2))