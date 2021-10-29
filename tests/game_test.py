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

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__draw__rock(self):
        self.player1.assign_choice_to_player("rock")
        self.player2.assign_choice_to_player("rock")
        self.assertEqual(None, self.game1.determine_winner(self.player1, self.player2))
    
    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__draw__paper(self):
        self.player1.assign_choice_to_player("paper")
        self.player2.assign_choice_to_player("paper")
        self.assertEqual(None, self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__draw__scissors(self):
        self.player1.assign_choice_to_player("scissors")
        self.player2.assign_choice_to_player("scissors")
        self.assertEqual(None, self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player1_wins__with_rock(self):
        self.player1.assign_choice_to_player("rock")
        self.player2.assign_choice_to_player("scissors")
        self.assertEqual("Player 1", self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player1_wins__with_paper(self):
        self.player1.assign_choice_to_player("paper")
        self.player2.assign_choice_to_player("rock")
        self.assertEqual("Player 1", self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player1_wins__with_scissors(self):
        self.player1.assign_choice_to_player("scissors")
        self.player2.assign_choice_to_player("paper")
        self.assertEqual("Player 1", self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player2_wins__with_rock(self):
        self.player1.assign_choice_to_player("scissors")
        self.player2.assign_choice_to_player("rock")
        self.assertEqual("Player 2", self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player2_wins__with_paper(self):
        self.player1.assign_choice_to_player("rock")
        self.player2.assign_choice_to_player("paper")
        self.assertEqual("Player 2", self.game1.determine_winner(self.player1, self.player2))

    @unittest.skip("delete this line to run the test")
    def test_game_returns_correct_winner__player2_wins__with_scissors(self):
        self.player1.assign_choice_to_player("paper")
        self.player2.assign_choice_to_player("scissors")
        self.assertEqual("Player 2", self.game1.determine_winner(self.player1, self.player2))
    


    