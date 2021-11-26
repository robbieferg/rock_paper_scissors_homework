from flask import render_template
from app import app
from models.game import Game
from models.player import Player


@app.route("/<player_1_choice>/<player_2_choice>/")
def display_result(player_1_choice, player_2_choice):
    player_1 = Player("Player 1, player_1_choice")
    player_2 = Player("Player 2", player_2_choice)
    game_1 = Game(player_1, player_2)
    winner = game_1.play_game()
    return render_template("result", title = "Result", winner = winner)