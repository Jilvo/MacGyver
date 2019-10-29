"""This Module is in charge of leaving the game after the win or the lose of Macgyver"""

# import modules
import sys
# the class is call when Macgyver hit the guard
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
        # sys.exit(0)
    # if we lose
    def lose(self):
        print("you lose")
        self.is_finished = True
        # sys.exit(0)
    def increm_value(self,val=1):
        self.value= self.value + val



