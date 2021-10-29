from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return "Welcome to Rock Paper Scissors!"

@app.route('/<player1_choice>/<player2_choice>')
def play_game(player1_choice, player2_choice):
    game1 = Game("Rock Paper Scissors")
    player1 = Player("Player 1")
    player1.assign_choice_to_player(player1_choice)
    player2 = Player("Player 2")
    player2.assign_choice_to_player(player2_choice)
    return f'{game1.determine_winner(player1, player2)}'
