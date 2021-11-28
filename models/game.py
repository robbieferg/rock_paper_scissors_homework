import random
from models.player import Player

class Game:
    
    def play_game(self, player_1, player_2):
        players = [player_1, player_2]
        choices = []
        choices.append(player_1.choice)
        choices.append(player_2.choice)
        winner = ""

        if choices[0] == choices[1]:
            winner = None
        elif "rock" in choices and "scissors" in choices:
            winner = players[choices.index("rock")]
        elif "scissors" in choices and "paper" in choices:
            winner = players[choices.index("scissors")]
        elif "paper" in choices and "rock" in choices:
            winner = players[choices.index("paper")]
        return winner

    def generate_computer_player(self):
        choice_list = ["rock", "paper", "scissors"]
        computer_player = Player("The Computer", random.choice(choice_list))

        return computer_player
