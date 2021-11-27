class Game:
    
    def play_game(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2 
        players = [self.player_1, self.player_2]
        choices = []
        choices.append(self.player_1.choice)
        choices.append(self.player_2.choice)
        winner = ""

        if choices[0] == choices[1]:
            winner = None
        elif "rock" in choices and "scissors" in choices:
            winner = players[choices.index("rock")].name
        elif "scissors" in choices and "paper" in choices:
            winner = players[choices.index("scissors")].name
        elif "paper" in choices and "rock" in choices:
            winner = players[choices.index("paper")].name
        return winner

    def play_computer(self):
        human_player = Player()
