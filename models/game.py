class Game():

    def __init__(self, name):
        self.name = name
    
    def determine_winner(self, player1, player2):
        if player1.choice == player2.choice:
            return None
        if player1.choice == "rock":
            if player2.choice == "paper":
                return player2
            if player2.choice == "scissors":
                return player1
        if player1.choice == "paper":
            if player2.choice == "rock":
                return player1
            if player2.choice == "scissors":
                return player2
        if player1.choice == "scissors":
            if player2.choice == "rock":
                return player2
            if player2.choice == "paper":
                return player1


    



