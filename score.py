"""This Module is in charge of leaving the game after the win or the lose of Macgyver"""

# import modules
import sys
# the class is call when Macgyver hit the guard
class Score():
    # init the class
    def __init__(self):
        self.score = 0
    # if we win
    def win(self):
        print("you win")
        sys.exit(0)
    # if we lose
    def lose(self):
        print("you lose")
        sys.exit(0)