class Player():

    def __init__(self, name):
        self.name = name
        self.choice = ""

    def assign_choice_to_player(self, input_choice):
        self.choice = input_choice