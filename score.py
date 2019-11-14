"""V1.1--This Module is in charge of changing the score
and if Macgyver hit the guard,set the win or the lose """
class Score():
    """This class was created for increm the score and return the victory and defeat"""
    def __init__(self):
        """init the class"""
        self.value = 0
        self.is_finished = False
        self.is_win = False
    def win(self):
        """if we win"""
        print("you win")
        self.is_finished = True
        self.is_win = True
    def lose(self):
        """if we lose"""
        print("you lose")
        self.is_finished = True
    def increm_value(self, val=1):
        """Increm the score"""
        self.value = self.value + val
