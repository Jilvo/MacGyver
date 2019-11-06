"""V1.0--This Module is in charge of changing the score
and if Macgyver hit the guard,set the win or the lose """
class Score():
    # init the class
    def __init__(self):
        self.value = 0
        self.is_finished = False
        self.is_win = False
    # if we win
    def win(self):
        print("you win")
        self.is_finished = True
        self.is_win = True
    # if we lose
    def lose(self):
        print("you lose")
        self.is_finished = True
    def increm_value(self, val=1):
        self.value = self.value + val
