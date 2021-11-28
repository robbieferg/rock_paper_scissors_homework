from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route("/")
def welcome():
    return render_template("welcome.html", title = "Welcome")

@app.route("/<player_1_choice>/<player_2_choice>/")
def display_result(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game_1 = Game()
    winner = game_1.play_game(player_1, player_2)
    return render_template("result.html", title = "Result", winner = winner, player_1 = player_1, player_2 = player_2)

@app.route("/play/")
def play():
    return render_template("play.html", title = "play")

@app.route("/play/", methods = ["POST"])
def play_computer_result():
    new_game = Game()
    player_1 = Player(request.form["name"], request.form["choice"])
    player_2 = new_game.generate_computer_player
    winner = new_game.play_game(player_1, player_2)
    return render_template("result.html", title = "Result", winner = winner, player_1 = player_1, player_2 = player_2)