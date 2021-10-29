from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/rules')
def rules():
    return render_template('rules.html', title='Rules')

@app.route('/play')
def play():
    return render_template('play.html', title='Play')

@app.route('/result/<player1_choice>/<player2_choice>')
def play_game(player1_choice, player2_choice):
    game1 = Game("Rock Paper Scissors")
    player1 = Player("Player 1")
    player1.assign_choice_to_player(player1_choice)
    player2 = Player("Player 2")
    player2.assign_choice_to_player(player2_choice)
    result = game1.determine_winner(player1, player2)
    return render_template('result.html', title='Result', p1 = player1, p2 = player2, result = result)
