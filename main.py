from score import Score
from maze_charging import Labyrinth
from perso import Perso
from lab_pygame import *
""" V1.1--Main file who will be imported other file and run them"""

set_the_score = Score()
game = Labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
mac_x, mac_y, list_macgyver = game.find_player()
macgyver_perso = Perso(mac_x, mac_y, game.structure, list_macgyver)